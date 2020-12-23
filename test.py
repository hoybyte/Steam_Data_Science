from api import get_request
import pandas as pd
import openpyxl



# generate sorted app_list from steamspy data
app_list = steam_spy_all[['appid', 'name']].sort_values('appid').reset_index(drop=True)

# export disabled to keep consistency across download sessions
# app_list.to_csv('../data/download/app_list.csv', index=False)

# instead read from stored csv
# app_list = pd.read_csv('../data/download/app_list.csv')

# display first few rows
