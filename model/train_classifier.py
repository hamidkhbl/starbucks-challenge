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
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score

def load_data():
    '''
    '''
    engine = create_engine('sqlite:///data/starbucks.sqlite')
    person_offer = pd.read_sql_table('person_offer', engine)
    profile = pd.read_sql_table('profile', engine)
    portfolio = pd.read_sql_table('portfolio', engine)

    return person_offer.merge(profile, on= 'person_id')

def split_data(person_offer):
    '''
    '''
    X = person_offer[['age','gender', 'income']]
    y = person_offer ['event_offer_completed']
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state=42)
    return X_train, X_test, y_train, y_test

def train_model(X_train, y_train):
    '''
    '''
    model = RandomForestClassifier()
    model.fit(X_train, y_train)
    return model

def predict(X_test, model):
    '''
    '''
    pred = model.predict(X_test)
    return pred

def main():
    data = load_data()
    X_train, X_test, y_train, y_test = split_data(data)
    model = train_model(X_train, y_train)
    pred = predict(X_test, model)
    print(accuracy_score(y_test, pred))
    print(X_test.head(1))
    print(predict(X_test.head(1), model))


if __name__ == "__main__":
    main()


# %%
