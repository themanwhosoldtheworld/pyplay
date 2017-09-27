from .context import doggy
import unittest

class Doggy_Suite(unittest.TestCase):
	def test_start(self):
		self.assertIsNone(doggy.start())

	def test_add_doggy(self):
		tricks = ["run","eat","sleep"]
		roxy = doggy.addDoggy("roxy",tricks)
		self.assertIsNotNone(roxy)


if __name__ == '__main__':
	unittest.main()
