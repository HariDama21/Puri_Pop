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
            border-radius: 8px;
            padding: 10px 20px;
        }
    </style>
""", unsafe_allow_html=True)

# Item prices
item_prices = {
    "Pani Puri": 20,
    "Masala Puri": 25,
    "Dahi Puri": 30,
    "Sev Puri": 30,
    "Chicken Puri": 50,
    "Lays Puri": 50
}

# Initialize sales data storage
if "sales_data" not in st.session_state:
    st.session_state.sales_data = pd.DataFrame(columns=["Item", "Count", "Total Price"])

# Title and subtitle
st.markdown("<div class='title-container'><h1 class='title'>Ganapathi's Kitchen Room 🍲</h1><p class='subtitle'>Fast, Easy, Delicious Billing</p></div>", unsafe_allow_html=True)

# Order Entry Section
st.markdown("<div class='order-section'>", unsafe_allow_html=True)
st.markdown("<h2 class='order-header'>🛒 Order Details</h2>", unsafe_allow_html=True)

# Input fields for each item
item_counts = {}
for item, price in item_prices.items():
    item_counts[item] = st.number_input(f"{item} (₹{price} each)", min_value=0, step=1)

# Calculate total price
total_price = sum(count * item_prices[item] for item, count in item_counts.items())
st.markdown(f"<p class='total-price'>Total Price: ₹{total_price}</p>", unsafe_allow_html=True)

# Submit bill button
if st.button("Submit Bill"):
    for item, count in item_counts.items():
        if count > 0:
            total_item_price = count * item_prices[item]
            new_entry = {"Item": item, "Count": count, "Total Price": total_item_price}
            st.session_state.sales_data = pd.concat(
                [st.session_state.sales_data, pd.DataFrame([new_entry])]
            ).reset_index(drop=True)
    
    # Reset input fields by clearing the session state for counts
    for item in item_counts.keys():
        item_counts[item] = 0
    
    st.success("Bill submitted successfully!", icon="✅")
st.markdown("</div>", unsafe_allow_html=True)

st.markdown("<div class='summary-section'>", unsafe_allow_html=True)
st.markdown("<h2 class='summary-header'>📊 Today's Sales Summary</h2>", unsafe_allow_html=True)
    
    # Display sales summary
    summary = st.session_state.sales_data.groupby("Item").agg({"Count": "sum", "Total Price": "sum"}).reset_index()

    
    st.table(summary)
    
    # Plotting sales data
    plt.figure(figsize=(10,5))
    plt.bar(summary["Item"], summary["Total Price"], color="#ff7b54")
    plt.xlabel('Items')
    plt.ylabel('Total Price (₹)')
    plt.title('Sales Summary')
    plt.xticks(rotation=45)
    st.pyplot(plt)
    
    st.markdown("</div>", unsafe_allow_html=True)

# Download sales data button
if st.button("Download Sales Data"):
    sales_csv = st.session_state.sales_data.to_csv(index=False).encode("utf-8")
    st.download_button("Download CSV", data=sales_csv, file_name="sales_data.csv", mime="text/csv")
