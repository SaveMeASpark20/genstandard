from typing import List, Optional
from function.clickButton import clickBtn
from function.clickButton import clickKeypad
from function.util import checkIfExist
from function.util import checkIfExistVisibleClickable
from function.util import checkIfExistEscapeSpecChars
from function.clickButton import clickNonBtn
from tender.clickTender import clickTender
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

def punch(dlg: any,
    prod: List[str],
    prod_parent : List[str],
    counts: List[int],
    tenders: List[str],
    amounts: Optional[List[str]] = None,
    disc: Optional[str] = None,
    tender_disc: Optional[str] = None,
    isFinalPayment = False,
    isZeroRated = False,
    isInputCustInfo = False,
    is_split_table = False,
    is_print_bill = False,
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
    
    dine_in = config.dine_in
    cashier = config.cashier_cred
    manager = config.manager_cred

    cashier_sign_setup_table(dlg, cashier.cashier_id, dine_in.table, pax)

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
    if spec_ins is None:
        spec_ins = [None] * len(prod)
    if parent_spec_ins is None:
        parent_spec_ins = [None] * len(prod)
    if qty_spec_ins is None:
        qty_spec_ins = [None] * len(prod)
    if dito is None:
        dito = [None] * len(prod)
        
   
    initial_punch(dlg, prod, counts, prod_parent, prod_addons, qty_prod_addons, meal_components, qty_meal_components, spec_ins, parent_spec_ins, qty_spec_ins, dito, open_memo, open_memo_prod)

    clickKeypad(dlg, 'check') #after punching check to go to tender section
    
    if split_bill_pax:
        split_bill(dlg, split_bill_pax, pax)

    if is_print_bill:
        if split_bill_pax:
            split_bill(dlg, split_bill_pax, pax)
        clickBtn(dlg, 'PRINT\r\nBILL')

    if isFinalPayment==False :
        store_order(dlg, cashier.cashier_id, dine_in.table)
        
    if transfers:
        transfer(dlg, transfers)

    if cancel_prod :   
        cancel_product(dlg, cancel_prod, isFinalPayment, manager.manager_id, manager.manager_pass)
    
    if additional_prod and additional_count and additional_prod_parent:
        add_product(dlg, additional_prod_parent, additional_prod, additional_count, additional_addons)

    if moveTo and paxMoveTo and mark_prods:
        move_prod_other_table(dlg, mark_prods, moveTo, pax, cashier.cashier_id)

    if changePax:
        change_pax(dlg, changePax)
    
    if is_split_table:
       split_table(dlg, mark_prods, cashier.cashier_id, dine_in.table)

    if(isFinalPayment==False):
        clickKeypad(dlg, 'check')

    if tender_disc :
        discount(dlg,manager.manager_id, manager.manager_pass, tender_disc, dine_in.customer_id, dine_in.customer_name, dine_in.address, dine_in.tin, dine_in.bus_style, 20, dc_pax)

    
    if split_bill_pax:
        split_bill(dlg, split_bill_pax, pax)

    clickBtn(dlg, 'FINAL\r\nPAYMENT')

    if(isZeroRated):
        zero_rated(dlg)
        
    if(isInputCustInfo):
        cust_info(dlg)

    if(disc):
        discount(dlg,manager.manager_id, manager.manager_pass, disc, dine_in.customer_id, dine_in.customer_name, dine_in.address, dine_in.tin, dine_in.bus_style, 20, dc_pax)
        
    tender_amount(dlg, amounts, tenders)

    # para sure na fully tender talaga
    if checkIfExistVisibleClickable(dlg, 'CASH') and not checkIfExist(dlg, 'VQP', control_type='Window'):
        print('Amount tendered not sufficient tender cash exact amount')
        clickTender(dlg, 'CASH')
    
    #kapag  maglalabas ng OK to print acc copy
    while(checkIfExist(dlg, 'OK')):
        clickBtn(dlg, 'OK')



    