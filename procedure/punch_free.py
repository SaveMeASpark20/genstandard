from typing import List, Optional
from function.clickButton import clickBtn
from function.util import checkIfExist
from handles.tender_free import tender_free
from handles.initial_punch import initial_punch

from configuration.config import config
from handles.re_route import re_route
from handles.return_to_product import return_to_product
from handles.cancel_all import cancel_all
from function.clickButton import clickBtnCoords
from handles.add_product import add_product
from handles.cancel_product import cancel_product_coords

import time

def punch_free(dlg: any,
    prod: List[str],
    prod_parent : List[str],
    counts: List[int],
    tenders: str,

    isReturn=False,
    isCancelAll=False,
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
    
    free = config.free
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
    
    if checkIfExist(dlg, 'FREE'):
        clickBtn(dlg, 'FREE')

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
                
        if isReturn:
            return_to_product(dlg)

        tender_free(dlg, free_btn=tenders)

        re_route(dlg)

        


        

        