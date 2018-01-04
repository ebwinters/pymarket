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
		teardown_user()
		teardown_holdings()
		setup_user()
		setup_holdings()
		make_holding(1, 'TEUM', 8.09, 1.27, 1, "test_pymarket.db")
		query = '''SELECT * FROM holdings where holdingID=?'''
		cursor.execute(query, [(18),])
		self.assertCountEqual([(18, 1, 'TEUM', 8.09, 1.27, 1)], cursor.fetchall())

suite = unittest.TestLoader().loadTestsFromTestCase(TestMakeFunction)
unittest.TextTestRunner(verbosity=2).run(suite)