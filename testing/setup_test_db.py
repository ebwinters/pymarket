import sys
import sqlite3

with sqlite3.connect("test_pymarket.db") as db:
    cursor = db.cursor()

def cr_usr():
    cursor.execute('''
CREATE TABLE IF NOT EXISTS user(
userID INTEGER PRIMARY KEY,
username VARCHAR(20) NOT NULL,
password VARCHAR(20) NOT NULL
);
''')

def cr_hold():
#0 if crypto
    cursor.execute('''
CREATE TABLE IF NOT EXISTS holdings(
holdingID INTEGER PRIMARY KEY,
userID INTEGER NOT NULL,
abrv VARCHAR(10) NOT NULL,
hold MONEY NOT NULL,
bought_at MONEY NOT NULL,
crypt BIT NOT NULL
);
''')

def setup_user():
	cr_usr()
	list_users_passes = [('ebw', 'ebw123'), ('rsw', 'rsw123'), ('lcw', 'dog32'),
		('krw', 'dogs1'), ('elerner', 'hil365'), ('hblock', '1234567'), ('jkenyon', 'cali46')]
	insert_data = '''INSERT INTO user(username, password) VALUES (?, ?)'''
	for user in list_users_passes:
		cursor.execute(insert_data, [(user[0]), (user[1])])
		db.commit()
	#Now the user db is filled with 7 users to manipulate

def teardown_user():
	query = '''DROP TABLE user'''
	cursor.execute(query)
	db.commit()

def setup_holdings():
	cr_hold()
	list_hold_info = [
		('1', 'AAPL', 37.2, 169.20, 1),		#Holding for ebw
		('1', 'ETH', .1, 667.59, 0),		#Holding for ebw
		('1', 'AAPL', 37.2, 169.20, 1),		#Holding for ebw
		('2', 'XRP', 325.0, 2.10, 0),		#Holding for rsw
		('3', 'MARA', 43.2, 4.50, 1),		#Holding for lcw
		('3', 'XML', 200.4, 269.80, 0),		#Holding for lcw
		('4', 'BTC', 6.1, 14003.54, 0),		#Holding for krw
		('4', 'TEUM', 11.24, 1.35, 1),		#Holding for krw
		('4', 'BAT', 32.13, .20, 0),		#Holding for krw
		('5', 'AMZN', 1.42, 903.86, 1),		#Holding for elerner
		('5', 'NKE', 13.62, 59.24, 1),		#Holding for elerner
		('6', 'UAA', 72.93, 19.40, 1),		#Holding for hblock
		('6', 'DVMT', 34.1, 72.46, 1),		#Holding for hblock
		('6', 'LTC', 3.42, 100.59, 0),		#Holding for hblock
		('6', 'TSLA', 13.83, 325.32, 1),	#Holding for hblock
		('7', 'LTC', .42, 80.29, 0),		#Holding for jkenyon
		('7', 'ETH', .2, 495.51, 0),		#Holding for jkenyon
	]
	insert_data = '''INSERT INTO holdings(userID, abrv, hold, bought_at, crypt) 
					VALUES (?, ?, ?, ?, ?)'''
	for holding in list_hold_info:
		cursor.execute(insert_data, [(holding[0]), (holding[1]), (holding[2]), (holding[3]), (holding[4])])
		db.commit()
	#Now the user db is filled with 7 users to manipulate

def teardown_holdings():
	query = '''DROP TABLE holdings'''
	cursor.execute(query)
	db.commit()




