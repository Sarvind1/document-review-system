"""Entry point for Streamlit deployment.

This file imports and runs the main Streamlit application from the src module.
"""

import sys
import os
from pathlib import Path

# Add the project root to Python path
current_dir = Path(__file__).parent
sys.path.insert(0, str(current_dir))

# Import and run the main app
try:
    import streamlit as st
    
    # Show version info in sidebar
    st.sidebar.markdown("### Version Info")
    st.sidebar.markdown("Branch: `main`")
    st.sidebar.markdown("Version: Multiple PDF Methods Test")
    
    from src.app import main
    main()
except Exception as e:
    import streamlit as st
    st.error(f"Error loading application: {str(e)}")
    st.write("Debug info:")
    st.write(f"Current directory: {os.getcwd()}")
    st.write(f"Python path: {sys.path}")
    st.write(f"Directory contents: {os.listdir('.')}")
