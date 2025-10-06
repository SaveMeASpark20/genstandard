from function.clickButton import clickBtn
from function.clickButton import clickKeypad
import time
from pywinauto.keyboard import send_keys

def inputText(dlg, text, name, max_retries=5, delay=0.5):
    attempt = 0

    while attempt < max_retries:
        try:
            textbox = dlg.child_window(control_type="Edit", title=name)

            # Make sure the control exists and is visible
            if not textbox.exists(timeout=1):
                raise Exception(f"{text} not found")
            
            textbox.set_focus()
            send_keys(str(text), with_spaces=True)
            # textbox.set_edit_text(str(text))
            print(f"✅ Successfully typed: '{text}' on attempt {attempt + 1}")
            return True  # exit if success

        except Exception as e:
            print(f"⚠️ Attempt {attempt + 1} failed: {e}")
            attempt += 1
            time.sleep(delay)

    print("❌ Failed to type text after retries.")
    return False  # failed after retries

def inputText_Re(dlg, text, name, max_retries=5, delay=0.5):
    attempt = 0
    title_re = f".*{name}.*"

    while attempt < max_retries:
        try:
            textbox = dlg.child_window(control_type="Edit", title_re=title_re)

            # Make sure the control exists and is visible
            if not textbox.exists(timeout=1):
                raise Exception(f"{text} not found")
            
            textbox.set_focus()
            send_keys(str(text), with_spaces=True)
            print(f"✅ Successfully typed: '{text}' on attempt {attempt + 1}")
            return True  # exit if success

        except Exception as e:
            print(f"⚠️ Attempt {attempt + 1} failed: {e}")
            attempt += 1
            time.sleep(delay)

    print("❌ Failed to type text after retries.")
    return False  # failed after retries


def inputTextByIndex(dlg, text, index):
    try:
        edit_boxes = dlg.descendants(control_type="Edit")
        if index < len(edit_boxes):
            target_box = edit_boxes[index]
            target_box.set_edit_text(str(text))
            print(f"✅ Typed into Edit[{index + 1}]: '{text}'")
        else:
            print(f"❌ No Edit box at index {index}")
    except Exception as e:
        print(f"❌ Failed to type: {e}")

def inputTextOnScreen(dlg, text):
    for char in str(text):
        if char.isdigit():  # If the character is a number (0-9)
            clickKeypad(dlg, int(char))
        elif char.isalpha():  # If the character is a letter (a-z, A-Z)
            clickBtn(dlg, char.upper())  # Convert to uppercase for consistency
        elif char.isspace():  # If the character is a space
            clickBtn(dlg, "space bar")  # Adjust this based on your system
        else:
            clickBtn(dlg, char)
