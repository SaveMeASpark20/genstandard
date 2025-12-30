from tender.clickTender import clickTender
from function.clickButton import clickBtn
from function.input import inputText
from pywinauto.keyboard import send_keys
from configuration.config import config


def tender_free(dlg, free_btn):
    on_account = config.on_account
    
    clickBtn(dlg, free_btn)        
    inputText(dlg, on_account.chargeTo, name='Charge To:')
    send_keys("{ENTER}")
    