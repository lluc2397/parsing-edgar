import requests
import pandas as pd
from bs4 import BeautifulSoup as bs
import time

#User Agent info
headers = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
    
    'Accept-Encoding': 'gzip, deflate'
}


#get ticker and companies cik
tck_cik_list = pd.read_csv('tck_cik_list.csv')



#get the list of all filings of the company
def ChangeFilingsUrl(search_ticker):
    url = f'https://data.sec.gov/submissions/CIK{search_ticker}.json'
    
    return url



#change current company cik to tendigits cik
def TenDigitsCik(current_cik):
    CIK_str = str(current_cik)

    cik_length = len(CIK_str)

    if cik_length == 10 :
        new_cik = CIK_str
    else :
       new_cik = CIK_str.zfill(10)
    return new_cik




#look for each company in the csv and get the url with all docs
for company in range(0, 1):

    CIK = tck_cik_list.at[company,"CIK"]
    Ticker = tck_cik_list.at[company,"Ticker"]

    new_CIK = TenDigitsCik(CIK)
    
    new_url = ChangeFilingsUrl(new_CIK)
    
    new_page = requests.get(new_url, headers=headers)
    
    call_status = new_page.status_code
    
    while call_status != 200 :
        time.sleep(1/5)
        new_page = requests.get(new_url, headers=headers)
        
        call_status = new_page.status_code
        
    if call_status == 200 :
        
        page_to_json = new_page.json()
        
#retreive all docs info from api
        all_filings_in_json = page_to_json['filings']['recent']
        

        all_filings_in_dataframe = pd.DataFrame(all_filings_in_json) 
        
        #get all reports form 
        filings_form = all_filings_in_dataframe['form']
        
        #if form match get accessionnumber
        for i, file in enumerate(filings_form):
            if file == '10-K':
                filing_accessionNumber = all_filings_in_dataframe.at[i,"accessionNumber"].replace("-","")
                print(Ticker)
                print(CIK)
                print(filing_accessionNumber)







                income_statement_part_url = f'https://www.sec.gov/Archives/edgar/data/{CIK}/{filing_accessionNumber}/R2.htm'
                balance_sheet_part_url = f'https://www.sec.gov/Archives/edgar/data/{CIK}/{filing_accessionNumber}/R3.htm'
                cashflow_statement_part_url = f'https://www.sec.gov/Archives/edgar/data/{CIK}/{filing_accessionNumber}/R7.htm'

                

                # income_statement_clean = pd.read_html(requests.get(income_statement_part_url, headers=headers).content)[0]
                # balance_sheet_clean = pd.read_html(requests.get(balance_sheet_part_url, headers=headers).content)[0]
                cashflow_statement_clean = pd.read_html(requests.get(cashflow_statement_part_url, headers=headers).content)[0]
                print(cashflow_statement_clean.columns)
                # balance_sheet_clean = pd.read_html(requests.get(balan_sh_url, headers=headers).content)[0]

                # new_is=income_statement_clean.columns.droplevel(0)
                # new_bs=balance_sheet_clean.columns.droplevel(0)
                new_cs=cashflow_statement_clean.columns.droplevel(0)

                # income_statement_clean.columns = new_is
                # balance_sheet_clean.columns = new_bs
                cashflow_statement_clean.columns = new_cs

                print(cashflow_statement_clean.columns)
                