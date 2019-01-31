import unittest
from adder import adder

class AdderTest(unittest.TestCase):
	def test_zero(self):
		self.assertTrue(adder(0) == 0)

	def test_negative(self):
		self.assertTrue(adder(-5) == 0)

	def test_five(self):
		self.assertTrue(int(adder(5)) == 15)

	def test_ten(self):
		self.assertTrue(int(adder(10)) == 55)


if __name__ == "__main__":
	unittest.main()

