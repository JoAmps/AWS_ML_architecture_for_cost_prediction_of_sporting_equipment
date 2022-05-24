import streamlit as st
import requests


def run():
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
    number_of_items_bought = st.slider('How many items do you want?', 1, 500, 25)
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

    if st.button("Predict"):
        response = requests.post("https://dhnqhr011c.execute-api.us-east-1.amazonaws.com/test/cost-prediction-sporting-equipment", json=data)
        prediction = response.text
        st.success(f"The estimated amount of money to be spent is : {prediction}")


if __name__ == '__main__':
    run()