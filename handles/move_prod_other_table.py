from function.clickButton import clickBtn 
from function.util import checkIfExistEscapeSpecChars
from function.clickButton import clickNonBtn
from function.clickButton import clickKeypad
from function.input import inputText
from function.util import checkIfExist
from handles.cashier_sign_setup_table import cashier_sign_setup_table
from tender.clickTender import clickTender
from pywinauto.keyboard import send_keys


def move_prod_other_table(dlg, mark_prods, moveTo, pax, cashier_id):
    clickBtn(dlg, 'TABLE\r\nFUNCTION')

    for mark_prod in mark_prods:
        clickNonBtn(dlg, mark_prod, control_type='Text')
        clickBtn(dlg, 'MARK')
    clickBtn(dlg, 'MOVE TO')
    clickBtn(dlg, moveTo)
    while(checkIfExistEscapeSpecChars(dlg, 'PAX', control_type='Edit')):
        print(f"PAX input showed means table to be move is empty...")
        inputText(dlg, pax, "PAX")
        send_keys("{ENTER}")
    while(checkIfExist(dlg, "Move/Transfer Qty", control_type="Group")):
        send_keys("{ENTER}")
    clickBtn(dlg, 'OK')
    clickKeypad(dlg, 'check')
    clickBtn(dlg, 'FINAL\r\nPAYMENT')
    clickTender(dlg, 'CASH')
    #kapag  maglalabas ng OK to print acc copy
    while(checkIfExist(dlg, 'OK')):
        clickBtn(dlg, 'OK')
    cashier_sign_setup_table(dlg, cashier_id, moveTo)