#!/usr/bin/env python3
"""Test script to verify the hello_world function can be imported from the package."""

import sys
import os

# Add the src directory to the Python path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

# Test importing hello_world function from the package
from open_swe_test import hello_world

# Call the function
hello_world()
