from function.clickButton import clickBtn
from function.clickButton import clickNonBtn
from function.util import checkIfExist
from function.clickButton import clickKeypad
from handles.cashier_sign_setup_table import cashier_sign_setup_table

def split_table(dlg, mark_prods, cashier_id, table):
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
    clickBtn(dlg, 'FINAL\r\nPAYMENT')
    clickBtn(dlg, 'CASH')
    clickKeypad(dlg, 'exact amount')
    while(checkIfExist(dlg, 'OK')):
        clickBtn(dlg, 'OK')
    cashier_sign_setup_table(dlg, cashier_id, table)
