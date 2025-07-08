from pywinauto import Application
import time
from configuration.config import config
from pywinauto.keyboard import send_keys

def clickBtn(dlg, button_name, retries=3, delay=2, control_type="Button", secondsToSleep=0):
    """Attempts to click a button multiple times with a delay in between."""
    attempt = 0
    while attempt < retries:
        try:
            button = dlg.child_window(title=button_name, control_type=control_type)
            if(secondsToSleep):
                time.sleep(secondsToSleep)
            button.click()
            print(f"Clicked '{button_name}' successfully.")
 
            return  # Exit function after a successful click
        except Exception as e:
            print(f"Attempt {attempt + 1}: Failed to click '{button_name}' - {e}")
            time.sleep(delay)
            attempt += 1

    print(f"Failed to click '{button_name}' after {retries} attempts.")

def clickKeypad(dlg, keypadVal, retries=3, delay=2, control_type="Button"):

    KeypadValToIndex = {
        "arrow_up": 0,
        7: 1,
        8: 2,
        9: 3,
        "arrow_down": 4,
        4: 5,
        5: 6,
        6: 7,
        "exact amount": 8,
        1: 9,
        2: 10,
        3: 11,
        "x": 12,
        0: 13,
        ".": 14,
        "check": 15
    }

    # Directly get the index
    found_index = KeypadValToIndex.get(keypadVal)

    if found_index is None:
        print(f"Number '{keypadVal}' not found in keypad mapping.")
        return


    """Attempts to click a button multiple times with a delay in between."""

    attempt = 0

    while attempt < retries:
        try:
            button = dlg.child_window(control_type=control_type,found_index=found_index)
            
            button.click_input()
            print(f"Clicked '{keypadVal}' successfully.")
            return
        except Exception as e:
            print(f"Attempt {attempt + 1}: Failed to click '{keypadVal}' - {e}")
            time.sleep(delay)
            attempt += 1

    print(f"Failed to click '{found_index}' after {retries} attempts.")


def clickDeliveryBtn(dlg, delivery_btn, class_name=None, retries=3, delay=2, control_type="Button"):
    """Attempts to click a button multiple times with a delay in between."""
    attempt = 0
    deliveryBtnVal = {
        "new": 0,
        "up": 1,
        "down": 2,
        "driver" : 3,
        "check": 4,
        "x":5
    }
    found_index = deliveryBtnVal.get(delivery_btn)

    if found_index is None:
        print(f"Button '{delivery_btn}' not found in keypad mapping.")
        return
    while attempt < retries:
        try:
            button = dlg.child_window(found_index=found_index, control_type=control_type)
            button.click()
            print(f"Clicked '{delivery_btn}' successfully.")
 
            return  # Exit function after a successful click
        except Exception as e:
            print(f"Attempt {attempt + 1}: Failed to click '{delivery_btn}' - {e}")
            time.sleep(delay)
            attempt += 1

    print(f"Failed to click '{delivery_btn}' after {retries} attempts.")


def clickNonBtn(dlg, button_name, retries=3, delay=2, control_type="Button", secondsToSleep=0):
    """Attempts to click a button multiple times with a delay in between."""
    attempt = 0
    while attempt < retries:
        try:
            button = dlg.child_window(title=button_name, control_type=control_type)
            if(secondsToSleep):
                time.sleep(secondsToSleep)
            button.click_input()
            print(f"Clicked '{button_name}' successfully.")
 
            return  # Exit function after a successful click
        except Exception as e:
            print(f"Attempt {attempt + 1}: Failed to click '{button_name}' - {e}")
            time.sleep(delay)
            attempt += 1

    print(f"Failed to click '{button_name}' after {retries} attempts.")


    
def clickBlkRecallBtn(dlg, btn_name):
    recallBtnVal = {
        "check": 6,
        "x":7
    }
    found_index = recallBtnVal.get(btn_name)
    button = dlg.child_window(control_type="Button",found_index=found_index)
    button.click()

    

def doubleClickDateArrow(dlg):
    dlg.click_input(coords=(418, 348))
    dlg.click_input(coords=(418, 348))






    

