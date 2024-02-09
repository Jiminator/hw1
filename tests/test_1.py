# test_google.py

import unittest

class Test1(unittest.TestCase):

    def test_standard_date(self):
        print("Hello World")
        
        assert 2 + 2 == 4

if __name__ == '__main__':
    unittest.main()
