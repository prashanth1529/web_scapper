import requests
from bs4 import BeautifulSoup
import pandas as pd

def acquire_data(url):
    print(f"Fetching data from {url}...")
    
    # 1. Request the page
    headers = {"User-Agent": "Mozilla/5.0"}
    response = requests.get(url, headers=headers)
    
    if response.status_code == 200:
        # 2. Parse the HTML
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Example: Scrape all <h2> headers (common for article titles)
        titles = soup.find_all('h2')
        
        data_list = [t.get_text().strip() for t in titles]
        
        # 3. Save to a CSV using Pandas
        df = pd.DataFrame(data_list, columns=['Title'])
        df.to_csv('acquired_data.csv', index=False)
        print("Success! Data saved to acquired_data.csv")
    else:
        print(f"Failed to retrieve data. Status code: {response.status_code}")

if __name__ == "__main__":
    # You can replace this with a real URL you have permission to scrape
    target_url = "https://example.com" 
    acquire_data(target_url)