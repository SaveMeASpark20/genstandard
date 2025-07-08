from function.clickButton import clickBtn
from function.clickButton import clickKeypad
from function.input import inputText
from pywinauto.keyboard import send_keys
from configuration.config import config

def generateReport(dlg, report_name) :
    mgrcred = config.manager_cred
    clickBtn(dlg, report_name)
    inputText(dlg, mgrcred.manager_id, "Manager")
    send_keys("{TAB}")
    inputText(dlg, mgrcred.manager_pass, "Password")
    send_keys("{ENTER}")
    clickBtn(dlg, 'PRINT')