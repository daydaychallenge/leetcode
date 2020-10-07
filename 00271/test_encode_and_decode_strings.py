import unittest
from encode_and_decode_strings import Codec


class TestSolution(unittest.TestCase):
    def test_generateParenthesis_Solution(self):
        sol = Codec()
        str_list = ['abc', 'Hello', 'World']
        self.assertEqual(str_list, sol.decode(sol.encode(str_list)))


if __name__ == '__main__':
    unittest.main()
