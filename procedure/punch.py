from typing import List, Optional
from function.clickButton import clickBtn
from function.clickButton import clickNonBtn
from function.clickButton import clickKeypad
from configuration.config import config
from function.util import checkIfExist
from function.util import checkIfExistWithTitleRe
from pywinauto.keyboard import send_keys
from function.input import inputText
from function.clickDisc import clickDiscount
from tender.clickTender import clickTender
from function.clickZeroRated import clickZeroRated
from function.clickCustInfo import clickCustInfo


def punch(dlg: any,
    prod: List[str],
    prod_parent : List[str],
    counts: List[int],
    tenders: List[str],
    amounts: Optional[List[str]] = None,
    disc: Optional[str] = None,
    isFinalPayment= False,
    isZeroRated= False,
    isInputCustInfo = False,
    pax=1,
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
    transfers : Optional[List[str]] = None

):  
    dine_in = config.dine_in
    cashier = config.cashier_cred
    manager = config.manager_cred

    inputText(dlg, cashier.cashier_id, 'Server')
    send_keys("{ENTER}")
    clickBtn(dlg, dine_in.table)
    inputText(dlg, pax, "PAX")
    send_keys("{ENTER}")
    
    last_parent = prod_parent[0]

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
        
    for index, (product, qty, parent, qpa, add_on, mc, qmc, si, psi, qsi, dt) in enumerate(zip(prod, counts, prod_parent, qty_prod_addons, prod_addons, meal_components, qty_meal_components, spec_ins, parent_spec_ins, qty_spec_ins, dito )):

        print("product :", product, " qty :", qty, "parent :", parent, "qpa: ", qpa, "add_on :", add_on, "mc :", mc, "qmc :", qmc, "si : ", si, "psi: ",psi, "qsi: ", qsi, " dt: ", dt)
        if qty and product and parent:
             #add functionality for DI/TO
            if dt == 1:
                clickBtn(dlg, 'DI/TO')
                clickBtn(dlg, 'OK')

            if parent == last_parent:
                if(index == 0):
                    clickBtn(dlg, parent)
                
            else :
                clickBtn(dlg, 'RETURN')
                clickBtn(dlg, parent)
                last_parent = parent

            for _ in range(qty):
                clickBtn(dlg, product)
                if qmc and mc:
                    if not isinstance(mc, list):
                        mc = [mc]
                    
                    if not isinstance(qmc, list):
                        qmc = [qmc]


                    for meal_comp, qty in zip(mc, qmc):
                        for _ in range(qty):
                            clickBtn(dlg, meal_comp)
                        
                if add_on and qpa :
                    if not isinstance(add_on, list):
                        add_on = [add_on]
                    
                    if not isinstance(qpa, list):
                        qpa = [qpa]

                    for qty, add in zip(qpa, add_on) :
                        for _ in range(qty) :
                            if add == 'CHECK' or add == 'SKIP':
                                clickKeypad(dlg, "check")
                            else: 
                                clickBtn(dlg, add)
                            
                if psi and si:
                    # clean_item = psi.replace("\r\n", " ")
                    # clickNonBtn(dlg, clean_item, control_type='Text')
                    clickBtn(dlg, "SPCL\r\nINSTRUCTN")
                    for _ in range(qsi):
                        clickBtn(dlg, si)
                
                    clickKeypad(dlg, "check")

    clickKeypad(dlg, 'check')
    
    if(isFinalPayment==False):
        clickBtn(dlg, 'STORE\r\nORDER')

        if(checkIfExist(dlg,'Re-route')):
            clickBtn(dlg, 'Re-route')
            clickBtn(dlg, 'P O S')
        
        if(checkIfExist(dlg,'RE-ROUTE')):
            clickBtn(dlg, 'RE-ROUTE')
            clickBtn(dlg, 'P O S')

        inputText(dlg, cashier.cashier_id, "Server")
        send_keys("{ENTER}")

        clickBtn(dlg, dine_in.table)

        if transfers:
            for transfer in transfers:
                clickNonBtn(dlg, transfer, control_type='Text')
                clickBtn(dlg, 'TRANSFER')

    if(cancel_prod) :   
        for product in cancel_prod:
            if(product and isFinalPayment==False):
                clean_item = product.replace("\r\n", " ")
                clickNonBtn(dlg, clean_item, control_type='Text')
                clickKeypad(dlg, 'x')
                inputText(dlg, manager.manager_id, "Manager")
                send_keys("{TAB}")
                inputText(dlg, manager.manager_pass, "Password")
                send_keys("{ENTER}")
                clickBtn(dlg, 'YES')
    
    if additional_prod and additional_count and additional_prod_parent:
        additional_last_parent = additional_prod_parent[0]
        if additional_addons is None:
            additional_addons = [None] 

        if len(additional_addons) != len(additional_prod):
            raise ValueError("additional_addons must be the same length as prod")
        for index,(product, qty, parent, add_on) in enumerate(zip(additional_prod, additional_count, additional_prod_parent, additional_addons)):
            if qty and product and parent:
                if parent == additional_last_parent:
                    if(index == 0):
                        clickBtn(dlg, parent)
                else :
                    clickBtn(dlg, 'RETURN')
                    clickBtn(dlg, parent)
                    last_parent = parent

                for _ in range(qty):
                    clickBtn(dlg, product)
                    if add_on and (add_on == 'CHECK' or add_on == 'SKIP'):
                        clickKeypad(dlg, "check")
                    elif add_on:    
                        clickBtn(dlg, add_on)

    if(isFinalPayment==False):
        clickKeypad(dlg, 'check')
       
    clickBtn(dlg, 'FINAL\r\nPAYMENT')

    if(isZeroRated):
        clickBtn(dlg, 'ZERO\r\nRATED')
        clickZeroRated(dlg)
    
    if(isInputCustInfo):
        clickBtn(dlg, 'CUSTOMER\r\nINFO')
        clickCustInfo(dlg)
    if(disc):
        clickBtn(dlg, 'DISC')
        inputText(dlg, manager.manager_id, "Manager")
        send_keys("{TAB}")
        inputText(dlg, manager.manager_pass, "Password")
        send_keys("{ENTER}")
        clickDiscount(dlg, disc, dine_in.customer_id, dine_in.customer_name, dine_in.address, dine_in.tin, dine_in.bus_style, 20, dc_pax )
    
    if(amounts):
        for tender, amount in zip(tenders, amounts):
            if(tender and amount):
                clickTender(dlg, tender) #add the amount
            else:
                clickTender(dlg, tender)
    else :
        for tender in tenders:
            clickTender(dlg, tender)
    
    while(checkIfExist(dlg, 'OK')):
        clickBtn(dlg, 'OK')


