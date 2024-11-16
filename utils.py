import pandas as pd

def extract_data(url):
    df = pd.read_csv(url)
    return df
#function to extract data for various df

def load_data():
    
    ev_sales_url = "https://api.iea.org/evs?parameters=EV%20sales&category=Historical&mode=Cars&csv=true"
    ev_sales_df = pd.read_csv(ev_sales_url)
    ev_sales_df = ev_sales_df[ev_sales_df["parameter"] == "EV sales"]
    cols_to_drop = ["mode", "category", "parameter"]
    ev_sales_df = ev_sales_df.drop(columns=cols_to_drop)
    
    return ev_sales_df




