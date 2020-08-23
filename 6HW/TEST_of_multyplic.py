import list_multyplication
import logging
import unittest
from unittest.mock import patch


class TestListMethods(unittest.TestCase):
    def setUp(self):
        self.a = list(range(1, 800))

    def test_tuple_format(self):
        self.assertIsInstance(list_multyplication.multiply((1, 2)), tuple)

    def test_list_format(self):
        self.assertIsInstance(list_multyplication.multiply([1, 2, 3]), list)

    def test_tuple(self):
        if list_multyplication.multiply((1, 2, 3, 4)) != (24, 12, 8, 6):
            logging.error('test_multiply is not working in tuple')
        self.assertEqual(list_multyplication.multiply((1, 2, 3, 4)), (24, 12, 8, 6))
        self.assertEqual(list_multyplication.multiply((0, 2, 5, 0)), (0, 0, 0, 0))
        self.assertEqual(list_multyplication.multiply((0, 1, 2, 3, 4, 5)), (120, 0, 0, 0, 0, 0))

    def test_list(self):
        if list_multyplication.multiply([1, 2, 3, 4]) != [24, 12, 8, 6]:
            logging.error('test_multiply is not working')
        self.assertEqual(list_multyplication.multiply([1, 2, 3, 4]), [24, 12, 8, 6])
        self.assertEqual(list_multyplication.multiply([0, 2, 5, 0]), [0, 0, 0, 0])
        self.assertEqual(list_multyplication.multiply([0, 1, 2, 3, 4, 5]), [120, 0, 0, 0, 0, 0])

    @patch('list_multyplication.multiply', return_value=[24, 12, 8, 6])  # использование моков
    def test_of_mock(self, a):
        self.assertEqual(list_multyplication.multiply([1, 2, 3, 4]), [24, 12, 8, 6])

    def test_side_conditions_for_list(self):
        self.assertEqual(list_multyplication.multiply([1]), [1])
        self.assertEqual(list_multyplication.multiply([1, 2]), [2, 1])

    def test_side_conditions_for_tuple(self):
        self.assertEqual(list_multyplication.multiply((1,)), (1,))
        self.assertEqual(list_multyplication.multiply((1, 2)), (2, 1))

    def test_wrong_format(self):
        self.assertRaises(TypeError, lambda: list_multyplication.multiply([1, 'kekich', 3]))
        self.assertRaises(TypeError, lambda: list_multyplication.multiply((1, 'kek', 3)))


if __name__ == '__main__':
    unittest.main()
