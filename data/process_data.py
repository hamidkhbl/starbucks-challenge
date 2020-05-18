#%%
import pandas as pd
import numpy as np
import math
import json
from sqlalchemy import create_engine

def load_data():
    '''

    '''
    # read in the json files
    portfolio = pd.read_json('data/portfolio.json', orient='records', lines=True)
    profile = pd.read_json('data/profile.json', orient='records', lines=True)
    transcript = pd.read_json('data/transcript.json', orient='records', lines=True)
    return portfolio, profile, transcript

# map encoded columns to ids
def column_mapper(column):
    '''
    '''
    coded_dict = dict()
    cter = 1
    encoded = []

    for val in column:
        if val not in coded_dict:
            coded_dict[val] = cter
            cter+=1

        encoded.append(coded_dict[val])
    return encoded

def clean(portfolio, profile, transcript):
    '''
    '''
    # convert value (json column) to multiple columns in transcript df
    transcript.value = transcript.value.astype(str).replace({'\'': '"'}, regex=True)
    transcript = pd.concat([transcript, pd.json_normalize(transcript.value.apply(json.loads))],axis = 1)
    del transcript['value']

    # rename columns
    portfolio.rename(columns = {'id':'portfolio_id'}, inplace = True)
    profile.rename(columns = {'id':'person_id'}, inplace = True)
    transcript.rename(columns = {'offer id':'portfolio_id','person':'person_id'}, inplace = True)

    # fix became_member_on date format
    profile['became_member_on'] = pd.to_datetime(profile['became_member_on'].astype(str), format='%Y%m%d')

    # fill null values in portfolio_id with offer_id
    transcript['portfolio_id'].fillna(transcript['offer_id'], inplace = True)

    #map portfolio_id
    transcript.portfolio_id = column_mapper(transcript.portfolio_id)

    # merge
    df = profile.merge(transcript, on = 'person_id', how='right').merge(portfolio, how='left', left_on='offer_id', right_on = 'portfolio_id')

    # sort df
    df = df.sort_values(['person_id','time'])

    # map encoded columns to ids
    df.person_id = column_mapper(df.person_id)

    # Add dummy variables for event column
    df = pd.get_dummies(df, columns=['event'])
    df.rename(columns={'event_offer completed':'event_offer_completed',
                    'event_offer received':'event_offer_received',
                    'event_offer viewed':'event_offer_viewed'}, inplace = True)

    # rename reward columns
    df.rename(columns={'reward_x':'offer_reward', 'reward_y':'portfolio_reward'}, inplace = True)
    df.rename(columns={'portfolio_id_x':'portfolio_id', 'reward_y':'portfolio_reward'}, inplace = True)

    # create person_offer dataframe
    person_offer = df.groupby(['person_id','portfolio_id']).sum().reset_index()
    person_offer = person_offer[['person_id', 'portfolio_id', 'event_offer_completed', 'event_offer_received', 'event_offer_viewed']]

    df['channels'] = df['channels'].astype('str')
    return df, person_offer

def save_data(df, person_offer):
    '''

    '''
    engine = create_engine('sqlite:///data/starbucks.sqlite')
    person_offer.to_sql('person_offer', engine, index=False)
    df.to_sql('offer_details', engine, index=False)


def main():

    portfolio, profile, transcript = load_data()
    df, person_offer = clean(portfolio, profile, transcript)
    save_data(df, person_offer)

if __name__ == "__main__":
    main()




# %%
