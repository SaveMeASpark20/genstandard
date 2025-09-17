from function.clickButton import clickBtn
from function.clickButton import clickKeypad
from function.clickDisc import clickDiscount
from function.clickButton import clickDeliveryBtn
from function.clickButton import doubleClickDateArrow
from function.util import checkIfExist
from function.util import generate_random_number
from function.input import inputText_Re
from function.input import inputTextByIndex
from function.clickButton import clickBlkRecallBtn
from configuration.config import config
from datetime import datetime
from pywinauto.keyboard import send_keys
import time
import random

def dineIn(dlg, transaction_type = "DINE IN",  ):
    restaurant_type = config.restaurant_type
    if(restaurant_type == 'FINE DINING'):
        bacchusDineIn(dlg)
    elif(restaurant_type == 'FASTFOOD'):
        foodDineIn(dlg)
    else :
        print('Neither Fine Dining or FastFood')

def takeOut(dlg, transaction_type = "TAKE OUT", ):
    restaurant_type = config.restaurant_type
    if(restaurant_type == 'FINE DINING'):
        bacchusTakeOut(dlg)
    elif(restaurant_type == 'FASTFOOD'):
        foodTakeOut(dlg)
    else :
        print('Neither Fine Dining or Fast Food')


def delivery(dlg, transaction_type ="DELIVERY") :
    delivery = config.delivery_transact
    clickBtn(dlg, transaction_type)
    for disc in delivery.disc :
        print(disc)
        clickDeliveryBtn(dlg, "new") #new 
        inputText_Re(dlg, delivery.phone, "Phone")
        send_keys("{TAB}")
        inputText_Re(dlg, delivery.loc, "Loc/Ext")
        send_keys("{TAB}")
        inputText_Re(dlg, delivery.name, "Name")
        send_keys("{TAB}")
        inputText_Re(dlg, delivery.address, "Address")
        send_keys("{TAB}")
        inputTextByIndex(dlg, delivery.address2, 4)
        send_keys("{TAB}")
        inputText_Re(dlg, delivery.grid, "Grid/Area")
        send_keys("{TAB}")
        inputText_Re(dlg, delivery.comment, "Comment")
        send_keys("{TAB}")
        inputText_Re(dlg, delivery.note, "Note")
        send_keys("{ENTER}")
        clickBtn(dlg, delivery.prod_group)
        clickBtn(dlg, delivery.product)
        clickKeypad(dlg, "check")
        clickBtn(dlg, "DISC")
        inputText_Re(dlg, delivery.manager_id, "Manager")
        send_keys("{TAB}")
        inputText_Re(dlg, delivery.manager_pass, "Password")
        send_keys("{ENTER}")
        clickDiscount(dlg, disc, delivery.customer_id, delivery.customer_name, delivery.address, delivery.tin, delivery.bus_style)
        clickBtn(dlg, "CASH")
        clickKeypad(dlg, "exact amount")
        if(checkIfExist(dlg,'RE-ROUTE')) :
            clickBtn(dlg, 'RE-ROUTE')
            clickBtn(dlg, 'P O S')
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
        clickBtn(dlg, "CASH")
        clickKeypad(dlg, "exact amount")
        clickBtn(dlg, "OK")
        if(checkIfExist(dlg,'RE-ROUTE')) :
            clickBtn(dlg, 'RE-ROUTE')
            clickBtn(dlg, 'P O S')

def misc(dlg, transaction_type = "MISC", ):
    misc = config.transact
    clickBtn(dlg, transaction_type)
    for disc in misc.disc :
        clickBtn(dlg, misc.prod_group)
        clickBtn(dlg, misc.product)
        clickKeypad(dlg, "check")
        clickBtn(dlg, "DISC")
        inputText_Re(dlg, misc.manager_id, "Manager")
        send_keys("{TAB}")
        inputText_Re(dlg, misc.manager_pass, "Password")
        send_keys("{ENTER}")
        clickDiscount(dlg, disc, misc.customer_id, misc.customer_name, misc.address, misc.tin, misc.bus_style)
        clickBtn(dlg, "CASH")
        clickKeypad(dlg, "exact amount")
        clickBtn(dlg, "OK")
        if(checkIfExist(dlg,'RE-ROUTE')) :
            clickBtn(dlg, 'RE-ROUTE')
            clickBtn(dlg, 'P O S')

def free(dlg, transaction_type = "FREE" ):
    clickBtn(dlg, transaction_type)
    free = config.free_transact
    for tender in free.free_tender:
        clickBtn(dlg, free.prod_group)
        clickBtn(dlg, free.product)
        clickKeypad(dlg, "check")
        clickBtn(dlg, tender)
        inputText_Re(dlg, free.charge_to, "Charge")
        send_keys("{ENTER}")
        if(checkIfExist(dlg,'RE-ROUTE')) :
            clickBtn(dlg, 'RE-ROUTE')
            clickBtn(dlg, 'P O S')



def bulk(dlg, transaction_type = 'BULK\r\nORDER'):
    clickBtn(dlg, transaction_type)
    bulk = config.bulk_transact
    for disc in bulk.disc :
        clickBtn(dlg, bulk.prod_group)
        clickBtn(dlg, bulk.product)
        clickKeypad(dlg, "check")
        clickBtn(dlg, bulk.deposit_name)
        duplicate_exists = True  # Set initial flag

        while duplicate_exists:
            inputText_Re(dlg, generate_random_number(6), "Contract")  # Input the random number
            send_keys("{TAB}")
            #Check if the contract number is a duplicate
            duplicate_exists = checkIfExist(dlg, 'Duplicate Contract Number!', "Text")
            if duplicate_exists:
                clickBtn('OK')  
        inputText_Re(dlg, bulk.name, "Name")
        send_keys("{TAB}")
        inputText_Re(dlg, generate_random_number(7), "Phone")
        send_keys("{TAB}")
        doubleClickDateArrow(dlg)
        send_keys("{TAB}")
        inputText_Re(dlg, bulk.time, "Time")
        send_keys("{TAB}")
        inputText_Re(dlg, bulk.funcRoom, "FuncRoom")
        send_keys("{ENTER}")
        clickBtn(dlg, 'DISC')
        inputText_Re(dlg, bulk.manager_id, "Manager")
        send_keys("{TAB}")
        inputText_Re(dlg, bulk.manager_pass, "Password")
        send_keys("{ENTER}")
        clickDiscount(dlg, disc, bulk.customer_id, bulk.customer_name, bulk.address, bulk.tin, bulk.bus_style, promo_amount=20)
        clickBtn(dlg, 'CASH')
        clickKeypad(dlg, "exact amount")
        clickBtn(dlg, 'RECALL', secondsToSleep=5)
        clickBlkRecallBtn(dlg, 'check')
        clickKeypad(dlg, 'check')
        clickBtn(dlg, 'FINAL\r\nPAYMENT')
        clickBtn(dlg, 'CASH')
        clickBtn(dlg, 'OK')
        if(checkIfExist(dlg,'RE-ROUTE')) :
            clickBtn(dlg, 'RE-ROUTE')
            clickBtn(dlg, 'P O S')

def foodDineIn(dlg, transaction_type='DINE IN'):
    dine_in = config.transact
    clickBtn(dlg, transaction_type)
    for disc in dine_in.disc :
        print(disc)
        clickBtn(dlg, dine_in.prod_group)
        clickBtn(dlg, dine_in.product)
        clickKeypad(dlg, "check")
        clickBtn(dlg, "DISC")
        inputText_Re(dlg, dine_in.manager_id, "Manager")
        send_keys("{TAB}")
        inputText_Re(dlg, dine_in.manager_pass, "Password")
        send_keys("{ENTER}")
        clickDiscount(dlg, disc, dine_in.customer_id, dine_in.customer_name, dine_in.address, dine_in.tin, dine_in.bus_style)
        clickBtn(dlg, "CASH")
        clickKeypad(dlg, "exact amount")
        if(disc == "EMPLOYEE DISC" or disc == "PROMO AMOUNT"): 
            clickKeypad(dlg, 1)
            clickKeypad(dlg, "check")
            clickBtn(dlg, "YES")
        clickBtn(dlg, "OK")
        if(checkIfExist(dlg,'RE-ROUTE')) :
            clickBtn(dlg, 'RE-ROUTE')
            clickBtn(dlg, 'P O S')

def foodTakeOut(dlg, transaction_type = "TAKE OUT"):
    take_out = config.transact
    clickBtn(dlg, transaction_type)
    for disc in take_out.disc :
        clickBtn(dlg, take_out.prod_group)
        clickBtn(dlg, take_out.product)
        clickKeypad(dlg, "check")
        clickBtn(dlg, "DISC")
        inputText_Re(dlg, take_out.manager_id, "Manager")
        send_keys("{TAB}")
        inputText_Re(dlg, take_out.manager_pass, "Password")
        send_keys("{ENTER}")
        clickDiscount(dlg, disc, take_out.customer_id, take_out.customer_name, take_out.address, take_out.tin, take_out.bus_style)
        clickBtn(dlg, "CASH")
        clickKeypad(dlg, "exact amount")
        
        clickKeypad(dlg, 1)
        clickKeypad(dlg, "check")
        clickBtn(dlg, "YES")
        clickBtn(dlg, "OK")
        if(checkIfExist(dlg,'RE-ROUTE')):
            clickBtn(dlg, 'RE-ROUTE')
            clickBtn(dlg, 'P O S')

def bacchusDineIn(dlg, transaction_type='DINE IN') :
    dine_in = config.transact
    clickBtn(dlg, transaction_type)
    for disc in dine_in.disc :
        #----server and table----#
        inputText_Re(dlg, dine_in.cashier_id, "Server?")
        clickKeypad(dlg, 'check')
        clickBtn(dlg, dine_in.table)
        inputText_Re(dlg, '1', "Pax")
        #----server and table----#
        send_keys("{ENTER}")
        clickBtn(dlg, dine_in.prod_group)
        clickBtn(dlg, dine_in.product)
        clickKeypad(dlg, "check")
        clickBtn(dlg, 'STORE\r\nORDER')
        if(checkIfExist(dlg,'RE-ROUTE')) :
            clickBtn(dlg, 'RE-ROUTE')
            clickBtn(dlg, 'P O S')
        #----recall----#
        inputText_Re(dlg, dine_in.cashier_id, "Server?")
        send_keys("{ENTER}")
        clickBtn(dlg, dine_in.table)
        #----recall----#
        clickKeypad(dlg, "check")
        clickBtn(dlg, 'FINAL\r\nPAYMENT')
        clickBtn(dlg, 'DISC')
        inputText_Re(dlg, dine_in.manager_id, "Manager")
        send_keys("{TAB}")
        inputText_Re(dlg, dine_in.manager_pass, "Password")
        send_keys("{ENTER}")
        clickDiscount(dlg, disc, dine_in.customer_id, dine_in.customer_name, dine_in.address, dine_in.tin, dine_in.bus_style, 20
                    )
        clickBtn(dlg, 'CASH')
        clickKeypad(dlg, 'exact amount')
        clickBtn(dlg, "OK")

def bacchusTakeOut(dlg, transaction_type='TAKE OUT') :
    dine_in = config.transact
    clickBtn(dlg, transaction_type)
    for disc in dine_in.disc :
        #----server and table----#
        inputText_Re(dlg, dine_in.cashier_id, "Server?")
        send_keys("{ENTER}")
        clickBtn(dlg, dine_in.table)
        inputText_Re(dlg, '1', 'Pax')
        #----server and table----#
        send_keys("{ENTER}")
        clickBtn(dlg, dine_in.prod_group)
        clickBtn(dlg, dine_in.product)
        clickKeypad(dlg, "check")
        clickBtn(dlg, 'STORE\r\nORDER')
        if(checkIfExist(dlg,'RE-ROUTE')) :
            clickBtn(dlg, 'RE-ROUTE')
            clickBtn(dlg, 'P O S')
        #----recall----#
        inputText_Re(dlg, dine_in.cashier_id, 'Server?')
        send_keys("{ENTER}")
        clickBtn(dlg, dine_in.table)
        #----recall----#
        clickKeypad(dlg, "check")
        clickBtn(dlg, 'FINAL\r\nPAYMENT')
        clickBtn(dlg, 'DISC')
        inputText_Re(dlg, dine_in.manager_id, "Manager")
        send_keys("{TAB}")
        inputText_Re(dlg, dine_in.manager_pass, "Password")
        send_keys("{ENTER}")
        clickDiscount(dlg, disc, dine_in.customer_id, dine_in.customer_name, dine_in.address, dine_in.tin, dine_in.bus_style, 20
                    )
        clickBtn(dlg, 'CASH')
        clickKeypad(dlg, 'exact amount')
        clickBtn(dlg, "OK")