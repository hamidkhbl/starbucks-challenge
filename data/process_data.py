import pandas as pd
import numpy as np
import math
import json

# read in the json files
portfolio = pd.read_json('data/portfolio.json', orient='records', lines=True)
profile = pd.read_json('data/profile.json', orient='records', lines=True)
transcript = pd.read_json('data/transcript.json', orient='records', lines=True)

# map encoded columns to ids
def column_mapper(column):
    coded_dict = dict()
    cter = 1
    encoded = []
    
    for val in column:
        if val not in coded_dict:
            coded_dict[val] = cter
            cter+=1
        
        encoded.append(coded_dict[val])
    return encoded

# convert value (json column) to multiple columns in transcript df
transcript = pd.concat([transcript, transcript['value'].apply(pd.Series)], axis=1)
del transcript['value']

# rename columns 
portfolio.rename(columns = {'id':'portfolio_id'}, inplace = True)
profile.rename(columns = {'id':'person_id'}, inplace = True)
transcript.rename(columns = {'offer_id':'offer_id_2','offer id':'offer_id','person':'person_id'}, inplace = True)

df = profile.merge(transcript, on = 'person_id', how='right').merge(portfolio, how='left', left_on='offer_id', right_on = 'portfolio_id')

# map encoded columns to ids for all dfs
# transcript.person = column_mapper(transcript.person)