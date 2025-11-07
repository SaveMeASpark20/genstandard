from function.clickButton import clickBtn

from function.clickButton import doubleClickDateArrow
from function.util import checkIfExist
from function.util import generate_random_number
from function.input import inputText
from function.input import focusOnlyOnInput

from configuration.config import config
from pywinauto.keyboard import send_keys


def depo_cust_info(dlg):
    bulk = config.bulk
    contract = generate_random_number(6)
    phone_no = generate_random_number(7)

    clickBtn(dlg, bulk.deposit_name)

    duplicate_exists = True  # Set initial flag to
    while duplicate_exists:
        inputText(dlg, contract, "Contract")  # Input the random number
        send_keys("{TAB}")
        #Check if the contract number is a duplicate
        duplicate_exists = checkIfExist(dlg, 'Duplicate Contract Number!', "Text")
        if duplicate_exists:
            clickBtn('OK') 

    inputText(dlg, bulk.name, "Name")
    send_keys("{TAB}")
    inputText(dlg, phone_no, "Phone No")
    send_keys("{TAB}")
    doubleClickDateArrow(dlg)
    send_keys("{TAB}")
    inputText(dlg, bulk.time, "Time")
    send_keys("{TAB}")
    inputText(dlg, bulk.funcRoom, "FuncRoom")
    send_keys("{ENTER}")

def depo_cust_noinfo(dlg):
    bulk = config.bulk
    clickBtn(dlg, bulk.deposit_name)
    focusOnlyOnInput(dlg, 'Contract')
    send_keys("{TAB}")
    focusOnlyOnInput(dlg, 'Name')
    send_keys("{TAB}")
    focusOnlyOnInput(dlg, 'Phone No')
    send_keys("{TAB}")
    # focusOnlyOnInput(dlg, 'Date')
    send_keys("{TAB}")
    focusOnlyOnInput(dlg, 'Time')
    send_keys("{TAB}")
    focusOnlyOnInput(dlg, 'FuncRoom')
    send_keys("{ENTER}")