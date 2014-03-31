import unittest

class TestNyx(unittest.TestCase):
    def setUp(self):
        self.nyx = 'nyx'

    def test_nyx(self):
        self.assertFalse(self.nyx is not self.nyx)

if __name__ == '__main__':
    unittest.main()
