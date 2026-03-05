# test_cryptolink.py
"""
Tests for CryptoLink module.
"""

import unittest
from cryptolink import CryptoLink

class TestCryptoLink(unittest.TestCase):
    """Test cases for CryptoLink class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = CryptoLink()
        self.assertIsInstance(instance, CryptoLink)
        
    def test_run_method(self):
        """Test the run method."""
        instance = CryptoLink()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
