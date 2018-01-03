"""Contains functions to display a menu for the main app"""

def show_menu():
	print ('#'*80)
	print ('Please select which action you would like to take')
	print ('1) Check holdings')
	print ('2) Update holdings')
	print ('3) Remove holdings')
	print ('4) Create new holding')
	selection = int(input())

	if selection not in range (1,5):	#if not valid selection, reselct
		show_menu()

	if selection == 1:	#check holdings
		#display individual holdings 		function for this 
		#allow to see net holdings
		pass

	if selection == 2:	#update holdings
		#display holdings 					function for this
		#choose which one to update using holdID
		pass

	if selection == 3:	#remove holdings
		#display holdings 					function for this
		#choose which to delete using holdID
		pass

	if selection == 4:	#create new holding
		pass



def check_holdings():
	#go to query file in db_Stuff
	#FUNCTION TO QUERY DB HERE
	pass

def update_holdings():
	#go to query file in db_Stuff
	#FUNCTION TO UPDATE HERE
	pass

def remove_holdings():
	#go to query file in db_Stuff
	#FUNCTION TO DELETE HERE
	pass

def create_holding():
	#go to query file in db_Stuff
	#FUNCTION TO CREATE HOLDING
	pass