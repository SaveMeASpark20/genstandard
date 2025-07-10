from function.clickButton import clickNonBtn
from function.clickButton import clickBtn
from function.clickButton import clickKeypad
from function.input import inputText
from pywinauto.keyboard import send_keys


def cancel_product(dlg, cancel_prod, isFinalPayment, manager_id, manager_pass): 
    for product in cancel_prod:
        if(product and isFinalPayment==False):
            clean_item = product.replace("\r\n", " ")
            clickNonBtn(dlg, clean_item, control_type='Text')
            clickKeypad(dlg, 'x')
            inputText(dlg, manager_id, "Manager")
            send_keys("{TAB}")
            inputText(dlg, manager_pass, "Password")
            send_keys("{ENTER}")
            clickBtn(dlg, 'YES')