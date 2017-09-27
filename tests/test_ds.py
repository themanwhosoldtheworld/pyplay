from .context import ds
import unittest

class DS_Suite(unittest.TestCase):
	def test_start(self):
		self.assertIsNotNone(ds.start())

if __name__ == '__main__':
	unittest.main()
