import unittest
from reorder_data_in_log_files import Solution


class TestSolution(unittest.TestCase):
    def test_isValid_Solution(self):
        sol = Solution()
        input = [
            "dig1 8 1 5 1",
            "let1 art can",
            "dig2 3 6",
            "let2 own kit dig",
            "let3 art zero"
        ]
        output = [
            "let1 art can",
            "let3 art zero",
            "let2 own kit dig",
            "dig1 8 1 5 1",
            "dig2 3 6"
        ]
        self.assertEqual(output, sol.reorderLogFiles(input))


if __name__ == '__main__':
    unittest.main()
