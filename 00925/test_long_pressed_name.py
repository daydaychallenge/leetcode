import unittest
from long_pressed_name import Solution


class TestSolution(unittest.TestCase):
    def test_Calculate_Solution(self):
        sol = Solution()
        self.assertTrue(sol.isLongPressedName('alex', 'aaleex'))
        self.assertFalse(sol.isLongPressedName('saeed', 'ssaaedd'))
        self.assertTrue(sol.isLongPressedName('leelee', 'lleeelee'))
        self.assertTrue(sol.isLongPressedName('laiden', 'laiden'))


if __name__ == '__main__':
    unittest.main()
