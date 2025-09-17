from function.clickButton import clickBtn
from function.clickButton import clickKeypad
from function.clickButton import clickNonBtn
from function.input import inputText_Re
from pywinauto.keyboard import send_keys
from function.util import checkIfExist

def split_bill(dlg, split_bill_pax, pax):
    clickBtn(dlg, 'SPLIT\r\nBILL')
    inputText_Re(dlg, split_bill_pax, 'Split by')
    send_keys("{ENTER}")
    if checkIfExist(dlg, f'Cannot Be > {pax}.', control_type='Text'):
        clickBtn(dlg, 'OK')
        print("Split Bill Pax is > than pax")