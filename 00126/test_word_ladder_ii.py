import unittest
from word_ladder_ii import Solution


class TestSolution(unittest.TestCase):
    def test_isValid_Solution(self):
        sol = Solution()
        self.assertEqual(
            [["hit", "hot", "dot", "dog", "cog"], ["hit", "hot", "lot", "log", "cog"]],
            sol.findLadders(beginWord="hit", endWord="cog", wordList=["hot", "dot", "dog", "lot", "log", "cog"])
        )
        self.assertEqual([], sol.findLadders(beginWord="hit", endWord="cog", wordList=["hot","dot","dog","lot","log"]))


if __name__ == '__main__':
    unittest.main()
