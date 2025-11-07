from typing import List, Optional
from function.clickButton import clickBtn
from function.util import checkIfExist
from function.util import checkIfExistVisibleClickable
from tender.clickTender import clickTender
from handles.initial_punch import initial_punch
from handles.cancel_product import cancel_product
from handles.add_product import add_product
from handles.zero_rated import zero_rated
from handles.cust_info import cust_info
from handles.discount import discount
from handles.tender_amount import tender_amount
from configuration.config import config
from pywinauto.keyboard import send_keys
from handles.re_route import re_route
from handles.return_to_product import return_to_product
from handles.cancel_all import cancel_all
import time
from datetime import datetime
from function.clickButton import clickDeliveryBtn
from function.input import inputText_Re
from sequence.del_cust_info import del_cust_info
from function.clickButton import clickBtnCoords


def punch_delivery(dlg: any,
    prod: List[str],
    prod_parent : List[str],
    counts: List[int],
    tenders: List[str],
    amounts: Optional[List[int]] = None,
    disc: Optional[str] = None,
    isFinalPayment = False,
    isZeroRated = False,
    isInputCustInfo = False,
    isReturn=False,
    isCancelAll=False,
    dc_pax=1,
    cancel_prod: Optional[List[str]] = None,
    prod_addons :  Optional[List[str]] = None ,
    qty_prod_addons :  Optional[List[int]] = None ,
    additional_prod: Optional[List[str]] = None,
    additional_prod_parent : Optional[List[str]] = None ,
    additional_count : Optional[List[str]] = None ,
    additional_addons : Optional[List[str]] = None,
    spec_ins : Optional[List[str]] = None,
    parent_spec_ins : Optional[List[str]] = None ,
    qty_spec_ins : Optional[List[int]] = None ,
    meal_components : Optional[List[str]] = None ,
    qty_meal_components : Optional[List[int]] = None,
    dito : Optional[List[int]] = None,
    open_memo : Optional[List[str]] = None,
    open_memo_prod : Optional[List[str]] = None
):  
    
    delivery = config.delivery
    manager = config.manager_cred
    coords_check_btn = config.coords_check_btn


    if prod_addons is None:
        prod_addons = [None] * len(prod)
    if qty_prod_addons is None:
        qty_prod_addons = [None] * len(prod)
    if additional_addons is None:
        additional_addons = [None] * len(prod)
    if prod_addons is None:
        prod_addons = [None] * len(prod)
    if meal_components is None:
        meal_components = [None] *  len(prod)
    if qty_meal_components is None:
        qty_meal_components = [None] * len(prod)
    dito_copy = dito
    if dito_copy is None:
        dito_copy = [None] * len(prod)
    
    clickDeliveryBtn(dlg, "new")
    del_cust_info(dlg)

    initial_punch(dlg, prod, counts, prod_parent, prod_addons, qty_prod_addons, meal_components, qty_meal_components, spec_ins, parent_spec_ins, qty_spec_ins, dito_copy, open_memo, open_memo_prod)
    
    if isCancelAll:
        time.sleep(2)
        cancel_all(dlg, 'CANCEL\r\nORDER')

    if not isCancelAll:
        clickBtnCoords(dlg, coords_check_btn)

        if isReturn:
            return_to_product(dlg)
                
        if disc:
            discount(dlg, manager.manager_id, manager.manager_pass, disc, delivery.customer_id, delivery.customer_name, delivery.address, delivery.tin, delivery.bus_style, 20, dc_pax)
        
        if(isZeroRated):
            zero_rated(dlg)
                
        if(isInputCustInfo):
            cust_info(dlg)
        
        #tender the amount
        tender_amount(dlg, amounts, tenders)
        re_route(dlg)

        if checkIfExistVisibleClickable(dlg, 'CASH') and not checkIfExist(dlg, 'VQP', control_type='Window'):
            print('Amount tendered not sufficient tender cash exact amount')
            clickTender(dlg, 'CASH')
        
        while not checkIfExist(dlg, 'Trans#', control_type="HeaderItem"):
            wait_time = 1
            re_route(dlg)
            print("waiting makita yung server input uli")
            if checkIfExist(dlg, 'OK'):
                clickBtn(dlg, 'OK')
            time.sleep(wait_time)

        if cancel_prod or additional_prod:   
            clickDeliveryBtn(dlg, "check")
            if cancel_prod:
                cancel_product(dlg, cancel_prod, isFinalPayment, manager.manager_id, manager.manager_pass)
            
            if additional_prod and additional_count and additional_prod_parent:
                add_product(dlg, additional_prod_parent, additional_prod, additional_count, additional_addons)

            tender_amount(dlg, amounts, tenders)

            re_route(dlg)
            # para sure na fully tender talaga

            if checkIfExistVisibleClickable(dlg, 'CASH') and not checkIfExist(dlg, 'VQP', control_type='Window'):
                print('Amount tendered not sufficient tender cash exact amount')
                clickTender(dlg, 'CASH')
            
            while not checkIfExist(dlg, 'Trans#', control_type="HeaderItem"):
                wait_time = 1
                re_route(dlg)
                print("waiting makita yung server input uli")
                if checkIfExist(dlg, 'OK'):
                    clickBtn(dlg, 'OK')
                time.sleep(wait_time)

        clickDeliveryBtn(dlg, "driver")
        inputText_Re(dlg, delivery.rider_id, "Rider")
        send_keys("{ENTER}")
        clickDeliveryBtn(dlg, "check")

        now = datetime.now()
        seconds_to_wait = 60 - now.second  # Calculate seconds until next minute

        print(f"Current Time: {now.strftime('%H:%M:%S')}")
        time.sleep(seconds_to_wait)  # Sleep until next minute

        updated_time = datetime.now().strftime("%H:%M")
        print(f"New Time: {updated_time}")
        inputTime =updated_time.replace(":", "")
        print(f"Update new Time: {inputTime}")
        inputText_Re(dlg, inputTime, 'RcvTime')
        send_keys("{ENTER}")
        send_keys("{ENTER}")
        tender_amount(dlg, amounts, tenders)

        # para sure na fully tender talaga
        if checkIfExistVisibleClickable(dlg, 'CASH') and not checkIfExist(dlg, 'VQP', control_type='Window'):
            print('Amount tendered not sufficient tender cash exact amount')
            clickTender(dlg, 'CASH')
        
        #kapag  maglalabas ng OK to print acc copy and reroute
        while not checkIfExist(dlg, 'Trans#', control_type="HeaderItem"):
            wait_time = 1
            re_route(dlg)
            print("waiting makita yung server input uli")
            if checkIfExist(dlg, 'OK'):
                clickBtn(dlg, 'OK')
            time.sleep(wait_time)


        

        