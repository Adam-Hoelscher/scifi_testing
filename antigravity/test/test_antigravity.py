from antigravity.src.antigravity import fly
import unittest

class TestAntigravity(unittest.TestCase):

    def test_my_subtract_one(self):
        self.assertEqual(fly(), -9.8)

