from function.clickButton import clickBtn
from function.clickButton import clickKeypad



def return_to_product(dlg, return_btn='RETURN', isFinalPaymentReturn=False):
    # Try clicking the RETURN button
    clickBtn(dlg, return_btn)

    clickKeypad(dlg, 'check')

    if isFinalPaymentReturn:
        clickBtn(dlg, 'FINAL\r\nPAYMENT')

