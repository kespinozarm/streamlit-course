import streamlit as st
from utils import load_data

###### Set up the page ######
st.set_page_config(
    page_title="EV Adoption Tracker",
    layout="centered", # or wide
    page_icon="🚗", # choose your favorite icon
    initial_sidebar_state="collapsed" # or expanded
)

### Load data ####
ev_sales_df = load_data()

#### modifying: 

# 1. Title
st.title("EV Adoption Tracker")

# 2. Subheader
st.subheader("This is a Subheader")

# 3. Selectbox

st.divider()
region_filter = st.selectbox("Select a region:", ev_sales_df["region"].unique())

filtered_df = ev_sales_df[ev_sales_df['region'] == region_filter]


st.bar_chart (filtered_df, x="year", y="value", color="region")

# 4. Subheader
st.subheader("This is a Subheader")

#5. Multi-select: 

country_filter = st.multiselect("Select a country", ev_sales_df["region"].unique(),default=["USA","China","Europe"])

powertrain_filter = st.selectbox("Select a powertrain", ev_sales_df["powertrain"].unique())

filtered_ev_sales_df= ev_sales_df[(ev_sales_df["region"].isin(country_filter)) & (ev_sales_df["powertrain"] == powertrain_filter)]

#line-chart

st.line_chart(filtered_ev_sales_df, x="year", y="value", color="region", x_label="year", y_label="Number of EVs sold (millions)")