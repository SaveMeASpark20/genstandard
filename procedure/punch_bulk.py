from typing import List, Optional
from function.clickButton import clickBtn
from function.clickButton import clickBtnCoords
from function.clickButton import clickKeypad
from handles.cust_info import cust_info
from function.util import checkIfExist
from function.clickButton import clickBlkRecallBtn
from configuration.config import config
from handles.initial_punch import initial_punch
from handles.tender_amount import tender_amount
from handles.depo_cust_info import depo_cust_info
from handles.depo_cust_info import depo_cust_noinfo
from handles.cancel_product import cancel_product
from handles.add_product import add_product
from handles.discount import discount
import time


def punch_bulk(dlg: any,
    prod: List[str],
    prod_parent : List[str],
    counts: List[int],
    tenders: List[str],
    deposits: Optional[List[int]] = None,
    additional_dep: Optional[List[int]] = None,
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
    bulk = config.bulk
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

    initial_punch(dlg, prod, counts, prod_parent, prod_addons, qty_prod_addons, meal_components, qty_meal_components, spec_ins, parent_spec_ins, qty_spec_ins, dito_copy, open_memo, open_memo_prod)

    #go to tender
    time.sleep(2) #KAPAG GALING SA ADD ONS HINDI sya gumagana yung check hahahaha
    clickBtnCoords(dlg, coords_check_btn)
 
    #click deposits and input cust info
    depo_cust_info(dlg)

    # if disc:
    #     discount(dlg, disc, bulk.customer_id, bulk.customer_name, bulk.address, bulk.tin, bulk.bus_style, promo_amount=20)

    if disc:
        discount(dlg, manager.manager_id, manager.manager_pass, disc, bulk.customer_id, bulk.customer_name, bulk.address, bulk.tin, bulk.bus_style, 20, dc_pax)

    if deposits:
        tender_amount(dlg, deposits, tenders)
    else:
        tender_amount(dlg, amounts, tenders)
    
    if checkIfExist(dlg, 'More Deposits?', control_type="Text"):
        clickBtn(dlg,'NO')
    
    while checkIfExist(dlg, 'CASH', control_type="Button"):
        wait_time = 1
        print("checking if CASH is still visible means there's a prompt")
        if checkIfExist(dlg, 'OK'):
            clickBtn(dlg, 'OK')
        time.sleep(wait_time) 


    if cancel_prod or additional_prod or additional_dep:   
        print("cancel order:", cancel_prod, "additional prod:", additional_prod)
        clickBtn(dlg, 'RECALL', secondsToSleep=5)
        clickBlkRecallBtn(dlg, 'check')

        if cancel_prod:
            cancel_product(dlg, cancel_prod, isFinalPayment, manager.manager_id, manager.manager_pass)
        
        if additional_prod and additional_count and additional_prod_parent:
            add_product(dlg, additional_prod_parent, additional_prod, additional_count, additional_addons)

        clickKeypad(dlg, 'check')
        depo_cust_noinfo(dlg)
            
        if additional_dep :
            tender_amount(dlg, additional_dep, tenders) #di pa supported yung mga maraming tender. mahirap eh
        else :
            tender_amount(dlg, amounts, tenders) #di pa supported yung mga maraming tender. mahirap eh

        if checkIfExist(dlg, 'More Deposits?', control_type="Text"):
            clickBtn(dlg,'NO')
        
        while checkIfExist(dlg, 'CASH', control_type="Button"):
            wait_time = 1
            print("checking if CASH is still visible means there's a prompt")
            if checkIfExist(dlg, 'OK'):
                clickBtn(dlg, 'OK')
            time.sleep(wait_time) 
        
    
    clickBtn(dlg, 'RECALL', secondsToSleep=5)

    clickBlkRecallBtn(dlg, 'check')
    clickKeypad(dlg, 'check')
        
    clickBtn(dlg, 'FINAL\r\nPAYMENT')
    if isInputCustInfo:
        cust_info(dlg)
    clickBtn(dlg, 'CASH')
    if checkIfExist(dlg, 'CASH Info', control_type='Group'):
        clickKeypad(dlg, "exact amount")

    while checkIfExist(dlg, 'CASH', control_type="Button"):
        wait_time = 1
        print("checking if CASH is still visible means there's a prompt")
        if checkIfExist(dlg, 'OK'):
            clickBtn(dlg, 'OK')
        time.sleep(wait_time) 

