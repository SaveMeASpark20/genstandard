import re
from configuration.config import config
from function.util import checkIfExist
from function.util import checkIfExistWithTitleRe
from function.clickButton import clickBtn, clickKeypad, clickBtnCoords
from function.input import inputText
from handles.prn_extractor import prn_extractor
from handles.prn_extractor import query_transaction
from pywinauto.keyboard import send_keys
from sequence.backMgrMenu import clickBckMgrMenu

def whatIsTransaction(dlg, trantype = ["DINE IN", "TAKE OUT", "DELIVERY", "MISC", "FREE", "BULK ORDER"]):
    for transaction in trantype:
        if(checkIfExistWithTitleRe(dlg, transaction, 'HeaderItem')):
            return transaction
    return None


def backToManager(dlg):
    currentTransaction = whatIsTransaction(dlg)
    restaurant_type = config.restaurant_type
    if(currentTransaction == None):
        print("Can't find Transaction")
    if currentTransaction == "DELIVERY":
        backToMgr = "x"
    elif restaurant_type == "FINE DINING" and currentTransaction in ["TAKE OUT", "DINE IN"]:
        backToMgr = "bacchusx"
        print("restaurant_type :", restaurant_type)
        print("Current_Transaction :", currentTransaction )
    else:
        backToMgr = "MGR MENU"
    print(backToMgr)
    clickBckMgrMenu(dlg, backToMgr)



def manager_void(dlg, manager_void_btn = 'MGR VOID', **kwargs):
    """
    -manager account
        check if required of manager
    -input invoice# or transaction#
    -reason(optional na muna ito basta may void)
        -check(kapag walang ilalagay na reason)
    -check(lalabas na yung ivovoid)
    -validate kung may header na void(control_type = "Text")
    check button TO void
    check if 
    Press Any Key for Accounting Copy. - click yes
    """
    coords_void_check = config.coords_void_check
    manager_cred = config.manager_cred
    void_button = re.sub(r'\d+$', '', manager_void_btn)

    clickBtn(dlg, void_button)
    if(checkIfExistWithTitleRe(dlg, "Manager Login", control_type="Group")):
        inputText(dlg , manager_cred.manager_id, "Manager Code:")
        send_keys("{TAB}")  
        inputText(dlg , manager_cred.manager_pass, "Password:")
        send_keys("{ENTER}")
    
    #need ko dito ng extractor sa prn para di ko manually aalamin kung ano ivovoid ko
    data = prn_extractor()

    filters = kwargs.get("trans_filter", {})

    # ✅ convert namespace → dict
    if not isinstance(filters, dict):
        filters = vars(filters)

    filtered_transactions = query_transaction(data, **filters)
    
    if not filtered_transactions:
        raise Exception("No matching transaction found")

    target = filtered_transactions[-1]
    print(target)
    trans_no = target.get("trans_no")

    inputText(dlg, trans_no, "Trans#")
    send_keys("{ENTER}")
    if (checkIfExist(dlg, "Reason:", control_type="ComboBox")):
        send_keys("{ENTER}")

    #this is done so that user will be manually input what trans if there's an issue
    if(checkIfExist(dlg, "VQP", control_type="Window")):
        raise Exception("Warning pls look it up")
    
    
    clickKeypad(dlg, "other check")
    if(checkIfExist(dlg, "V O I D", control_type="Window")):
        clickBtnCoords(dlg, coords_void_check)

    if(checkIfExist(dlg, "VQP", control_type="Window")):
        clickBtn(dlg, "OK")

    backToManager(dlg)






def backToMgr(dlg):
    currentTransaction = whatIsTransaction(dlg)
    restaurant_type = config.restaurant_type
    if(currentTransaction == None):
        print("Can't find Transaction")
    if currentTransaction == "DELIVERY":
        backToMgr = "x"
    elif restaurant_type == "FINE DINING" and currentTransaction in ["TAKE OUT", "DINE IN"]:
        backToMgr = "bacchusx"
        print("restaurant_type :", restaurant_type)
        print("Current_Transaction :", currentTransaction )
    else:
        backToMgr = "MGR MENU"
    print(backToMgr)
    clickBckMgrMenu(dlg, backToMgr)
    