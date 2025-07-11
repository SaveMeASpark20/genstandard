from function.clickButton import clickBtn
from pywinauto.keyboard import send_keys
from function.input import inputText

def cashier_sign_setup_table(dlg, cashier_id, table, pax=None) :
    inputText(dlg, cashier_id, 'Server')
    send_keys("{ENTER}")
    clickBtn(dlg, table)
    if(pax):
        inputText(dlg, pax, "PAX")
        send_keys("{ENTER}")