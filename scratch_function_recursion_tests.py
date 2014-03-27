import unittest

from scratch_function_recursion import Fibo, FiboRecur

class RecursionTest(unittest.TestCase):
	def setUp(self):
		self.fibo = Fibo().fibo
		self.fibo_recur = FiboRecur().fibo_recur

	def test_fibo_term_one(self):
		self.assertEqual(self.fibo(1),1)

	def test_fibo_term_two(self):
		self.assertEqual(self.fibo(2),1)		

	def test_fibo_term_three(self):
		self.assertEqual(self.fibo(3),2)
		# 0 1 1 2 3 5 8 13		

	def test_fibo_term_zero(self):
		self.assertEqual(self.fibo(0),0)
		# 0 1 1 2 3 5 8 13		
	def test_fibo_term_hundred(self):
		self.assertEqual(self.fibo(20),6765)	

	def test_fibo_term_one_recur(self):
		self.assertEqual(self.fibo_recur(1),1)

	def test_fibo_term_two_recur(self):
		self.assertEqual(self.fibo_recur(2),1)		

	def test_fibo_term_three_recur(self):
		self.assertEqual(self.fibo_recur(3),2)
		# 0 1 1 2 3 5 8 13		

	def test_fibo_term_zero_recur(self):
		self.assertEqual(self.fibo_recur(0),0)
		# 0 1 1 2 3 5 8 13		
	def test_fibo_term_hundred_recur(self):
		self.assertEqual(self.fibo_recur(20),6765)	