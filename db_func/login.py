import sqlite3
import getpass
from hashlib import blake2b
import sys


"""Return user id from function to only allow to to edit their data". If -1,
not valid user"""
def login(username, password):
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
			return int(p[0])
			break
	else:
		return -1


def make_user(username, password, password2):
	found = 0
	while found == 0:
		with sqlite3.connect("pymarket.db") as db:
			cursor = db.cursor()
		find_user = ("SELECT * FROM user WHERE username = ?")
		cursor.execute(find_user, [(username),])
		if cursor.fetchall():
			break
		else:
			found = 1
	if password == password2:
		password = blake2b(digest_size=20)
		password2 = password2.encode()
		password.update(password2)
		password = password.hexdigest()
		insert_data = '''INSERT INTO user(username, password)
						VALUES(?, ?)'''
		cursor.execute(insert_data, [(username), (password)])
		db.commit()
			
	else:
		print ("Wrong combination")
		sys.exit()


