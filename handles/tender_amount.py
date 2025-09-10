from tender.clickTender import clickTender

def tender_amount(dlg, amounts, tenders):
    
    if amounts :
        for tender, amount in zip(tenders, amounts):
            # tender_status:
            #  1 = "amount tendered",
            #  2 = " amount is greater than price exact amount execute",
            #  3 = "no amount, exact amount execute"
            if(tender and amount):
                tender_status = clickTender(dlg, tender, amount=amount) #add the amount
                if tender_status == 2 or tender_status == 3:
                    return
    else :
        for tender in tenders:
            print(f"ito ba yung na aano? {tender}")
            clickTender(dlg, tender)