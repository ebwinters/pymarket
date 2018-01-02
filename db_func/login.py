import sqlite3
import getpass
from hashlib import blake2b

"""Return user id from function to only allow to to edit their data". If -1,
not valid user"""
def login():
	for i in range(3):
		username = input("Enter username: ")
		password = getpass.getpass("Enter password: ")

		with sqlite3.connect("pymarket.db") as db:
			cursor = db.cursor()
		password = password.encode()
		pw = blake2b(digest_size=20)
		pw.update(password)
		pw = pw.hexdigest()
		find_user = ("SELECT * FROM user WHERE username = ? AND password = ?")
		cursor.execute(find_user, [(username), (pw)])
		results = cursor.fetchall()

		if results:
			for p in results:
				print ("Welcome, " + p[1])
				print()
			return int(p[0])
			break
		else:
			print ("Username & password combination not recognized\n\n")
	print ("Too many incorrect matches, exiting")
	return -1


def make_user():
	found = 0
	while found == 0:
		username = input("Enter a username: ")
		with sqlite3.connect("pymarket.db") as db:
			cursor = db.cursor()
		find_user = ("SELECT * FROM user WHERE username = ?")
		cursor.execute(find_user, [(username),])
		if cursor.fetchall():
			print ("Username already taken, please try again\n\n")
		else:
			found = 1
	password = getpass.getpass("Enter a password: ")
	password2 = getpass.getpass("Re-Enter password: ")
	while password != password2:
		print ("Passwords didn't match, try again\n\n")
		password = getpass.getpass("Enter a password: ")
		password2 = getpass.getpass("Re-Enter password: ")
	password = blake2b(digest_size=20)
	password2 = password2.encode()
	password.update(password2)
	password = password.hexdigest()
	insert_data = '''INSERT INTO user(username, password)
					VALUES(?, ?)'''
	cursor.execute(insert_data, [(username), (password)])
	db.commit()
	print ("User created!")

