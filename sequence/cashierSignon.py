
from function.clickButton import clickBtn
from function.clickButton import clickKeypad
from function.input import inputText_Re
from function.util import checkIfExist
from function.util import checkIfExistWithTitleRe
from pywinauto.keyboard import send_keys
from configuration.config import config
import time
def cashierSignon(dlg) :
    cashier = config.cashier_cred
    cashier_btn = config.cashier_btn
    clickBtn(dlg, cashier_btn)
    isNewDate=False
    time.sleep(10)
    while(checkIfExist(dlg, 'VQP', control_type='Window')):
        if(checkIfExistWithTitleRe(dlg, "Opened", 'Text')):
            clickBtn(dlg, 'OK')
        elif(checkIfExistWithTitleRe(dlg, "Cashier", 'Text')):
            clickBtn(dlg, 'OK')
            return
    inputText_Re(dlg, cashier.cashier_id, "Cashier")
    send_keys("{TAB}")
    inputText_Re(dlg, cashier.cashier_pass, "Password")
    send_keys("{ENTER}")
    if(isNewDate):
        time.sleep(5)
        inputText_Re(dlg, '20000')
        clickKeypad(dlg, 'check')
    clickKeypad(dlg, 'check')
    if(checkIfExist(dlg, 'OK')):
        clickBtn(dlg, 'OK')