from function.util import checkIfExist
from function.clickButton import clickBtn

# Fix: Handle Multiple button name variations, Track if whether any button was clicked.

def re_route(dlg, prompt_header="KITCHEN MONITOR ERROR", reroute_btns=None, reroute_prn_options=None, max_retries=5, current_retry=0):
    if current_retry >= max_retries:
        print("Max retries reached. Exiting re_route.")
        return

    # Set default button names if   
    # not provided
    if reroute_btns is None:
        reroute_btns = ['RE-ROUTE', 'Re-route']
    if reroute_prn_options is None:
        reroute_prn_options = ['P O S', 'POS']

    # Tracker to check if any button was clicked
    clicked = False
    clicked_button = None
    clicked_prn = None

    # Error Window Exists
    if checkIfExist(dlg, prompt_header, control_type='Window'):
        for btn in reroute_btns:
            if checkIfExist(dlg, btn):
                clickBtn(dlg, btn)
                clicked = True
                clicked_button = btn
                print(f"[RE_ROUTE] Clicked reroute button: {btn}")
                break

        for prn in reroute_prn_options:
            if checkIfExist(dlg, prn):
                clickBtn(dlg, prn)
                clicked = True
                clicked_prn = True
                print(f"[RE_ROUTE] Clicked reroute print option: {prn}")
                break
    # Fallback: No error window, but buttons exists.
    else:
        for btn in reroute_btns:
            if checkIfExist(dlg, btn):
                clickBtn(dlg, btn)
                clicked = True
                clicked_button = btn
                print(f"[RE_ROUTE] Clicked reroute button: {btn}")
                break

        for prn in reroute_prn_options:
            if checkIfExist(dlg, prn):
                clickBtn(dlg, prn)
                clicked = True
                clicked_prn = True
                print(f"[RE_ROUTE] Clicked reroute print option: {prn}")
                break

    if clicked:
        print(
            f"[RE_ROUTE] Action completed. "
            f"Button={clicked_button}, POS={clicked_prn}, "
            f"Retry={current_retry + 1}"
        )

        re_route(
            dlg,
            prompt_header,
            reroute_btns,
            reroute_prn_options,
            max_retries,
            current_retry + 1
        )
    else:
        print("[RE_ROUTE] No clickable buttons found. Stopping.")