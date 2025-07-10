from function.clickButton import clickBtn
from function.clickDisc import clickDiscount
from function.input import inputText
from pywinauto.keyboard import send_keys

def discount(dlg, manager_id, manager_pass, disc, customer_id, customer_name, address, tin, bus_style, promo_amount, dc_pax):
    clickBtn(dlg, 'DISC')
    inputText(dlg, manager_id, "Manager")
    send_keys("{TAB}")
    inputText(dlg, manager_pass, "Password")
    send_keys("{ENTER}")
    clickDiscount(dlg, disc, customer_id,customer_name, address, tin, bus_style, promo_amount, dc_pax )