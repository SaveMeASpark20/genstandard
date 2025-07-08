from configuration.config import config
from function.input import inputText
import time
from pywinauto.keyboard import send_keys
from function.clickButton import clickKeypad

def clickTender(dlg, tender_btn, retries=3, delay=2, amounts= 0 , control_type="Button"):
    """Attempts to click a button multiple times with a delay in between."""
    attempt = 0
    tenderBtnVal = {
        "CASH": "CASH",
        "CREDIT CARD": "CREDIT\r\nCARD",
        "DEBIT CARD": "DEBIT\r\nCARD",
        "GIFT CERT" : "GIFT CERT",
        "CHECKS": "CHECKS",
        "ON ACCOUNT" : "ON\r\nACCOUNT"
    }
    btn = tenderBtnVal.get(tender_btn)
    credit_card = config.credit_card
    debit_card = config.debit_card
    gift_cert = config.gift_cert
    on_account = config.on_account
    checks = config.checks
    if btn is None:
        print(f"Button '{tender_btn}' not found in keypad mapping.")
        return
    while attempt < retries:
        try:
            button = dlg.child_window(title_re=btn, control_type=control_type)
            button.click()
            print(f"Clicked '{btn}' successfully.")
            if(tender_btn =='CREDIT CARD'):
                inputText(dlg, credit_card.appCode, "ApprCode")
                send_keys("{ENTER}")
                clickKeypad(dlg, "exact amount")
                return  # Exit function after a successful click
            if(tender_btn == 'CASH'):
                clickKeypad(dlg, "exact amount")
                return
            if(tender_btn == 'DEBIT CARD'):
                inputText(dlg, debit_card.Invoice, "Invoice")
                send_keys("{ENTER}")
                clickKeypad(dlg, "exact amount")
                return
            if(tender_btn == 'GIFT CERT'):
                inputText(dlg, gift_cert.giftcert, "GIFT CERT")
                send_keys("{ENTER}")
                clickKeypad(dlg, "exact amount")
                return
            
            if(tender_btn == 'ON ACCOUNT'):
                inputText(dlg, on_account.chargeTo, "Charge To")
                send_keys("{ENTER}")
                clickKeypad(dlg, "exact amount")
                return
            
            if(tender_btn == 'CHECKS'):
                inputText(dlg, checks.check, "CHECKS")
                send_keys("{ENTER}")
                inputText(dlg, checks.bank, "Bank")
                send_keys("{ENTER}")
                inputText(dlg, checks.acc_name, "Account Name")
                send_keys("{ENTER}")
                inputText(dlg, checks.acc_no, "Account No")
                send_keys("{ENTER}")
                send_keys("{ENTER}")
                clickKeypad(dlg, "exact amount")
                return

        except Exception as e:
            print(f"Attempt {attempt + 1}: Failed to click '{btn}' - {e}")
            time.sleep(delay)
            attempt += 1

    print(f"Failed to click '{btn}' after {retries} attempts.")


