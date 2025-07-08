from function.clickButton import clickBtn
from function.clickButton import clickKeypad

def inputText(dlg, text, name):
    try:
        title_re = f".*{name}.*"
        textbox = dlg.child_window(control_type="Edit", title_re=title_re)  # Adjust this if needed
        
        textbox.set_edit_text(str(text))
        print("Successful type: ", text)
    except Exception as e:
        print("Failed to type text:", e)


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
