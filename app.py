import streamlit as st
import pandas as pd

# Page setup
st.set_page_config(page_title="Sales Data Export", layout="wide")




# Show centered logo using st.image
col1, col2, col3 = st.columns([2, 1, 2])
with col2:
    st.image("Magrabi Retail Story Thumbnail.png", width=200)
st.title("Snowflake Data Export Interface")


# Sample filter values (mocked for POC)
store_list = ["Mall of The Emirates", "Dubai Mall", "Dubai Festival City Mall"]
country_list = ["UAE","KSA","Egypt","Qatar"]
city_list = ["Abu Dhabi", "Dubai", "Riyadh","Cairo","Doha"]
dataset_name = ["sales", "invoices", "traffic", "customers", "stores"]
date_list = ["2025-03-01", "2025-04-01", "2025-05-01","2025-06-01"]

# Filter inputs
col1, col2, col3, col4, col5 = st.columns(5)
with col1:
    store = st.selectbox("Select Store", store_list)
with col2:
    country = st.selectbox("Select Country", country_list)
with col3:
    city = st.selectbox("Select City", city_list)
with col4:
    dataset = st.selectbox("Select Dataset Name", dataset_name)
with col5:
    date = st.selectbox("Select Date", date_list)


# Simulated output data
def mock_data():
    return pd.DataFrame({
        "store": [store]*5,
        "country": [country]*5,
        "city": [city]*5,
        "date": [date]*5,
        "dataset":[dataset]*5,
        "invoice_id": [f"INV{100+i}" for i in range(5)],
        "item_id": [f"ITEM{200+i}" for i in range(5)],
        "net_sales": [round(100 + i * 15.75, 2) for i in range(5)],
    })


# Load Data Button
if st.button("Load Data"):
    result_df = mock_data()
    st.success(f"{len(result_df)} records loaded.")
    st.dataframe(result_df, use_container_width=True)

    # Download button
    csv = result_df.to_csv(index=False).encode("utf-8")
    st.download_button(
        label="Download CSV",
        data=csv,
        file_name=f"{store}_{date}_sales.csv",
        mime="text/csv"
    )


#remove hamburger 
st.markdown("""
    <style>
        .reportview-container {
            margin-top: -20em;
        }
        #MainMenu {visibility: hidden;}
        .stDeployButton {display:none;}
        footer {visibility: hidden;}
        #stDecoration {display:none;}
    </style>
""", unsafe_allow_html=True)
