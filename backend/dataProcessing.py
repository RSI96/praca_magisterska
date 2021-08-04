import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from sklearn import preprocessing
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression



def get_column_names(file_name):
    df = pd.read_csv('/usr/src/app/uploadeddata/'+file_name)
    list_of_column_names = list(df.columns)
    return list_of_column_names

def rainTomorow(column_name):
    df=pd.read_csv('/usr/src/app/uploadeddata/weatherAUS.csv')
    
    # Dropping the missing values from the dataset
    df.dropna(inplace=True)

    df["Date"] = pd.to_datetime(df["Date"], format = "%Y-%m-%d", errors = "coerce")

    # Mapping Yes:1, No:0

    df['RainTomorrow'] = df['RainTomorrow'].map({'Yes': 1, 'No': 0})
    df['RainToday'] = df['RainToday'].map({'Yes': 1, 'No': 0})

    #Label Encoding the non-numeric variables
    le = preprocessing.LabelEncoder()
    df['Location'] = le.fit_transform(df['Location'])
    df['WindDir9am'] = le.fit_transform(df['WindDir9am'])
    df['WindDir3pm'] = le.fit_transform(df['WindDir3pm'])
    df['WindGustDir'] = le.fit_transform(df['WindGustDir'])
    
    df.drop("Date", axis=1, inplace=True)

    #Splitting the data into training and test datasets
    #Here, we are trying to predict whether it is going to
    #  Rain tomorrow or not in Australia using the given data. 
    # Hence, the RainTomorrow will be the y label 
    # and rest of the data will be the X or the input data.

    # X data
    X = df.drop("RainTomorrow", axis=1)
    # y data
    y = df["RainTomorrow"]


    X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.2, random_state=42)

    #Training the Model
    #Linear Regression
    lr = LinearRegression()
    lr.fit(X_train, y_train)
    LinearRegressionScore = lr.score(X_test,y_test)

    result = LinearRegressionScore*100
    return result