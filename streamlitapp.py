import streamlit as st
import requests
from model_process import predict
from joblib import load
import numpy as np
import pandas as pd
from model_process import one_hot_encode
from preprocessing import datetime, read_dataset, find_season, create_weekday, scale_outliers, drop


def user_input_features():
    mode_of_purchase = st.selectbox(
            "Select mode of purchase",
            ('order',
            'physical_collection',
            ))
    sporting_equipment = st.selectbox(
            "Select Sporting Equipment",
            ('hiking/trekking',
            'crosstrain',
            'pilates',
            'jog/run',
            'fitness',
            'football',
            'swimming',
            'tennis',
            'yoga',
            'surfing',
            'cycling',
            'diving',
            'basketball',
            'skate/roller',
            'badminton',
            'trail',
            'yoga',
            'triathlon',
            'golf',
            'kayak/sup',
            'ski',
            'table_tennis',
            'others',
            'rugby',
            'sailing',
            'boxing',
            'climbing',
            'squash',
            'volleyball'))
    store = st.selectbox(
            "Select the store",
            ('east', 'west','south'))
    number_of_items_bought = st.slider('How many items do you want?', 1, 300, 25)
    seasons = st.selectbox(
            "Select the Season",
            ('Autumn',
            'Summer',
            'Spring',
            'Evening',
            'Winter'))
    weekday = st.selectbox(
            "Select Weekday/Weekend",
            ('weekday',
            'weekend'))

    data = {
            'mode_of_purchase': mode_of_purchase,
            'sporting_equipment': sporting_equipment,
            'store': store,
            'number_of_items_bought':number_of_items_bought,
            'seasons': seasons,
            'weekday': weekday,
        }
    features = pd.DataFrame(data, index=[0])
    return features

input_df = user_input_features()


# If button is pressed
if st.button("Submit"):
    
# Apply model to make predictions
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
    df = df.drop(columns=['estimated_spending'])
    df = pd.concat([input_df, df], axis=0)
    encode = ['mode_of_purchase', 'sporting_equipment', 'store', 'seasons', 'weekday']
    for col in encode:
        dummy = pd.get_dummies(df[col], prefix=col)
        df = pd.concat([df, dummy], axis=1)
        del df[col]
    df = df[:1]
    df=one_hot_encode(df)
    model=load("model.joblib")
    prediction = model.predict(df)

    # Output prediction
    st.text(f"The estimated amount of money to be spent is :{prediction}")         
