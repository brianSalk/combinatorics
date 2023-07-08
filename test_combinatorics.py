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
    def test_C(self):
        # test positive
        self.assertEqual(C(5,0), 1)
        self.assertEqual(C(5,1), 5)
        self.assertEqual(C(5,2), 10)
        self.assertEqual(C(5,3), 10)
        self.assertEqual(C(5,4), 5)
        self.assertEqual(C(5,5,), 1)
        # test negativeC(-n+r-1,r) * (-1)**r
        self.assertEqual(C(-5,0),C(5+0-1,0) * (-1)**0)
        self.assertEqual(C(-5,1),C(5+1-1,1) * (-1)**1)
        self.assertEqual(C(-5,2),C(5+2-1,2) * (-1)**2)
        self.assertEqual(C(-5,3),C(5+3-1,3) * (-1)**3)
        self.assertEqual(C(-5,4),C(5+4-1,4) * (-1)**4)
        self.assertEqual(C(-5,5),C(5+5-1,5) * (-1)**5)
        # throw if r is negative
        with self.assertRaises(ValueError):
            C(1,-1)
    def test_fact(self):
        self.assertEqual(fact(0),1)
        self.assertEqual(fact(1),1)
        self.assertEqual(fact(2),2)
        self.assertEqual(fact(3),6)
        self.assertEqual(fact(4),24)
if __name__ == "__main__":
    unittest.main()
