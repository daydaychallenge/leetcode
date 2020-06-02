import unittest
from defanging_an_ip_address import Solution


class TestSolution(unittest.TestCase):
    def test_isValid_Solution(self):
        sol = Solution()
        self.assertEqual('1[.]1[.]1[.]1', sol.defangIPaddr('1.1.1.1'))


if __name__ == '__main__':
    unittest.main()
