# test_jupiteraggr.py
"""
Tests for JupiterAggr module.
"""

import unittest
from jupiteraggr import JupiterAggr

class TestJupiterAggr(unittest.TestCase):
    """Test cases for JupiterAggr class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = JupiterAggr()
        self.assertIsInstance(instance, JupiterAggr)
        
    def test_run_method(self):
        """Test the run method."""
        instance = JupiterAggr()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
