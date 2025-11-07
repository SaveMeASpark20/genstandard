from typing import List, Optional
from function.clickButton import clickBtn
from function.clickButton import clickKeypad
from function.clickButton import clickBtnCoords
from function.util import checkIfExist
from function.util import checkIfExistVisibleClickable
from function.util import checkIfExistEscapeSpecChars
from function.clickButton import clickNonBtn
from tender.clickTender import clickTender
from function.input import inputText_Re
from function.input import inputText
from handles.cashier_sign_setup_table import cashier_sign_setup_table
from handles.initial_punch import initial_punch
from handles.store_order import store_order
from handles.transfer import transfer
from handles.cancel_product import cancel_product
from handles.add_product import add_product
from handles.zero_rated import zero_rated
from handles.cust_info import cust_info
from handles.discount import discount
from handles.tender_amount import tender_amount
from handles.move_prod_other_table import move_prod_other_table
from handles.change_pax import change_pax
from handles.split_table import split_table
from configuration.config import config
from pywinauto.keyboard import send_keys
from handles.split_bill import split_bill
from sequence.backMgrMenu import clickBckMgrMenu
from handles.re_route import re_route
from handles.return_to_product import return_to_product
from handles.first_table_final import first_table_final
from handles.cancel_all import cancel_all
from sequence.managerSignon import managerSignon

import time

def punch_takeout_OTK(dlg1: any, dlg2: any,
    prod: List[str],
    prod_parent : List[str],
    counts: List[int],
    tenders: List[str],
    amounts: Optional[List[int]] = None,
    disc: Optional[str] = None,
    tender_disc: Optional[str] = None,
    isFinalPayment = False,
    isZeroRated = False,
    isInputCustInfo = False,
    is_split_table = False,
    is_print_bill = False,
    isFinalPaymentReturn = False,
    isReturn=False,
    isCancelAll=False,
    pax=1,
    dc_pax=1,
    changePax=None,
    moveTo : Optional[str] = None,
    paxMoveTo : Optional[int] = None,
    mark_prods : Optional[List[str]] = None,
    split_bill_pax : Optional[int] = None,
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
    transfers : Optional[List[str]] = None,
    open_memo : Optional[List[str]] = None,
    open_memo_prod : Optional[List[str]] = None
):  
    dlg = dlg1
    dlg2 = dlg2
    
    takeout = config.take_out
    takeout_OTK = config.take_out_OTK
    cashier = config.cashier_cred
    manager = config.manager_cred
    bachus_mainmenu_btn = config.bacchus_mainmenu_btn
    coords_check_btn = config.coords_check_btn


    if checkIfExist(dlg2, 'TAKE OUT'):
        clickBtn(dlg2, 'TAKE OUT')


    cashier_sign_setup_table(dlg2, cashier.cashier_id, takeout_OTK.table, pax)

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
    # if spec_ins is None:
    #     spec_ins = [None] * len(prod)
    # if parent_spec_ins is None:
    #     parent_spec_ins = [None] * len(prod)
    # if qty_spec_ins is None:
    #     qty_spec_ins = [None] * len(prod)
    dito_copy = dito
    if dito_copy is None:
        dito_copy = [None] * len(prod)
        
   
    initial_punch(dlg2, prod, counts, prod_parent, prod_addons, qty_prod_addons, meal_components, qty_meal_components, spec_ins, parent_spec_ins, qty_spec_ins, dito_copy, open_memo, open_memo_prod)

    # if split_bill_pax:
    #     split_bill(dlg2, split_bill_pax, pax)
        
    # clickKeypad(dlg2, 'check') #after punching check to go to tender section
    clickBtnCoords(dlg, coords_check_btn) #after punching check to go to tender section

    if not isFinalPayment:
        store_order(dlg2, cashier.cashier_id, takeout_OTK.table)

        if isCancelAll:
            cancel_all(dlg2, 'CANCEL\r\nORDER')

    if not isCancelAll:
        print("papasok ba sya dito kapag hinanap yung final payment")
        time.sleep(2)
        if dito :
            if (checkIfExist(dlg2, "VQP", control_type="Window")):
                print('Transaction Type (DINE IN) Does Not Match! is exist')
                clickBtn(dlg2, 'OK')
                clickBckMgrMenu(dlg2, bachus_mainmenu_btn)
                clickBtn(dlg2, 'DINE IN')
                cashier_sign_setup_table(dlg2, cashier.cashier_id, takeout.table)

        if transfers:
            transfer(dlg2, transfers, 'Text')

        if cancel_prod :   
            cancel_product(dlg2, cancel_prod, isFinalPayment, manager.manager_id, manager.manager_pass)
        
        if additional_prod and additional_count and additional_prod_parent:
            add_product(dlg2, additional_prod_parent, additional_prod, additional_count, additional_addons)

        if moveTo and paxMoveTo and mark_prods:
            move_prod_other_table(dlg2, mark_prods, moveTo, pax, cashier.cashier_id)
            dlg.set_focus()
            first_table_final(dlg, cashier_id=cashier.cashier_id, table=takeout.table, amounts=amounts, tenders=tenders)
            re_route(dlg)

            dlg2.set_focus()
            cashier_sign_setup_table(dlg2, cashier.cashier_id, table=moveTo)
        if changePax:
            change_pax(dlg2, changePax)
        
        if is_split_table:
            split_table(dlg2, mark_prods, table=takeout_OTK.table, cashier_id=cashier.cashier_id)
            dlg.set_focus()
            first_table_final(dlg, cashier_id=cashier.cashier_id, table=takeout.table, amounts=amounts, tenders=tenders, is_split_table=is_split_table)
            re_route(dlg)

            dlg2.set_focus()
            cashier_sign_setup_table(dlg2, cashier.cashier_id, table= takeout_OTK.table)

        clickKeypad(dlg2, 'check') 

        if tender_disc :
            discount(dlg2, manager.manager_id, manager.manager_pass, tender_disc, takeout.customer_id, takeout.customer_name, takeout.address, takeout.tin, takeout.bus_style, 20, dc_pax)

        if isReturn:
            return_to_product(dlg2)

        if split_bill_pax:
            split_bill(dlg2, split_bill_pax, pax)

        if is_print_bill:
            # if split_bill_pax:
            #     split_bill(dlg2, split_bill_pax, pax)
            
            clickBtn(dlg2, 'PRINT\r\nBILL')

            inputText_Re(dlg2, cashier.cashier_id, "Server?")
            send_keys("{ENTER}")
            if moveTo:
                clickBtn(dlg2, moveTo)
            else:
                clickBtn(dlg2, takeout_OTK.table)

            if checkIfExist(dlg2, "Bill Already Printed!", control_type='Text') or checkIfExist(dlg2, "VQP", control_type='Window'):
                print(f"Bill Already Printed Click OK")
                clickBtn(dlg2, 'OK')

        clickBckMgrMenu(dlg2, 'MAIN MENU')

        dlg.set_focus()

        if checkIfExist(dlg, 'TAKE OUT'):
            clickBtn(dlg, 'TAKE OUT')
        if(checkIfExist(dlg, 'Invalid Code!', control_type='Text')):
            clickBtn(dlg, 'OK')
        
        if dito or transfers:
            inputText(dlg, cashier.cashier_id, 'Server?')
            send_keys("{ENTER}")
            clickBckMgrMenu(dlg, bachus_mainmenu_btn)
            clickBtn(dlg, 'DINE IN')
        
        if moveTo:
            cashier_sign_setup_table(dlg, cashier.cashier_id, table=moveTo)
        else:
            cashier_sign_setup_table(dlg, cashier.cashier_id, table=takeout.table)

        if not isCancelAll:

            if not isFinalPayment :
                clickKeypad(dlg, 'check')

            if split_bill_pax:
                # clickKeypad(dlg, 'check')
                split_bill(dlg, split_bill_pax, pax)

            clickBtn(dlg, 'FINAL\r\nPAYMENT')

            if(isZeroRated):
                zero_rated(dlg)
                
            if(isInputCustInfo):
                cust_info(dlg)

            if(disc):
                discount(dlg,manager.manager_id, manager.manager_pass, disc, takeout.customer_id, takeout.customer_name, takeout.address, takeout.tin, takeout.bus_style, 20, dc_pax)

            if isFinalPaymentReturn: # return to cancel out the discount go back to product menu
                return_to_product(dlg, isFinalPaymentReturn=True)

            tender_amount(dlg, amounts, tenders)

            #check kung may reroute
            re_route(dlg)
            if checkIfExistVisibleClickable(dlg, 'CASH') and not checkIfExist(dlg, 'VQP', control_type='Window'):
                print('Amount tendered not sufficient tender cash exact amount')
                clickTender(dlg, 'CASH')

            while not checkIfExist(dlg, 'Server?', control_type="Edit"):
                wait_time = 1
                print("waiting makita yung server input uli")
                re_route(dlg)
                if checkIfExist(dlg, 'OK'):
                    clickBtn(dlg, 'OK')
                time.sleep(wait_time)
            
            #this is for di/to function to go back to TAKE OUT transaction
            if dito or transfers:
                inputText(dlg, cashier.cashier_id, 'Server?')
                send_keys("{ENTER}")
                clickBckMgrMenu(dlg, bachus_mainmenu_btn)
                clickBtn(dlg, 'TAKE OUT')



        