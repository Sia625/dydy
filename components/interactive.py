import streamlit as st
import pandas as pd
import numpy as np

def display_interactive_chart():
    st.write("Interactive Chart Demo")
    
    # Create sample data
    data = pd.DataFrame({
        'Date': pd.date_range(start='2023-01-01', periods=100),
        'Value': np.random.randn(100).cumsum()
    })
    
    # Use streamlit's native chart function instead of matplotlib
    st.line_chart(data.set_index('Date'))