import sqlite3

with sqlite3.connect("pymarket.db") as db:
    cursor = db.cursor()

cursor.execute('''
	CREATE TABLE IF NOT EXISTS user(
	userID INTEGER PRIMARY KEY,
	username VARCHAR(20) NOT NULL,
	password VARCHAR(20) NOT NULL
		);
	''')

# cursor.execute('''
# 	INSERT INTO user(username, password)
# 	VALUES("test_user", "test_pass")
# 	''')
# db.commit()

# cursor.execute("SELECT * FROM user")
# print(cursor.fetchall())