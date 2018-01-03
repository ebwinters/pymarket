import sqlite3

with sqlite3.connect("pymarket.db") as db:
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

# cursor.execute('''
# 	INSERT INTO user(username, password)
# 	VALUES("test_user", "test_pass")
# 	''')
# db.commit()

# cursor.execute("SELECT * FROM user")
# print(cursor.fetchall())