#!/usr/bin/python3
# filepath: /home/lucas/holbertonschool-higher_level_programming/python-test_driven_development/tests/6-max_integer_test.py
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Test class for max_integer function"""

    def test_empty_list(self):
        """Test with an empty list"""
        self.assertIsNone(max_integer([]))

    def test_single_element(self):
        """Test with a list containing one element"""
        self.assertEqual(max_integer([5]), 5)
        self.assertEqual(max_integer([-10]), -10)

    def test_positive_numbers(self):
        """Test with list of positive numbers"""
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)
        self.assertEqual(max_integer([1, 3, 4, 2]), 4)
        self.assertEqual(max_integer([10, 5, 7, 9]), 10)

    def test_negative_numbers(self):
        """Test with list of negative numbers"""
        self.assertEqual(max_integer([-1, -2, -3, -4]), -1)
        self.assertEqual(max_integer([-10, -5, -7, -2]), -2)

    def test_mixed_numbers(self):
        """Test with list of mixed positive and negative numbers"""
        self.assertEqual(max_integer([-1, 2, -3, 4]), 4)
        self.assertEqual(max_integer([-10, 0, 10, 5]), 10)

    def test_duplicate_numbers(self):
        """Test with list containing duplicate numbers"""
        self.assertEqual(max_integer([5, 5, 5, 5]), 5)
        self.assertEqual(max_integer([1, 5, 5, 3]), 5)

    def test_large_numbers(self):
        """Test with list containing large numbers"""
        self.assertEqual(max_integer([1000000, 10000, 100]), 1000000)
        
    def test_float_numbers(self):
        """Test with list containing float numbers"""
        self.assertEqual(max_integer([1.5, 2.5, 3.5]), 3.5)
        self.assertEqual(max_integer([-1.5, -2.5, -3.5]), -1.5)
        
    def test_mixed_types(self):
        """Test with list containing integers and floats"""
        self.assertEqual(max_integer([1, 2.5, 3, 4.5]), 4.5)
        
    def test_string_list(self):
        """Test with list of strings"""
        self.assertEqual(max_integer(["a", "b", "c", "d"]), "d")
        self.assertEqual(max_integer(["apple", "banana", "cherry"]), "cherry")
        
    def test_max_at_beginning(self):
        """Test with max value at beginning of list"""
        self.assertEqual(max_integer([4, 3, 2, 1]), 4)
        
    def test_max_in_middle(self):
        """Test with max value in middle of list"""
        self.assertEqual(max_integer([1, 2, 5, 3, 4]), 5)


if __name__ == '__main__':
    unittest.main()
