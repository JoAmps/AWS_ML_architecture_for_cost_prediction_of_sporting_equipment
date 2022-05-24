import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from preprocessing import datetime, read_dataset, find_season, create_weekday, scale_outliers, drop
import os
from joblib import dump
import json
from model_process import split_data, one_hot_encode, train_model, predict


if __name__ == '__main__':
    df = read_dataset('data/costs.csv')
    df=datetime(df)
    season_list = []
    for month in df['month']:
        season = find_season(month)
        season_list.append(season)
    df['seasons'] = season_list
    df=create_weekday(df)
    df=scale_outliers(df)
    df=drop(df)

    X_train,X_valid,y_train,y_valid,X_test,y_test=split_data(df,0.15,0.2)  
    X_train=one_hot_encode(X_train)
    X_valid=one_hot_encode(X_valid)
    X_test=one_hot_encode(X_test)

    model= train_model(X_train, y_train)
    dump(model, 'model.joblib')

