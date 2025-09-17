from function.clickButton import clickBtn
from function.util import checkIfExist
from function.clickButton import clickKeypad
from function.input import inputText
from pywinauto.keyboard import send_keys
from handles.tender_amount import tender_amount
from tender.clickTender import clickTender
from function.util import checkIfExistVisibleClickable
import time


def first_table_final(dlg, cashier_id, table, amounts, tenders, wait_time = 2, is_split_table=False): 
    if(checkIfExist(dlg, 'DINE IN')):
            clickBtn(dlg, 'DINE IN')
    inputText(dlg, cashier_id, "Server?")
    send_keys("{ENTER}")
    clickBtn(dlg, table)
    if is_split_table:
        table_no = table.split()
        sub_table_no = 'A0' + table_no[1] + ':1'
        clickBtn(dlg, sub_table_no)
    clickKeypad(dlg, 'check')
    clickBtn(dlg, 'FINAL\r\nPAYMENT')
    tender_amount(dlg, amounts, tenders)
    if checkIfExistVisibleClickable(dlg, 'CASH') and not checkIfExist(dlg, 'VQP', control_type='Window'):
        print('Amount tendered not sufficient tender cash exact amount')
        clickTender(dlg, 'CASH')
    while not checkIfExist(dlg, 'Server?', control_type="Edit"):
        print("waiting makita yung server input uli")
        if checkIfExist(dlg, 'OK'):
            clickBtn(dlg, 'OK')
        time.sleep(wait_time)
    #kapag  maglalabas ng OK to print acc copy
    while(checkIfExist(dlg, 'OK')):
        clickBtn(dlg, 'OK')