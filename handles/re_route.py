from function.util import checkIfExist
from function.clickButton import clickBtn

def re_route(dlg, prompt_header="KITCHEN MONITOR ERROR", reroute_btn="RE-ROUTE", reroute_prn='P O S'):
    # Check if the prompt window exists
    if checkIfExist(dlg, prompt_header, control_type='Window'):
        # Click the re-route button and the POS button
        clickBtn(dlg, reroute_btn)
        clickBtn(dlg, reroute_prn)
        # After clicking, recursively call re_route to check again
        re_route(dlg, prompt_header, reroute_btn, reroute_prn)
    from function.util import checkIfExist
from function.clickButton import clickBtn

def re_route(dlg, prompt_header="KITCHEN MONITOR ERROR", reroute_btn="RE-ROUTE", reroute_prn='P O S', max_retries=5, current_retry=0):
    if current_retry >= max_retries:
        print("Max retries reached. Exiting function.")
        return
    
    if checkIfExist(dlg, prompt_header, control_type='Window'):
        clickBtn(dlg, reroute_btn)
        clickBtn(dlg, reroute_prn)
        # Call recursively with incremented retry count
        re_route(dlg, prompt_header, reroute_btn, reroute_prn, max_retries, current_retry + 1)
    
    elif checkIfExist(dlg, 'Re-route'):
        clickBtn(dlg, 'Re-route')
        clickBtn(dlg, 'P O S')
        re_route(dlg, prompt_header, reroute_btn, reroute_prn, max_retries, current_retry + 1)
    
    elif checkIfExist(dlg, 'RE-ROUTE'):
        clickBtn(dlg, 'RE-ROUTE')
        clickBtn(dlg, 'P O S')
        re_route(dlg, prompt_header, reroute_btn, reroute_prn, max_retries, current_retry + 1)

    # Check if the "Re-route" window exists
    elif checkIfExist(dlg, 'Re-route'):
        clickBtn(dlg, 'Re-route')
        clickBtn(dlg, 'P O S')
        # Recursively call re_route again to check after clicking
        re_route(dlg, prompt_header, reroute_btn, reroute_prn)
    
    # Check if the "RE-ROUTE" window exists
    elif checkIfExist(dlg, 'RE-ROUTE'):
        clickBtn(dlg, 'RE-ROUTE')
        clickBtn(dlg, 'P O S')
        # Recursively call re_route again to check after clicking
        re_route(dlg, prompt_header, reroute_btn, reroute_prn)
