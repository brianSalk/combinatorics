from functions import *
from triangles import *
import unittest


class TestFunctions(unittest.TestCase):
    def test_P(self):
        self.assertEqual(P(5, 2), 20)
        self.assertEqual(P(5, 5), 120)
        self.assertEqual(P(10, 0), 1)
        with self.assertRaises(ValueError):
            P(-1, 1)
            P(1, -1)

    def test_C(self):
        # test positive
        self.assertEqual(C(5, 0), 1)
        self.assertEqual(C(5, 1), 5)
        self.assertEqual(C(5, 2), 10)
        self.assertEqual(C(5, 3), 10)
        self.assertEqual(C(5, 4), 5)
        self.assertEqual(
            C(
                5,
                5,
            ),
            1,
        )
        # test negativeC(-n+r-1,r) * (-1)**r
        self.assertEqual(C(-5, 0), C(5 + 0 - 1, 0) * (-1) ** 0)
        self.assertEqual(C(-5, 1), C(5 + 1 - 1, 1) * (-1) ** 1)
        self.assertEqual(C(-5, 2), C(5 + 2 - 1, 2) * (-1) ** 2)
        self.assertEqual(C(-5, 3), C(5 + 3 - 1, 3) * (-1) ** 3)
        self.assertEqual(C(-5, 4), C(5 + 4 - 1, 4) * (-1) ** 4)
        self.assertEqual(C(-5, 5), C(5 + 5 - 1, 5) * (-1) ** 5)
        # throw if r is negative
        with self.assertRaises(ValueError):
            C(1, -1)

    def test_fact(self):
        self.assertEqual(fact(0), 1)
        self.assertEqual(fact(1), 1)
        self.assertEqual(fact(2), 2)
        self.assertEqual(fact(3), 6)
        self.assertEqual(fact(4), 24)

    def test_multinomial(self):
        self.assertEqual(multinomial(5, 2, 3), 10)
        # test raises if negative
        with self.assertRaises(ValueError):
            multinomial(5, 2, -1, 4)
        with self.assertRaises(ValueError):
            multinomial(5, 2, 4)

    def test_stirling1(self):
        self.assertEqual(stirling1(5, 3), 35)
        self.assertEqual(stirling1(10, 3), 1_172_700)

    def test_stirling2(self):
        self.assertEqual(stirling2(5, 3), 25)
        self.assertEqual(stirling2(7, 4), 350)

    def test_bell(self):
        self.assertEqual(bell(0), 1)
        self.assertEqual(bell(4), 15)
        self.assertEqual(bell(5), 52)
        with self.assertRaises(ValueError):
            bell(-1)

    def test_ordered_bell(self):
        self.assertEqual(ordered_bell(0), 1)
        self.assertEqual(ordered_bell(4), 75)
        self.assertEqual(ordered_bell(5), 541)
        with self.assertRaises(ValueError):
            bell(-1)

    def test_stars_bars(self):
        def c_to_stars(n, k):
            return C(n + k - 1, k - 1)

        for i in range(8):
            for j in range(i):
                if i > 0 and j > 0:
                    self.assertEqual(c_to_stars(i, j), stars_bars(i, j))

    # maybe I should delete binomial_theorem...
    def test_catalan(self):
        expected = [1, 1, 2, 5, 14, 42, 132]
        for i, ex in enumerate(expected):
            self.assertEqual(catalan(i), ex)
        with self.assertRaises(ValueError):
            catalan(-1)

    def test_paths_in_matrix(self):
        self.assertEqual(paths_in_matrix(3, 4), 10)
        self.assertEqual(paths_in_matrix(10, 9), 24310)
        self.assertEqual(paths_in_matrix(2, 3), 3)

    def test_pbinom(self):
        self.assertEqual(pbinom(10, 11, 0.5), 0)
        self.assertEqual(pbinom(10, -2, 0.5), 0)

        self.assertAlmostEqual(pbinom(10, 7, 0.8), 0.201, places=2)
        self.assertAlmostEqual(pbinom(10, 5, 0.2), 0.026, places=2)

        self.assertAlmostEqual(pbinom(10, 7, 0.8, "lt"), 0.121, places=2)
        self.assertAlmostEqual(pbinom(10, 5, 0.2, "lt"), 0.968, places=2)

        self.assertAlmostEqual(pbinom(10, 7, 0.8, "le"), 0.322, places=2)
        self.assertAlmostEqual(pbinom(10, 5, 0.2, "le"), 0.994, places=2)

        self.assertAlmostEqual(pbinom(10, 7, 0.8, "gt"), 0.678, places=2)
        self.assertAlmostEqual(pbinom(10, 5, 0.2, "gt"), 0.006, places=2)

        self.assertAlmostEqual(pbinom(10, 7, 0.8, "ge"), 0.879, places=2)
        self.assertAlmostEqual(pbinom(10, 5, 0.2, "ge"), 0.032, places=2)

        self.assertAlmostEqual(pbinom(10, 7, 0.8, "ne"), 1 - 0.201, places=2)
        self.assertAlmostEqual(pbinom(10, 5, 0.2, "ne"), 1 - 0.026, places=2)

        with self.assertRaises(ValueError):
            pbinom(2, 1, 2)

    def test_derangments(self):
        self.assertEqual(derangments(0), 1)
        self.assertEqual(derangments(1), 0)
        self.assertEqual(derangments(2), 1)
        self.assertEqual(derangments(3), 2)
        self.assertEqual(derangments(4), 9)
        self.assertEqual(derangments(5), 44)

        with self.assertRaises(ValueError):
            derangments(-1)

class TestTriangles(unittest.TestCase):
    def test_ptriangle(self):
        pasc_triangle = ptriangle()
        self.assertEqual(pasc_triangle.get(0, 0), 1)
        self.assertEqual(pasc_triangle.get(2, 1), 2)
        self.assertEqual(pasc_triangle.get(4, 2), 6)
        self.assertEqual(pasc_triangle.get(7, 4), 35)
        with self.assertRaises(IndexError):
            pasc_triangle.get(3, -1)
            pasc_triangle.get(4, 5)
            pasc_triangle(-1, 4)

    def test_bells_triagle(self):
        bell_triangle = btriangle(3)
        self.assertEqual(bell_triangle.get(0, 0), 1)
        self.assertEqual(bell_triangle.get(2, 1), 3)
        self.assertEqual(bell_triangle.get(4, 2), 27)
        self.assertEqual(bell_triangle.get(6, 3), 409)
        with self.assertRaises(IndexError):
            bell_triangle.get(-1, 0)
            bell_triangle.get(3, 4)


if __name__ == "__main__":
    unittest.main()
