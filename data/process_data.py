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

# map encoded columns to ids for all dfs
portfolio.id = column_mapper(portfolio.id)
profile.id = column_mapper(profile.id)
transcript.person = column_mapper(transcript.person)

# convert json column to multiple columns in transcript df
transcript = pd.concat([transcript, transcript['value'].apply(pd.Series)], axis=1)