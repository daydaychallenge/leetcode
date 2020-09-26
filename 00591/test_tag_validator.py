import unittest
from tag_validator import Solution


class TestSolution(unittest.TestCase):
    def test_generateParenthesis_Solution(self):
        sol = Solution()
        self.assertTrue(sol.isValid("<DIV>This is the first line <![CDATA[<div>]]></DIV>"))
        self.assertTrue(sol.isValid("<DIV>>>  ![cdata[]] <![CDATA[<div>]>]]>]]>>]</DIV>"))


if __name__ == '__main__':
    unittest.main()
