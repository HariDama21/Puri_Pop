import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Configure the app page settings
st.set_page_config(page_title="Puri Pop", page_icon="🍲", layout="centered")

# Define CSS for styling the app
st.markdown("""
    <style>
        /* General Styling */
        body {
            background-color: #f9f9f9;
            font-family: 'Helvetica', sans-serif;
            color: #333333;
        }
        .main {
            padding: 1rem;
        }
        
        /* Title Styling */
        .title-container {
            background-color: #ffcc66;
            border-radius: 15px;
            padding: 20px;
            text-align: center;
            box-shadow: 0px 4px 12px rgba(0, 0, 0, 0.1);
        }
        .title {
            color: #333333;
            font-size: 2.5rem;
            font-weight: bold;
            margin: 0;
        }
        .subtitle {
            color: #555555;
            font-size: 1rem;
            margin: 5px 0 0;
        }

        /* Order Input Section */
        .order-section {
            background-color: #ffffff;
            border-radius: 10px;
            padding: 20px;
            margin-top: 20px;
            box-shadow: 0px 4px 8px rgba(0, 0, 0, 0.1);
        }
        .order-header {
            font-size: 1.5rem;
            color: #ff7b54;
            margin-bottom: 15px;
            font-weight: bold;
        }
        
        /* Summary Section */
        .summary-section {
            background-color: #fafafa;
            border-radius: 10px;
            padding: 20px;
            margin-top: 20px;
            box-shadow: 0px 4px 8px rgba(0, 0, 0, 0.1);
        }
        .summary-header {
            font-size: 1.5rem;
            color: #333333;
            font-weight: bold;
        }
        .total-price {
            font-size: 1.75rem;
            color: #28a745;
            font-weight: bold;
        }

        /* Button Styling */
        .stButton > button {
            background-color: #ff7b54;
            color: #ffffff;
            font-size: 1rem;
            font-weight: bold;
