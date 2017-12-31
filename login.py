import sqlite3
import getpass

def login():
	for i in range(3):
		username = input("Enter username: ")
		password = getpass.getpass("Enter password: ")

		with sqlite3.connect("pymarket.db") as db:
			cursor = db.cursor()
		find_user = ("SELECT * FROM user WHERE username = ? AND password = ?")
		cursor.execute(find_user, [(username), (password)])
		results = cursor.fetchall()

		if results:
			for p in results:
				print ("Welcome, " + p[1])
			break
		else:
			print ("Username & password combination not recognized\n\n")

login()

def make_user():
	pass