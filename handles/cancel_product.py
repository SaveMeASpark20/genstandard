from function.clickButton import clickNonBtn
from function.clickButton import clickBtn
from function.clickButton import clickKeypad
from function.input import inputText_Re
from pywinauto.keyboard import send_keys
from function.clickButton import clickBtnCoords
from configuration.config import config


coords_x_btn = config.coords_x_btn


def cancel_product(dlg, cancel_prod, isFinalPayment, manager_id, manager_pass): 
    for product in cancel_prod:
        if(product and not isFinalPayment):
            clean_item = product.replace("\r\n", " ")
            clickNonBtn(dlg, clean_item, control_type='Text')
            clickKeypad(dlg, 'x')
            inputText_Re(dlg, manager_id, "Manager")
            send_keys("{TAB}")
            inputText_Re(dlg, manager_pass, "Password")
            send_keys("{ENTER}")
            clickBtn(dlg, 'YES')

def cancel_product_coords(dlg, cancel_prod, isFinalPayment, manager_id, manager_pass):
        for product in cancel_prod:
            if(product and not isFinalPayment):
                clean_item = product.replace("\r\n", " ")
                clickNonBtn(dlg, clean_item, control_type='Text')
                clickBtnCoords(dlg, coords_x_btn) #after punching check to go to tender section
                inputText_Re(dlg, manager_id, "Manager")
                send_keys("{TAB}")
                inputText_Re(dlg, manager_pass, "Password")
                send_keys("{ENTER}")
                clickBtn(dlg, 'YES')