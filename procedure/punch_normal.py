from typing import List, Optional
from function.clickButton import clickBtn
from function.util import checkIfExist
from function.util import checkIfExistVisibleClickable
from tender.clickTender import clickTender
from handles.initial_punch import initial_punch
from handles.zero_rated import zero_rated
from handles.cust_info import cust_info
from handles.discount import discount
from handles.tender_amount import tender_amount
from configuration.config import config
from handles.re_route import re_route
from handles.return_to_product import return_to_product
from handles.cancel_all import cancel_all
from function.clickButton import clickBtnCoords
from handles.add_product import add_product
from handles.cancel_product import cancel_product_coords
from handles.head_count import handle_head_count

import time

def punch_normal(dlg: any,
    prod: List[str],
    prod_parent: List[str],
    counts: List[int],
    tenders: List[str],
    amounts: Optional[List[int]] = None,
    disc: Optional[str] = None,
    isZeroRated=False,
    isInputCustInfo=False,
    isReturn=False,
    isCancelAll=False,
    pax: Optional[int] = None,
    dc_pax=1,
    cancel_prod: Optional[List[str]] = None,
    prod_addons:  Optional[List[str]] = None,
    qty_prod_addons:  Optional[List[int]] = None,
    additional_prod: Optional[List[str]] = None,
    additional_prod_parent: Optional[List[str]] = None,
    additional_count: Optional[List[str]] = None,
    additional_addons: Optional[List[str]] = None,
    spec_ins: Optional[List[str]] = None,
    parent_spec_ins: Optional[List[str]] = None,
    qty_spec_ins: Optional[List[int]] = None,
    meal_components: Optional[List[str]] = None,
    qty_meal_components: Optional[List[int]] = None,
    dito: Optional[List[int]] = None,
    open_memo: Optional[List[str]] = None,
    open_memo_prod: Optional[List[str]] = None,
    trantype:  str = None,
    **_extra_kwargs,
):  
    # Get transaction-specific config.
    # Config keys are often snake_case (e.g. dine_in, take_out) while UI labels
    # passed in can be upper case with spaces (e.g. "DINE IN").
    transaction = None
    if isinstance(trantype, str) and trantype.strip():
        transaction = getattr(config, trantype, None)
        if transaction is None:
            normalized = trantype.strip().lower().replace(" ", "_")
            transaction = getattr(config, normalized, None) or getattr(config, normalized.lower(), None)

    if transaction is None:
        print(f"No config found for action: {trantype}")
        return
    
    # Shared config values
    manager = config.manager_cred
    coords_check_btn = config.coords_check_btn

    # Normalize optional list parameters.
    # Avoids None errors when handlers expect lists.
    # Makes list with the same len as prod filled with None.
    if prod_addons is None:
        prod_addons = [None] * len(prod)
    if qty_prod_addons is None:
        qty_prod_addons = [None] * len(prod)
    if additional_addons is None:
        additional_addons = [None] * len(prod)
    if prod_addons is None:
        prod_addons = [None] * len(prod)
    if meal_components is None:
        meal_components = [None] * len(prod)
    if qty_meal_components is None:
        qty_meal_components = [None] * len(prod)
    dito_copy = dito
    if dito_copy is None:
        dito_copy = [None] * len(prod)
    
    # 
    initial_punch(dlg, prod, counts, prod_parent, prod_addons, qty_prod_addons, meal_components, qty_meal_components, spec_ins, parent_spec_ins, qty_spec_ins, dito_copy, open_memo, open_memo_prod)
    
    if isCancelAll:
        time.sleep(2)
        cancel_all(dlg, 'CANCEL\r\nORDER')
    
    if cancel_prod or additional_prod:
            if cancel_prod:
                cancel_product_coords(dlg, cancel_prod, False, manager.manager_id, manager.manager_pass)
            
            if additional_prod and additional_count and additional_prod_parent:
                add_product(dlg, additional_prod_parent, additional_prod, additional_count, additional_addons)

    if not isCancelAll:
        clickBtnCoords(dlg, coords_check_btn)
                
        if disc:
            customer_id = getattr(transaction, "customer_id", "")
            customer_name = getattr(transaction, "customer_name", "")
            address = getattr(transaction, "address", "")
            tin = getattr(transaction, "tin", "")
            bus_style = getattr(transaction, "bus_style", "")

            discount(
                dlg,
                manager.manager_id,
                manager.manager_pass,
                disc,
                customer_id,
                customer_name,
                address,
                tin,
                bus_style,
                20,
                dc_pax,
            )
        
        if(isZeroRated):
            zero_rated(dlg)
        
        if(isInputCustInfo):
            cust_info(dlg)
        
        if isReturn:
            return_to_product(dlg)
            
        # tender the amount
        tender_amount(dlg, amounts, tenders)
        # Prefer per-step pax override, otherwise fall back to per-transaction config, then default.
        head_count_value = pax if pax is not None else getattr(transaction, "head_count", 1)
        handle_head_count(dlg, head_count=head_count_value)

        if checkIfExistVisibleClickable(dlg, 'CASH') and not checkIfExist(dlg, 'VQP', control_type='Window'):
            print('Amount tendered not sufficient tender cash exact amount')
            clickTender(dlg, 'CASH')
        
        # Prevent infinite waits if tendering fails and "TOTAL DUE" never clears.
        # Default behavior is preserved for other transactions unless they opt-in via config.
        total_due_timeout_s = getattr(transaction, "total_due_timeout_s", None)
        if trantype == "FOOD_DINEIN" and total_due_timeout_s is None:
            total_due_timeout_s = 30

        total_due_start = time.time()
        while checkIfExist(dlg, 'TOTAL DUE:', control_type="Text"):
            wait_time = 1
            re_route(dlg)
            print("waiting makita yung server input uli")
            if checkIfExist(dlg, 'OK'):
                clickBtn(dlg, 'OK')
            if total_due_timeout_s is not None and (time.time() - total_due_start) > float(total_due_timeout_s):
                print(f"[TOTAL_DUE] Timeout after {total_due_timeout_s}s for trantype={trantype}. Stopping wait loop.")
                break
            time.sleep(wait_time)
