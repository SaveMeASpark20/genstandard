from function.clickButton import clickBtn 
from function.util import checkIfExistEscapeSpecChars
from function.clickButton import clickNonBtn
from function.clickButton import clickKeypad
from function.input import inputText_Re
from function.util import checkIfExist
from handles.cashier_sign_setup_table import cashier_sign_setup_table
from tender.clickTender import clickTender
from pywinauto.keyboard import send_keys
import time


def move_prod_other_table(dlg, mark_prods, moveTo, pax, cashier_id, isPos=False):
    clickBtn(dlg, 'TABLE\r\nFUNCTION')
    for mark_prod in mark_prods:
        clickNonBtn(dlg, mark_prod, control_type='Text')
        clickBtn(dlg, 'MARK')
    clickBtn(dlg, 'MOVE TO')
    clickBtn(dlg, moveTo)
    while(checkIfExistEscapeSpecChars(dlg, 'PAX', control_type='Edit')):
        print(f"PAX input showed means table to be move is empty...")
        inputText_Re(dlg, pax, "PAX")
        send_keys("{ENTER}")
    while(checkIfExist(dlg, "Move/Transfer Qty", control_type="Group")):
        send_keys("{ENTER}")
    clickBtn(dlg, 'OK')
    clickKeypad(dlg, 'check')
    if(checkIfExist(dlg, 'FINAL\r\nPAYMENT') and isPos):
        clickBtn(dlg, 'FINAL\r\nPAYMENT')
        clickTender(dlg, 'CASH')
        while not checkIfExist(dlg, 'Server?', control_type="Edit"):
            wait_time = 2
            print("waiting makita yung server input uli")
            if checkIfExist(dlg, 'OK'):
                clickBtn(dlg, 'OK')
            time.sleep(wait_time)
        #kapag  maglalabas ng OK to print acc copy
        while(checkIfExist(dlg, 'OK')):
            clickBtn(dlg, 'OK')
        cashier_sign_setup_table(dlg, cashier_id, moveTo)
    else:
        clickBtn(dlg, 'STORE\r\nORDER')
    
    while(checkIfExist(dlg, 'OK')):
        clickBtn(dlg, 'OK')