import unittest
from integer_to_english_words import Solution


class TestSolution(unittest.TestCase):
    def test_Calculate_Solution(self):
        sol = Solution()
        self.assertEqual('Zero', sol.numberToWords(0))
        self.assertEqual('One', sol.numberToWords(1))
        self.assertEqual('Twenty', sol.numberToWords(20))

        self.assertEqual(
            'One Billion Two Hundred Thirty Four Million Five Hundred Sixty Seven Thousand Eight Hundred Ninety One',
            sol.numberToWords(1234567891))

        self.assertEqual(
            'One Million Two Hundred Thirty Four Thousand Five Hundred Sixty Seven',
            sol.numberToWords(1234567))


if __name__ == '__main__':
    unittest.main()
