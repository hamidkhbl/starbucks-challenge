#%%
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.naive_bayes import GaussianNB
from sklearn.model_selection import GridSearchCV
from sklearn.model_selection import train_test_split
from sklearn.metrics import f1_score
from sklearn.metrics import accuracy_score
from sqlalchemy import create_engine


def load_all_data():
    '''
    '''
    engine = create_engine('sqlite:///data/starbucks.sqlite')
    profile = pd.read_sql_table('profile', engine)
    portfolio = pd.read_sql_table('portfolio', engine)
    transcript = pd.read_sql_table('transcript', engine)
    return profile, portfolio, transcript


def load_data():
    '''
    '''
    engine = create_engine('sqlite:///data/starbucks.sqlite')
    person_offer = pd.read_sql_table('person_offer', engine)
    portfolio = pd.read_sql_table('portfolio', engine)

    return person_offer.merge(portfolio, on = 'portfolio_id')

def user_offers_history(user_id, person_offer):
    offers = person_offer[person_offer['person_id'] == user_id]
    offers = offers[offers['offer_type'] != 'informational']
    offers = offers.groupby('offer_type').mean()
    offers['completion rate'] = offers['event_offer_completed']/offers['event_offer_received']
    offers['view rate'] = offers['event_offer_viewed']/offers['event_offer_received']
    offers = offers.reset_index()
    print(offers.columns)
    offers = offers[['offer_type','view rate', 'completion rate']]
    return offers

def user_history_analyzer(user_offers_history):
    user_offers_history['view rate']=user_offers_history['view rate'].astype(float)
    user_offers_history['completion rate']=user_offers_history['completion rate'].astype(float)

    dis_com_rate = user_offers_history[user_offers_history['offer_type'] == 'discount']['completion rate'].values
    bogo_com_rate = user_offers_history[user_offers_history['offer_type'] == 'bogo']['completion rate'].values

    dis_view_rate = user_offers_history[user_offers_history['offer_type'] == 'discount']['view rate'].values
    bogo_view_rate = user_offers_history[user_offers_history['offer_type'] == 'bogo']['view rate'].values

    if dis_com_rate > dis_view_rate:
        return 'This user has completed a discount offer without seeing it, so it is better to send them a bogo offer.'
    elif bogo_com_rate > bogo_view_rate:
        return 'This user has completed a bogo offer without seeing it, so it is better to send them a discount offer.'
    elif dis_com_rate > bogo_com_rate:
        return 'It seems this user likes discount offers better.'
    elif dis_com_rate < bogo_com_rate:
        return 'It seems this user likes bogo offers better.'
    else:
        return 'It does not matter which offer you send.'

# %%
