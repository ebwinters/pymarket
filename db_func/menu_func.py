import sqlite3
from db_func.backend_func import get_current_price

with sqlite3.connect("pymarket.db") as db:
	cursor = db.cursor()



def get_net_worth(user_id):
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

	print ('net gain: $' + "%0.2f" % (net,))

"""Print out a users holdings to the terminal"""
def display_holdings(user_id):
	list_holdings = []
	query = ("SELECT * FROM holdings where userID = ?")
	cursor.execute(query, [(user_id),])
	for holding in cursor.fetchall():
		print ('holding id: ' + str(holding[0]))
		print ('holding: ' + str(holding[2]))
		print ('ammount: ' + str(holding[3]))
		print ('bought @: $' + str(holding[4]) + '\n')
	return list_holdings


