import unittest
from sample import get_area_of_rectangle

class TestSampleMethods(unittest.TestCase):
    """
    Test harness
    """

    def test_increment_by_two(self):
        """
        Test area of rectangle
        """
        self.assertEqual(get_area_of_rectangle(5, 5), 25)
        self.assertEqual(get_area_of_rectangle(2, 3), 6)
        self.assertEqual(get_area_of_rectangle(4, 3), 12)

if __name__ == '__main__':
    unittest.main()
