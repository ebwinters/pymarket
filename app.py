from db_func.login import login, make_user
from db_func.data_base import cr_usr, cr_hold
from menu import show_menu
cr_usr()
cr_hold()

show_menu()

# is_logged_in = login()
# if is_logged_in != -1:
# 	#menu
# 	pass
