import unittest

import main


class TestSum(unittest.TestCase):
    def test_example_pt1_is_954377(self):
        """
        Test that result is 954377
        """
        actual = main.d7("example.txt", 1)
        self.assertEqual(actual, 95437)

    def test_pt1_is_1543140(self):
        """
        Test that result is 15431407
        """
        actual = main.d7("input.txt", 1)
        self.assertEqual(actual, 1543140)

    def test_example_pt2_is_24933642(self):
        """
        Test that result is 24933642
        """
        actual = main.d7("example.txt", 2)
        self.assertEqual(actual, 24933642)

    def test_pt2_is_11285770(self):
        """
        Test that result is 11285770
        """
        actual = main.d7("input.txt", 2)
        self.assertEqual(actual, 11285770)


if __name__ == '__main__':
    unittest.main()
