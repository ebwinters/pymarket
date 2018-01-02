from db_func.login import login, make_user
from db_func.data_base import cr_usr, cr_hold

cr_usr()
cr_hold()

is_logged_in = login()
if is_logged_in != -1:
	#menu
	pass
