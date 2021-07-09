import pandas as pd
import requests

def ModifyArchiveUrl(ticker, url_complement):
    url = f'https://www.sec.gov/Archives/edgar/data/{ticker}/{url_complement}.txt'
    
    return url

filings_list_csv = pd.read_csv('aapl.csv')

filings_form = filings_list_csv['form']
filings_form_list = list(filings_form)

#it works
for i, row in enumerate(filings_form_list):
    if row == '10-K':
        filing_accessionNumber = filings_list_csv.at[i,"accessionNumber"]

        new_archive_url = ModifyArchiveUrl('320193' ,filing_accessionNumber)

        new_archive_page = requests.get(new_archive_url)
        



        print(new_archive_url)

        
