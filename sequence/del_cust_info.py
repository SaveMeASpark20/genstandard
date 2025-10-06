 
from configuration.config import config
from function.clickButton import clickDeliveryBtn
from function.input import inputText
from function.input import inputTextByIndex
from pywinauto.keyboard import send_keys
from function.clickButton import clickBtn
from function.clickButton import clickKeypad
import time

def del_cust_info(dlg):
    delivery = config.delivery
    clickDeliveryBtn(dlg, "new")
    inputText(dlg, delivery.phone, "Phone")
    send_keys("{TAB}")
    inputText(dlg, delivery.loc, "Loc/Ext")
    send_keys("{TAB}")
    inputText(dlg, delivery.name, "Name    ")
    send_keys("{TAB}")
    inputText(dlg, delivery.address, "Address")
    send_keys("{TAB}")
    inputTextByIndex(dlg, delivery.address2, 4)
    send_keys("{TAB}")
    inputText(dlg, delivery.grid, "Grid/Area")
    send_keys("{TAB}")
    inputText(dlg, delivery.comment, "Comment")
    send_keys("{TAB}")
    inputText(dlg, delivery.note, "Note")
    send_keys("{ENTER}")
