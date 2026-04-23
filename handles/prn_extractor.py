import re
from configuration.config import config
# file_path = r"E:\G93ZZ\winvqp93\888.prn"

def prn_extractor():
    file_path = config.prn_path
    with open(file_path, "r", encoding="utf-8", errors="ignore") as f:
        content = f.read()
        
    # =========================================================
    # STEP 1: SPLIT FILE INTO BIG BLOCKS
    # =========================================================
    # We split by blank lines because POS files separate sections
    # with large empty spacing.
    # Regex breakdown:
    # \n\s*\n{2,}
    # ├── \n        → newline
    # ├── \s*       → optional spaces
    # ├── \n{2,}    → at least 2 new lines (big separation)
    #
    # This helps group each "document chunk" together.
    # =========================================================
    blocks = re.split(r"\n\s*\n{6,}", content)

    transactions = []

    # =========================================================
    # STEP 2: CLASSIFY EACH BLOCK
    # =========================================================
    for b in blocks:
        # Normalize spacing remove newline also
        text = b.strip()

        if not text:
            continue

        # Detect document type
        doc_type_sup = ""

        if "Sales INVOICE" in text:
            doc_type = "SALES"
            if "ACCOUNTING COPY" in text:
                doc_type_sup = "AC"

        elif "Z-READING" in text or "TERMINAL CLOSING" in text:
            doc_type = "READING"
            doc_type_sup = "ZREADING"

        elif "X-READING" in text or "CASHIER CUT-OFF" in text:
            doc_type = "READING"
            doc_type_sup = "XREADING"

        elif "TERMINAL-READING" in text:
            doc_type = "READING"
            doc_type_sup = "REG"

        elif "CASHIER READING" in text:
            doc_type = "READING"
            doc_type_sup = "CASHIER"

        else:
            doc_type = "OTHER"


        # =========================================================
        # STEP 3: ONLY PROCESS SALES INVOICE
        # =========================================================
        if doc_type == "SALES":

            # ----------------------------
            # TRANSACTION NUMBER
            # ----------------------------
            # Regex breakdown:
            #
            # Trans#            → literal text match
            # \s+               → spaces after label
            # (?:\d+\s+)?       → optional "0000 " prefix
            # ├── ?:            → non-capturing group
            # ├── \d+          → digits (0000)
            # ├── \s+          → space
            # (\d+)             → FINAL transaction number (CAPTURED)
            #
            # Example:
            # Trans# 0000 0100000020
            #                 ↑ captured
            # ----------------------------
            trans_match = re.search(r"Trans#\s+(?:\d+\s+)?(\d+)", text)
            # ----------------------------
            # GUEST COUNT + DISCOUNT PAX
            # ----------------------------
            # Example:
            # Guest Count: 3 (2 PWD)
            # Breakdown:
            # Guest Count:      → label
            # \s*              → optional spaces
            # (\d+)            → total guests (CAPTURED)
            #
            # (?: ... )?       → optional discount section
            #
            # \((\d+)          → discount pax number
            # (SC|PWD|...)     → discount type
            #
            # Entire "(2 PWD)" is optional
            # ----------------------------
            guest_match = re.search(
                r"Guest Count:\s*(\d+)(?:\s*\((\d+)\s*(SC|PWD|NACD|MOV|SOLO)\))?",
                text
            )
            # ----------------------------
            # DATE + TIME
            # ----------------------------
            # Example:
            # 09/22/2025 13:16
            #
            # (\d{2}/\d{2}/\d{4}) → date
            # \s+                → space
            # (\d{2}:\d{2})      → time
            # ----------------------------
            date_match = re.search(r"(\d{2}/\d{2}/\d{4})\s+(\d{2}:\d{2})", text)
            # ----------------------------
            # SAFE EXTRACTION
            # ----------------------------
            trans_no = trans_match.group(1) if trans_match else None

            if guest_match:
                guest_count = int(guest_match.group(1))
                pax = int(guest_match.group(2)) if guest_match.group(2) else 0
                dc_pax_type = guest_match.group(3) if guest_match.group(3) else None
            else:
                guest_count = 0
                pax = 0
                dc_pax_type = None

            if date_match:
                date = date_match.group(1)
                time = date_match.group(2)
            else:
                date = None
                time = None
            
            # Detect discount
            if re.search(r"SENIOR", text, re.IGNORECASE):
                discount = "SENIOR"
            elif re.search(r"PWD", text, re.IGNORECASE):
                discount = "PWD"
            elif re.search(r"NACD", text, re.IGNORECASE):
                discount = "NACD"
            elif re.search(r"SOLO", text, re.IGNORECASE):
                discount = "SOLO"
            elif re.search(r"MEDAL", text, re.IGNORECASE):
                discount = "MEDAL"
            elif re.search(r"PROMO", text, re.IGNORECASE):
                discount = "PROMO"
            elif re.search(r"EMPLOYEE", text, re.IGNORECASE):
                discount = "EMPLOYEE"
            else:
                discount = "NONE"

            # ----------------------------
            # TENDER TYPE (simple keyword check)
            # ----------------------------
            if "CREDIT CARD" in text:
                tender = "CREDIT CARD"
            elif "CHECKS" in text:
                tender = "CHECK"
            elif "CASH" in text:
                tender = "CASH"
            else:
                tender = "UNKNOWN"

            # ----------------------------
            # TRANSACTION TYPE
            # ----------------------------
            if "DINE IN" in text:
                trantype = "DINE IN"
            elif "TAKE OUT" in text:
                trantype = "TAKE OUT"
            elif "DELIVERY" in text:
                trantype = "DELIVERY"
            elif "MISC" in text:
                trantype = "MISC"
            else:
                trantype = "UNKNOWN"


            # ----------------------------
            # STORE RESULT
            # ----------------------------
            transactions.append({
                "type": doc_type or '',
                "trans_no": trans_no,
                "tran_type": trantype,
                "tender": tender,
                "guest_count": guest_count,
                "discount": discount,
                "pax": pax,
                "dc_pax_type": dc_pax_type,
                "date": date,
                "time": time,
                "type_sup": doc_type_sup or ''
            })


        # =========================================================
        # STEP 4: OPTIONAL - STORE READINGS
        # =========================================================
        elif doc_type != "SALES":
            transactions.append({
                "type": doc_type,
                "type_sup": doc_type_sup ,   # keeps XREADING / ZREADING info if you still want it
                "raw": text[:20]      # preview only
        })
    # =========================================================
    # STEP 5: OUTPUT
    # =========================================================
    return transactions
    
    

def query_transaction(data, **filters):
    """
    Filter extracted PRN data using keyword arguments.

    Example:
        query_transactions(data, type="SALES", tender="CASH")
    """

    results = data
    print(results)

    for key, value in filters.items():
        results = [t for t in results if t.get(key) == value]

    return results

#examples
# sales = query_transactions(data, type="SALES")
# senior_sales = query_transactions(data, discount="SENIOR")
#     filtered = query_transactions(
#     data,
#     type="SALES",
#     tran_type="DINE IN",
#     tender="CASH",
#     discount="SENIOR"
# )

doc_type="SALES",
tran_type="DINE IN",
tender="CASH"

if __name__ == "__main__":
    data = prn_extractor()
    query = query_transaction(data, type="SALES", 
                            tran_type="TAKE OUT",
                            tender="CASH", 
                            discount = 'PWD',
                            guest_count = 2)[0]
    print("data: ", data)
    print("query", query)
