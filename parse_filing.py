from bs4 import BeautifulSoup as bs
import requests
import pandas as pd
import time
import csv

#User Agent info
headers = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
    
    'Accept-Encoding': 'gzip, deflate'
}

# filings_list_csv = pd.read_csv('aapl.csv')

# filings_form = filings_list_csv['form']
# filings_form_list = list(filings_form)

# def ModifyArchiveUrl(ticker, documentnum, primarydoc):
#     url = f'https://www.sec.gov/ix?doc=/Archives/edgar/data/{ticker}/{documentnum}/{primarydoc}'    
#     return url

# for i, row in enumerate(filings_form_list):
#     if row == '10-K':
#         primarydoc = filings_list_csv.at[i,"primaryDocument"]
#         filing_accessionNumber = filings_list_csv.at[i,"accessionNumber"].replace("-","")

#         new_archive_url = ModifyArchiveUrl('320193' ,filing_accessionNumber, primarydoc)

#         new_archive_page = requests.get(new_archive_url, headers=headers)
        
#         print(new_archive_url)

        
url = f'https://www.sec.gov/Archives/edgar/data/320193/000119312511282113/d220209d10k.htm'

page_to_parse = requests.get(url, headers=headers)
call_status = page_to_parse.status_code
print((call_status))

table_MN = pd.read_html(page_to_parse.text)
# print(f'Total tables: {len(table_MN)}')
print(table_MN)
