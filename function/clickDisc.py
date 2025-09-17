from function.clickButton import clickBtn
from function.input import inputText_Re
from configuration.config import config
from function.util import checkIfExistWithRegex
from pywinauto.keyboard import send_keys

def clickDiscount(dlg, disc_name, customer_id, customer_name, address, tin, bus_style, promo_amount=20,dc_pax=1, restaurant_type='FASTFOOD'):
    restaurant_type = config.restaurant_type
    available_discounts = {
        "EMPLOYEE DISC": "EMPLOYEE\r\nDISC",
        "PROMO AMOUNT": "PROMO\r\nAMOUNT",
        "SENIOR DISC": "SENIOR\r\nDISC 20%",
        "SOLO PARENT" : "SOLO\r\nPARENT",
        "PWD DISC" : "PWD DISC\r\n20%",
        "NACD" : "NACD",
        "MEDAL OF VALOR" : "MEDAL OF\r\nVALOR",
    }
    
    # Find the best match in the available discounts
    for key, button_name in available_discounts.items():
        if key in disc_name.upper():  # Convert input to uppercase to allow case-insensitive matching
            clickBtn(dlg, button_name)
            if key == "PROMO AMOUNT":
                inputText_Re(dlg, promo_amount, 'Disc Amount:')
                send_keys("{ENTER}")
                return
            if key in ("SENIOR DISC", "SOLO PARENT", "PWD DISC", "NACD", "MEDAL OF VALOR"):
                while(checkIfExistWithRegex(dlg, 'PAX')):
                    # di pa pwede sa food kasi may pax at senior pax etc dun
                    inputText_Re(dlg, dc_pax, "PAX")
                    send_keys("{ENTER}")
                for i in range(dc_pax):
                    if(i==0):
                        inputText_Re(dlg, customer_id, "ID")
                        send_keys("{TAB}")
                        inputText_Re(dlg, customer_name, "Name")
                        send_keys("{TAB}")
                        inputText_Re(dlg, address, "Address")
                        send_keys("{TAB}")
                        inputText_Re(dlg, tin, "TIN")
                        send_keys("{TAB}")
                        inputText_Re(dlg, bus_style, "Bus Style")
                        send_keys("{ENTER}")
                    else:
                        inputText_Re(dlg, customer_id, "ID")
                        send_keys("{TAB}")
                        inputText_Re(dlg, customer_name, "Name")
                        send_keys("{ENTER}")
                return
            return
    print(f"Warning: No configure  discount found for '{disc_name}'")