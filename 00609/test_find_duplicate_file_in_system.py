import unittest
from find_duplicate_file_in_system import Solution


class TestSolution(unittest.TestCase):
    def test_isValid_Solution(self):
        sol = Solution()
        inputs = [
            "root/a 1.txt(abcd) 2.txt(efgh)",
            "root/c 3.txt(abcd)",
            "root/c/d 4.txt(efgh)",
            "root 4.txt(efgh)"
        ]
        output = [
            ["root/a/1.txt", "root/c/3.txt"],
            ["root/a/2.txt", "root/c/d/4.txt", "root/4.txt"]
        ]

        self.assertEqual(sorted(output), sorted(sol.findDuplicate(inputs)))


if __name__ == '__main__':
    unittest.main()
