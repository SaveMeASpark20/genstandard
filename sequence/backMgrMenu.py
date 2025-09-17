from function.clickButton import clickBtn
from function.clickButton import clickDeliveryBtn
from function.input import inputText_Re
from function.input import inputText
from configuration.config import config
from pywinauto.keyboard import send_keys


def clickBckMgrMenu(dlg, name, secondsToSleep=0) :
    mgrcred = config.manager_cred
    cashier_cred = config.cashier_cred
    if(name =='x'):
        clickDeliveryBtn(dlg, name)
    elif(name =='bacchusx') :
        inputText(dlg, cashier_cred.cashier_id, "Server?")
        send_keys("{ENTER}")
        clickBtn(dlg, 'MAIN MENU')
    else:
        clickBtn(dlg, name, secondsToSleep=secondsToSleep)
    inputText_Re(dlg, mgrcred.manager_id, "Manager")
    send_keys("{TAB}")
    inputText_Re(dlg, mgrcred.manager_pass, "Password")
    send_keys("{ENTER}")