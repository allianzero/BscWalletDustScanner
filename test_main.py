"""Tests for BscWalletDustScanner."""
import unittest
from main import calculate


class TestTool(unittest.TestCase):
    def test_main_function(self):
        self.assertAlmostEqual(calculate(0.0001, 0.001), True, places=6)


if __name__ == "__main__":
    unittest.main()
