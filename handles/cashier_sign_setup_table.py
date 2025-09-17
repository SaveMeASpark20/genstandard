from function.clickButton import clickBtn
from pywinauto.keyboard import send_keys
from function.input import inputText
from function.input import inputText_Re
from function.util import checkIfExist
from configuration.config import config
import time

def cashier_sign_setup_table(dlg, cashier_id, table, pax=None, wait_time=2) :
    pos_num = config.POS
    is_table_opened=True

    inputText(dlg, cashier_id, 'Server?')
    send_keys("{ENTER}")
    while is_table_opened:
        clickBtn(dlg, table)
        if checkIfExist(dlg, f'Table Is Opened at TERMINAL {pos_num}.', control_type="Text") or checkIfExist(dlg, 'VQP', control_type='Window'):
            print(f'Table Is Opened at TERMINAL {pos_num}.')
            clickBtn(dlg, 'OK')
            time.sleep(wait_time)
        else:
            is_table_opened=False    
    if(pax):
        inputText_Re(dlg, pax, "PAX")
        send_keys("{ENTER}")