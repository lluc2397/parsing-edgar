import json
import pandas as pd


with open('submissions.json') as f:

    data = json.load(f)

del data['cik']
del data['entityType']
del data['sic']
del data['sicDescription']
del data['addresses']

with open('new_sub.json', 'w') as f:

    json.dump(data,f, indent=2)
# filings = data['filings']
print('done')

# df = pd.read_json('submissions.json')
# 
# df.to_csv ('submissions.csv', index = None)