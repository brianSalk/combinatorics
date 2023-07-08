from functions import *
import unittest
class TestFunctions(unittest.TestCase):
    
    def test_P(self):
        self.assertEqual(P(5,2), 20) 
        self.assertEqual(P(5,5), 120)
        self.assertEqual(P(10,0), 1)
        with self.assertRaises(ValueError):
            P(-1,1)
            P(1,-1)
if __name__ == "__main__":
    unittest.main()
