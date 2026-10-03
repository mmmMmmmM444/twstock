import contextlib
import io
import unittest

from twstock import scan


class ScanTest(unittest.TestCase):
    def test_selftest(self):
        # selftest 會印出含中文的表格；導向記憶體避免 Windows 主控台編碼問題
        with contextlib.redirect_stdout(io.StringIO()):
            self.assertEqual(scan.selftest(), 0)

    def test_to_num(self):
        self.assertEqual(scan.to_num("1,234.5"), 1234.5)
        self.assertEqual(scan.to_num("－3"), -3.0)
        self.assertIsNone(scan.to_num("--"))

    def test_is_common_stock(self):
        self.assertTrue(scan.is_common_stock("2330"))
        self.assertFalse(scan.is_common_stock("0050"))
        self.assertFalse(scan.is_common_stock("2330A"))


if __name__ == "__main__":
    unittest.main()
