import unittest
from print_words_vertically import Solution


class TestSolution(unittest.TestCase):
    def test_generateParenthesis_Solution(self):
        sol = Solution()
        self.assertEqual(["HAY", "ORO", "WEU"], sol.printVertically("HOW ARE YOU"))
        self.assertEqual(["TBONTB", "OEROOE", "   T"], sol.printVertically("TO BE OR NOT TO BE"))
        self.assertEqual(["CIC", "OSO", "N M", "T I", "E N", "S G", "T"], sol.printVertically("CONTEST IS COMING"))


if __name__ == '__main__':
    unittest.main()
