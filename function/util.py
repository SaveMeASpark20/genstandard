import random 
import time
import re

from function.clickButton import clickKeypad

def checkIfExist(dlg, name, control_type = "Button"): 
    child = dlg.child_window(title=name, control_type=control_type)
    if(child.exists()):
        return True
    return False

def generate_random_number(digits: int) -> int:
    """Generate a random number with the specified number of digits."""
    if digits < 1:
        raise ValueError("Number of digits must be at least 1")
    
    lower_bound = 10**(digits - 1)  # Smallest number with given digits (e.g., 100 for 3 digits)
    upper_bound = (10**digits) - 1  # Largest number with given digits (e.g., 999 for 3 digits)

    return random.randint(lower_bound, upper_bound)

def checkIfExistWithRegex(dlg, name, control_type = "Text") :
    all_text_controls = dlg.descendants(control_type="Text")

    # Filter manually with regex
    matches = [ctrl for ctrl in all_text_controls if re.search(r"\bPAX\b", ctrl.window_text(), re.IGNORECASE)]

    if matches:
        print("✅ PAX FOUND")
        return True
    else:
        return False


def checkIfExistWithTitleRe(dlg, name, control_type = "Button"): 
    title_re = f".*{name}.*"
    child = dlg.child_window(title_re=title_re, control_type=control_type)
    if(child.exists()):
        return True
    return False

