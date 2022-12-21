import unittest

import main


class TestSum(unittest.TestCase):
    def test_example_pt1_is_21(self):
        """
        Test that result issa knife.
        """
        actual = main.treehouse('example.txt', 1)
        self.assertEqual(actual, 21)

    def test_input_pt1_1690(self):
        """
        Test that result is 1690.
        """
        actual = main.treehouse('input.txt', 1)
        self.assertEqual(actual, 1690)

    def test_example_pt2_is_8(self):
        """
        Test that result is 8.
        """
        actual = main.treehouse('example.txt', 2)
        self.assertEqual(actual, 8)

    def test_input_pt2_is_535680(self):
        """
        Test that result is 535680.
        """
        actual = main.treehouse('input.txt', 2)
        self.assertEqual(actual, 535680)


if __name__ == '__main__':
    unittest.main()
