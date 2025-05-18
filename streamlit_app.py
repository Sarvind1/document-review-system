"""Entry point for Streamlit Cloud deployment.

This file imports and runs the main Streamlit application from the src module.
"""

import sys
import os

# Add the current directory to sys.path
sys.path.append(os.path.abspath("."))

# Import the main app module
from src.app import *

# The app code will be executed when this file is run by Streamlit 