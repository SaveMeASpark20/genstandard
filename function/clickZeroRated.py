from function.input import inputText
from configuration.config import config
from pywinauto.keyboard import send_keys
def clickZeroRated(dlg):
    dine_in = config.dine_in
    inputText(dlg, dine_in.customer_id, "ID")
    send_keys("{TAB}")
    inputText(dlg, dine_in.customer_name, "Cust Name")
    send_keys("{TAB}")
    inputText(dlg, dine_in.address, "Address")
    send_keys("{TAB}")
    inputText(dlg, dine_in.tin, "TIN")
    send_keys("{TAB}")
    inputText(dlg, dine_in.bus_style, "Bus Style")
    send_keys("{ENTER}")  