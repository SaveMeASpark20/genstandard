from typing import List, Optional
from function.clickButton import clickBtn
from function.clickButton import clickKeypad
from function.clickDisc import clickDiscount
from function.clickButton import doubleClickDateArrow
from function.util import checkIfExist
from function.util import generate_random_number
from function.input import inputText
from function.clickButton import clickBlkRecallBtn
from configuration.config import config
from pywinauto.keyboard import send_keys
from handles.initial_punch import initial_punch
from function.util import checkIfExistVisibleClickable
from handles.tender_amount import tender_amount
from handles.re_route import re_route
from handles.depo_cust_info import depo_cust_info
from tender.clickTender import clickTender
from handles.cancel_product import cancel_product
from handles.add_product import add_product
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
    bulk = config.bulk_transact
    manager = config.manager_cred

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
    clickKeypad(dlg, "check")
 
    #click deposits and input cust info
    depo_cust_info(dlg)

    if disc:
        clickDiscount(dlg, disc, bulk.customer_id, bulk.customer_name, bulk.address, bulk.tin, bulk.bus_style, promo_amount=20)

    if deposits:
        tender_amount(dlg, deposits, tenders)
    else:
        tender_amount(dlg, amounts, tenders)
    
    if checkIfExist(dlg, 'More Deposits?', control_type="Text"):
        clickBtn(dlg,'No')


    # re_route(dlg)

    # if checkIfExistVisibleClickable(dlg, 'CASH') and not checkIfExist(dlg, 'VQP', control_type='Window'):
    #     print('Amount tendered not sufficient tender cash exact amount')
    #     clickTender(dlg, 'CASH')
    
    # while not checkIfExist(dlg, 'Trans#', control_type="HeaderItem"):
    #     wait_time = 1
    #     re_route(dlg)
    #     print("waiting makita yung server input uli")
    #     if checkIfExist(dlg, 'OK'):
    #         clickBtn(dlg, 'OK')
    #     time.sleep(wait_time)  

    clickBtn(dlg, 'RECALL', secondsToSleep=5)
    clickBlkRecallBtn(dlg, 'check')
    clickKeypad(dlg, 'check')

    if cancel_prod or additional_prod:   
        clickBtn(dlg, 'RECALL', secondsToSleep=5)
        clickBlkRecallBtn(dlg, 'check')
        clickKeypad(dlg, 'check')

        if cancel_prod:
            cancel_product(dlg, cancel_prod, isFinalPayment, manager.manager_id, manager.manager_pass)
        
        if additional_prod and additional_count and additional_prod_parent:
            add_product(dlg, additional_prod_parent, additional_prod, additional_count, additional_addons)

        if additional_dep :
            tender_amount(dlg, additional_dep, tenders)
        else :
            tender_amount(dlg, amounts, tenders)

        if checkIfExist(dlg, 'More Deposits?', control_type="Text"):
            clickBtn(dlg,'No')
        
        #re_route(dlg)
            
        # # para sure na fully tender talaga
        # if checkIfExistVisibleClickable(dlg, 'CASH') and not checkIfExist(dlg, 'VQP', control_type='Window'):
        #     print('Amount tendered not sufficient tender cash exact amount')
        #     clickTender(dlg, 'CASH')
        
        # while not checkIfExist(dlg, 'Trans#', control_type="HeaderItem"):
        #     wait_time = 1
        #     re_route(dlg)
        #     print("waiting makita yung server input uli")
        #     if checkIfExist(dlg, 'OK'):
        #         clickBtn(dlg, 'OK')
        #     time.sleep(wait_time)
    
    clickBtn(dlg, 'RECALL', secondsToSleep=5)

    clickBlkRecallBtn(dlg, 'check')
    clickKeypad(dlg, 'check')
    clickBtn(dlg, 'FINAL\r\nPAYMENT')
    clickBtn(dlg, 'CASH')
    clickBtn(dlg, 'OK')
    if(checkIfExist(dlg,'RE-ROUTE')) :
        clickBtn(dlg, 'RE-ROUTE')
        clickBtn(dlg, 'P O S')

