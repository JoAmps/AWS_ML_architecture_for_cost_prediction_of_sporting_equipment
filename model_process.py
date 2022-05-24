from preprocessing import datetime, read_dataset, find_season, create_weekday, scale_outliers, drop
import pandas as pd
import numpy as np

from sklearn.metrics import mean_absolute_error, mean_squared_error
from sklearn.model_selection import train_test_split
from lightgbm import LGBMRegressor

import logging


def split_data(df,test_size,valid_size):
    X = df.drop(columns=['estimated_spending'])
    y = df['estimated_spending']
    X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=test_size,random_state=0)
    X_train,X_valid,y_train,y_valid=train_test_split(X_train,y_train,test_size=valid_size,random_state=0)
    return X_train,X_valid,y_train,y_valid,X_test,y_test
 

def one_hot_encode(df):
    df=pd.get_dummies(df)
    return df

def train_model(X_train, y_train):
    model = LGBMRegressor(random_state=0)
    model.fit(X_train, y_train)
    return model

def predict(X_test, model):
    predictions = model.predict(X_test)
    return predictions


#def evaluate_model(y_test, predictions):
   # mean_absolute_error = mean_absolute_error(y_test, predictions)
  #  mean_squared_error = mean_squared_error(y_test, predictions) 
   # print(mean_absolute_error)
    

