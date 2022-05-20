import pandas as pd
import numpy as np

def read_dataset(path):
    df=pd.read_csv(path)
    
    return df

def datetime(df):
    df['Date']=pd.to_datetime(df['Date'])
    df['month']=df['Date'].dt.month
    df['day']=df['Date'].dt.day
    return df

def find_season(month):
    season = {12:'Winter', 1:'Winter', 2:'Winter',
            3:'Spring', 4:'Spring', 5:'Spring',
            6:'Summer', 7:'Summer', 8:'Summer',
            9:'Autumn', 10:'Autumn', 11:'Autumn'}
    return season.get(month)

def create_weekday(df):
    df['weekday']=np.where((df['Date'].dt.dayofweek) < 5,'weekday','weekend')  
    return df


def scale_outliers(df):
    UL=np.percentile(df['estimated_spending'], [75])[0] 
    df['estimated_spending'][df['estimated_spending']>3*UL]=3*UL 
    return df

def drop(df):
    df=df[df['sporting_equipment']!='unknown']
    df=df.drop(columns=['day','month','Date'])
    df=df.drop(columns=df.filter(like='Unnamed'))
    #print(df.head())
    return df

    

#if __name__=='__main__':
  #  df=read_dataset('costs.csv')
  #  df=datetime(df)    
  #  season_list = []
   # for month in df['month']:
   #     season = find_season(month)
   #     season_list.append(season)
   # df['seasons'] = season_list
   # df=create_weekday(df)
  #  df=scale_outliers(df)
   # df=drop(df)