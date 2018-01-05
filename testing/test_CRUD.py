import unittest
import sqlite3
import sys
from setup_test_db import setup_user, setup_holdings, teardown_user, teardown_holdings

sys.path.append('../')
sys.path.append('~/Desktop/pymarket/db_func')
from db_func.menu_func import get_net_worth, display_holdings, update_holding, delete_holding, make_holding

with sqlite3.connect("test_pymarket.db") as db:
    cursor = db.cursor()

class TestMakeFunction(unittest.TestCase):
	def test_make_holding(self):
		'''test that make works in general, no need to test if user doesn't exist,
	 		since function only called when logged in'''
		teardown_user()
		teardown_holdings()
		setup_user()
		setup_holdings()
		make_holding(1, 'TEUM', 8.09, 1.27, 1, "test_pymarket.db")
		query = '''SELECT * FROM holdings where holdingID=? and userID=?'''
		cursor.execute(query, [(18), (1)])
		self.assertCountEqual([(18, 1, 'TEUM', 8.09, 1.27, 1)], cursor.fetchall())

	def test_make_holding_string_inputs(self):
		'''test that the function still works with all string inputs'''
		teardown_user()
		teardown_holdings()
		setup_user()
		setup_holdings()
		make_holding('1', 'TEUM', '8.09', '1.27', '1', "test_pymarket.db")
		query = '''SELECT * FROM holdings where holdingID=? and userID=?'''
		cursor.execute(query, [(18), (1)])
		self.assertCountEqual([(18, 1, 'TEUM', 8.09, 1.27, 1)], cursor.fetchall())	


class TestDeleteFunction(unittest.TestCase):
	def test_delete_holding(self):
		'''test that remove works in general'''
		teardown_user()
		teardown_holdings()
		setup_user()
		setup_holdings()
		delete_holding(4, 8, "test_pymarket.db")
		query = '''SELECT * FROM holdings where holdingID=? and userID=?'''
		cursor.execute(query, [(8), (4)])
		self.assertCountEqual([], cursor.fetchall())

	def test_delete_holding_not_exist(self):
		'''test that remove works with an invalid holding, doesn't crash'''
		teardown_user()
		teardown_holdings()
		setup_user()
		setup_holdings()
		delete_holding(2, 8, "test_pymarket.db")
		query = '''SELECT * FROM holdings where holdingID=? and userID=?'''
		cursor.execute(query, [(8), (2)])
		self.assertCountEqual([], cursor.fetchall())


class TestUpdateFunction(unittest.TestCase):
	def test_update_holding(self):
		'''test that update works in general'''
		teardown_user()
		teardown_holdings()
		setup_user()
		setup_holdings()
		update_holding(4, 8, 10, 10, "test_pymarket.db")
		query = '''SELECT * FROM holdings where holdingID=? and userID=?'''
		cursor.execute(query, [(8), (4)])
		self.assertEqual(cursor.fetchall()[0][3], 10.0)

	def test_update_holding_wrong_id(self):
		'''test that update works with wrong id given'''
		teardown_user()
		teardown_holdings()
		setup_user()
		setup_holdings()
		update_holding(2, 8, 10, 10, "test_pymarket.db")
		query = '''SELECT * FROM holdings where holdingID=? and userID=?'''
		cursor.execute(query, [(8), (4)])
		self.assertEqual(cursor.fetchall()[0][3], 11.24)	

suite = unittest.TestLoader().loadTestsFromTestCase(TestUpdateFunction)
unittest.TextTestRunner(verbosity=3).run(suite)

# suite = unittest.TestLoader().loadTestsFromTestCase(TestDeleteFunction)
# unittest.TextTestRunner(verbosity=3).run(suite)

# suite = unittest.TestLoader().loadTestsFromTestCase(TestMakeFunction)
# unittest.TextTestRunner(verbosity=2).run(suite)