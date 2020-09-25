import unittest
from search_suggestions_system import Solution


class TestSolution(unittest.TestCase):
    def test_generateParenthesis_Solution(self):
        sol = Solution()
        res1 = [
            ["mobile", "moneypot", "monitor"],
            ["mobile", "moneypot", "monitor"],
            ["mouse", "mousepad"],
            ["mouse", "mousepad"],
            ["mouse", "mousepad"]
        ]
        res2 = [["havana"], ["havana"], ["havana"], ["havana"], ["havana"], ["havana"]]
        res3 = [["baggage", "bags", "banner"], ["baggage", "bags", "banner"], ["baggage", "bags"], ["bags"]]
        self.assertEqual(res1, sol.suggestedProducts(["mobile", "mouse", "moneypot", "monitor", "mousepad"], "mouse"))
        self.assertEqual(res2, sol.suggestedProducts(["havana"], "havana"))
        self.assertEqual(res3, sol.suggestedProducts(["bags","baggage","banner","box","cloths"], "bags"))

        self.assertEqual(res1, sol.suggestedProducts01(["mobile", "mouse", "moneypot", "monitor", "mousepad"], "mouse"))
        self.assertEqual(res2, sol.suggestedProducts01(["havana"], "havana"))
        self.assertEqual(res3, sol.suggestedProducts01(["bags","baggage","banner","box","cloths"], "bags"))


if __name__ == '__main__':
    unittest.main()
