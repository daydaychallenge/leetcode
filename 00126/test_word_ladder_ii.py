import unittest
from word_ladder_ii import Solution


class TestSolution(unittest.TestCase):
    def test_isValid_Solution(self):
        sol = Solution()
        source = [["hit", "hot", "dot", "dog", "cog"], ["hit", "hot", "lot", "log", "cog"]]
        expects = {''.join(item) for item in source}
        ret = sol.findLadders(beginWord="hit", endWord="cog", wordList=["hot", "dot", "dog", "lot", "log", "cog"])
        results = {''.join(item) for item in ret}
        self.assertEqual(expects, results)
        self.assertEqual([], sol.findLadders(beginWord="hit", endWord="cog", wordList=["hot","dot","dog","lot","log"]))


if __name__ == '__main__':
    unittest.main()
