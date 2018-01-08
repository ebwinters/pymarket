from db_func.login import login, make_user
from db_func.data_base import cr_usr, cr_hold
from db_func.menu_func import display_holdings, get_net_worth
# from db_func.backend_func import get_net_worth
from menu import show_menu, check_holdings

cr_usr()
cr_hold()
# get_net_worth('1')
# check_holdings('1')

usr = int(input("To make a user press 1, otherwise press 0: "))
if usr == 1:
	make_user()
usr = 10
if (usr != 1):
	is_logged_in = login()
	if is_logged_in != -1:
		show_menu(str(is_logged_in))

