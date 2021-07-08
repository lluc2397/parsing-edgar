from json.decoder import JSONDecodeError
from os import error
import requests
import random
import pandas as pd
from bs4 import BeautifulSoup
import time
import csv
import operator


#read, parse in list, change list to dataframe, dataframe to csv
# text = requests.get(f'https://www.sec.gov/include/ticker.txt').content
# text = text.decode("utf-8").split('\n')
# print(text)
# df_t = pd.DataFrame(text)
# df_t.to_csv('test.csv',index=False)

df = pd.read_csv('test.csv')


# for index, row in df.iterrows():
#     print(row["CIK"])
# all_tickers = df.get("Ticker")
# all_tickers = df.iloc("Ticker")
#first 0 last 12836

def get_proxies():
    url = f'https://free-proxy-list.net/'
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    modal = soup.find('div', class_="modal-body" )
    modal_text = modal.textarea.text.replace('Free proxies from free-proxy-list.net', '')
    
    modal_text_clean = modal_text.splitlines()[3:]

    return modal_text_clean

def ChangeUrl(search_ticker):
    # url = f'https://data.sec.gov/api/xbrl/companyfacts/CIK{search_ticker}.json'

    url = f'https://data.sec.gov/submissions/CIK{search_ticker}.json'
    
    return url

def TenDigitsCik(current_cik):
    CIK_str = str(current_cik)

    cik_length = len(CIK_str)

    if cik_length == 10 :
        new_cik = CIK_str
    else :
       new_cik = CIK_str.zfill(10)
    return new_cik
 
for position in range(0, 1):
    time.sleep(1/10)

    CIK = df.at[position,"CIK"]
    Ticker = df.at[position,"Ticker"]

    new_CIK = TenDigitsCik(CIK)
    
    new_url = ChangeUrl(new_CIK)
    
    new_page = requests.get(new_url)

    call_status = new_page.status_code

    while call_status != 200 :
        time.sleep(1/5)
        new_page = requests.get(new_url)

        call_status = new_page.status_code
        print('error')
        if call_status == 200 :
            page_to_json = new_page.json()
            
            filings = page_to_json['filings']['recent']

            # fields = 'accessionNumber' , 'filingDate', 'reportDate', 'form', 'primaryDocument', 'primaryDocDescription'

            # accessionNumber = filings['accessionNumber']
            # filingDate = filings['filingDate']
            # reportDate = filings['reportDate']
            # form = filings['form']
            # primaryDocument = filings['primaryDocument']
            # primaryDocDescription = filings['primaryDocDescription']


            dataframe = pd.DataFrame(filings) 
            company_filings_csv = dataframe.to_csv(Ticker+'.csv')

            print('listo')


        
        