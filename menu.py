"""Contains functions to display a menu for the main app"""
from db_func.menu_func import display_holdings, get_net_worth, update_holding, delete_holding, make_holding
from db_func.backend_func import get_current_price
import sys

def show_menu(user_id):
	print ('#'*80)
	print ('Please select which action you would like to take')
	print ('0) Quit')
	print ('1) Check holdings')
	print ('2) Update holdings')
	print ('3) Remove holdings')
	print ('4) Create new holding')
	# print ('5) Get current price of coin/stock')
	selection = int(input())

	if selection not in range (0,6):	#if not valid selection, reselct
		print ('\n\n\nincorrect input please enter again')
		show_menu(user_id)

	if selection == 0:
		sys.exit()

	if selection == 1:	#check holdings
		check_holdings(user_id)

	if selection == 2:	#update holdings
		update_holdings(user_id)

	if selection == 3:	#remove holdings
		remove_holdings(user_id)

	if selection == 4:	#create new holding
		create_holding(user_id)

	# if selection == 5:
	# 	abrv = str(input("Please enter the abbreviation of the stock/coin you want to check: ")).upper()	
	# 	cryp = int(input("Please enter 0 for crypto, 1 for stock: "))	
	# 	print("Price of " + abrv + " is: $" + str(get_current_price(abrv, cryp)))
	# 	print()
	# 	show_menu()



def check_holdings(user_id):	#selc 1
	print ("Here is a list of your holdings:\n")
	display_holdings(str(user_id))
	get_net_worth(str(user_id))
	print('\n\n\n\n')
	show_menu(user_id)

def update_holdings(user_id):	#selc 2
	print ("Here is a list of your holdings:\n")
	display_holdings(str(user_id))
	holding_to_change = input("Please enter a holding id which you would like to change: ")
	update_holding(user_id, holding_to_change)
	print('\n\n\n\n')
	show_menu(user_id)


def remove_holdings(user_id):	#selc3
	print ("Here is a list of your holdings:\n")
	display_holdings(str(user_id))
	holding_to_delete = input("Please enter a holding id which you would like to delete: ")
	delete_holding(user_id, holding_to_delete)
	print('\n\n\n\n')
	show_menu(user_id)

def create_holding(user_id):	#selc4
	abrv = str(input("Please enter the abbreviation of the stock/coin you want to add: ")).upper()
	hold = float(input("Please enter the amount you bought: "))
	bought_at = float(input("Please enter the price which you bought at: $"))
	cryp = int(input("Please enter 0 for crypto, 1 for stock: "))
	make_holding(user_id, abrv, hold, bought_at, cryp)
	print()
	display_holdings(user_id)
	print('\n\n\n\n')
	show_menu(user_id)


