#!/usr/bin/env python3
import os
import sys

# Add the project root directory to Python path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

# Import and run the main module
from src.main import main
from curses import wrapper

if __name__ == "__main__":
    wrapper(main) 