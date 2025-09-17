from function.clickButton import clickBtn
from function.clickButton import clickKeypad
from function.util import checkIfExist
from handles.re_route import re_route
from pywinauto.keyboard import send_keys
from function.input import inputText


def store_order(dlg, cashier_id, table): 
    clickBtn(dlg, 'STORE\r\nORDER')
    re_route(dlg)
    # if(checkIfExist(dlg,'Re-route')):
    #     clickBtn(dlg, 'Re-route')
    #     clickBtn(dlg, 'P O S')
    
    # if(checkIfExist(dlg,'RE-ROUTE')):
    #     clickBtn(dlg, 'RE-ROUTE')
    #     clickBtn(dlg, 'P O S')

    inputText(dlg, cashier_id, "Server?")
    send_keys("{ENTER}")

    clickBtn(dlg, table)
    