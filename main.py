import requests
import pandas as pd
from datetime import datetime
from google.cloud import bigquery
import os

# Configuration
PROJECT_ID = "your-project-id"
DATASET_ID = "market_data"
TABLE_ID = "raw_prices"

def fetch_market_data():
    """Extract: Mocking an API call to get crypto prices"""
    url = "https://api.binance.com/api/v3/ticker/price?symbol=BTCUSDT"
    response = requests.get(url)
    data = response.json()
    
    df = pd.DataFrame([{
        "symbol": data['symbol'],
        "price": float(data['price']),
        "volume": 100.0, # Mock volume
        "ingested_at": datetime.utcnow().isoformat()
    }])
    return df

def load_to_bigquery(df):
    """Load: Push data to BQ using the service account"""
    client = bigquery.Client(project=PROJECT_ID)
    table_ref = f"{PROJECT_ID}.{DATASET_ID}.{TABLE_ID}"
    
    job = client.load_table_from_dataframe(df, table_ref)
    job.result()  # Wait for the job to complete
    print(f"Successfully loaded {len(df)} rows to {table_ref}")

if __name__ == "__main__":
    data_df = fetch_market_data()
    load_to_bigquery(data_df)