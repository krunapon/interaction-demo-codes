import unittest
import check_str


class TestStrFail(unittest.TestCase):
    def test_str_fail(self):
        self.assertRaises(ValueError, check_str.check_str, "fail")
        self.assertEqual(check_str.check_str("success"), "success")
