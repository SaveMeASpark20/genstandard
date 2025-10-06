from function.clickButton import clickBtn

from function.clickButton import doubleClickDateArrow
from function.util import checkIfExist
from function.util import generate_random_number
from function.input import inputText

from configuration.config import config
from pywinauto.keyboard import send_keys


def depo_cust_info(dlg):
    bulk = config.bulk
    manager = config.manager_cred
    clickBtn(dlg, bulk.deposit_name)

    duplicate_exists = True  # Set initial flag to
    while duplicate_exists:
        inputText(dlg, generate_random_number(6), "Contract")  # Input the random number
        send_keys("{TAB}")
        #Check if the contract number is a duplicate
        duplicate_exists = checkIfExist(dlg, 'Duplicate Contract Number!', "Text")
        if duplicate_exists:
            clickBtn('OK') 

    inputText(dlg, bulk.name, "Name")
    send_keys("{TAB}")
    inputText(dlg, generate_random_number(7), "Phone")
    send_keys("{TAB}")
    doubleClickDateArrow(dlg)
    send_keys("{TAB}")
    inputText(dlg, bulk.time, "Time")
    send_keys("{TAB}")
    inputText(dlg, bulk.funcRoom, "FuncRoom")
    send_keys("{ENTER}")
    clickBtn(dlg, 'DISC')
    inputText(dlg, manager.manager_id, "Manager")
    send_keys("{TAB}")
    inputText(dlg, manager.manager_pass, "Password")
    send_keys("{ENTER}")