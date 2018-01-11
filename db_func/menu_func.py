import sqlite3
from db_func.backend_func import get_current_price

with sqlite3.connect("pymarket.db") as db:
	cursor = db.cursor()



def get_net_worth(user_id, db_name):
	with sqlite3.connect(db_name) as db:
		cursor = db.cursor()
	money_spent = []
	current_price = []
	net = 0
	get_original_stats_query = ("SELECT abrv, hold, bought_at, crypt FROM holdings where userID = ?")
	cursor.execute(get_original_stats_query,[(user_id),])
	for holding in cursor.fetchall():	#get orig money spent
		money_spent.append(holding[1] * holding[2])

	cursor.execute(get_original_stats_query,[(user_id),])
	for holding in cursor.fetchall():	#get current gainz
		current_price.append(holding[1] * get_current_price(holding[0], holding[3]))

	for i in range(len(money_spent)):
		net += (current_price[i] - money_spent[i])

	return ('net gain: $' + "%0.2f" % (net,))

"""Print out a users holdings to the terminal"""
def display_holdings(user_id, db_name):
	with sqlite3.connect(db_name) as db:
		cursor = db.cursor()
	list_holdings = []
	query = ("SELECT * FROM holdings where userID = ?")
	cursor.execute(query, [(user_id),])
	return cursor.fetchall()

"""Update holdings with userid and holding to change as holdingID"""
def update_holding(user_id, holding_to_change, hold_amt, bought_at, db_name):
	with sqlite3.connect(db_name) as db:
		cursor = db.cursor()
	query = ("UPDATE holdings set hold = ?, bought_at = ? where userID = ? and holdingID = ?")
	cursor.execute(query,[(float(hold_amt)), (float(bought_at)), (user_id), (holding_to_change)])
	db.commit()
	print ("Holding " + str(holding_to_change) + " updated.")

"""Delete holding with userid and holding to change is holdingID"""
def delete_holding(user_id, holding_to_delete, db_name):
	with sqlite3.connect(db_name) as db:
		cursor = db.cursor()

	query = ("DELETE FROM holdings where userID = ? AND holdingID = ?")
	cursor.execute(query,[(user_id), (holding_to_delete)])
	db.commit()
	query = ("SELECT * FROM holdings where userID = ? AND holdingID = ?")
	cursor.execute(query, [(user_id), (holding_to_delete)])
	if len(cursor.fetchall()) == 0:
		print ("Holding " + str(holding_to_delete) + " deleted.")

def make_holding(user_id, abrv, hold, bought_at, crypt, db_name):
	with sqlite3.connect(db_name) as db:
		cursor = db.cursor()
	query = ('''INSERT INTO holdings(userID, abrv, hold, bought_at, crypt)
				VALUES (?, ?, ?, ?, ?)''')
	cursor.execute(query, [(user_id), (abrv), (hold), (bought_at), (crypt)])
	db.commit()
	
