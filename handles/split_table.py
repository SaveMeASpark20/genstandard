from function.clickButton import clickBtn
from function.clickButton import clickNonBtn
from function.util import checkIfExist
from function.clickButton import clickKeypad
from tender.clickTender import clickTender
import time
from handles.cashier_sign_setup_table import cashier_sign_setup_table
from pywinauto.keyboard import send_keys


def split_table(dlg, mark_prods,table, cashier_id, isPos=False):
    clickBtn(dlg, 'TABLE\r\nFUNCTION')    
    for mark_prod in mark_prods:
        clickNonBtn(dlg, mark_prod, control_type='Text')
        clickBtn(dlg, 'MARK')
    clickBtn(dlg, 'SPLIT TABLE')
    clickBtn(dlg, 'OK')
    if(checkIfExist(dlg, 'VQP', control_type='Window') and checkIfExist(dlg, 'YES')):
        clickBtn(dlg, 'YES')
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
        cashier_sign_setup_table(dlg, cashier_id, table=table)
    else:
        clickBtn(dlg, 'STORE\r\nORDER')


    while(checkIfExist(dlg, 'OK')):
        clickBtn(dlg, 'OK')

