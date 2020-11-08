import unittest
from brace_expansion_ii import Solution


class TestSolution(unittest.TestCase):
    def test_generateParenthesis_Solution(self):
        sol = Solution()
        self.assertEqual({"ac", "ad", "ae", "bc", "bd", "be"}, set(sol.braceExpansionII("{a,b}{c,{d,e}}")))
        self.assertEqual({"a", "ab", "ac", "z"}, set(sol.braceExpansionII("{{a,z},a{b,c},{ab,z}}")))


if __name__ == '__main__':
    unittest.main()
