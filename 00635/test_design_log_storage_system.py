import unittest
from design_log_storage_system import LogSystem


class TestSolution(unittest.TestCase):
    def test_generateParenthesis_Solution(self):
        log_sys = LogSystem()
        log_sys.put(1, "2017:01:01:23:59:59")
        log_sys.put(2, "2017:01:01:22:59:59")
        log_sys.put(3, "2016:01:01:00:00:00")
        self.assertEqual({1, 2, 3}, set(log_sys.retrieve("2016:01:01:01:01:01", "2017:01:01:23:00:00", "Year")))
        self.assertEqual({1, 2}, set(log_sys.retrieve("2016:01:01:01:01:01", "2017:01:01:23:00:00", "Hour")))


if __name__ == '__main__':
    unittest.main()
