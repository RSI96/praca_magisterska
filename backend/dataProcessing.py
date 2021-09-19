import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from sklearn import preprocessing
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
from sklearn.neighbors import KNeighborsClassifier

def primary(x):
    if x in [' 1st-4th', ' 5th-6th', ' 7th-8th', ' 9th', ' 10th', ' 11th', ' 12th']:
        return ' Primary'
    else:
        return x

def get_column_names(file_name):
    df = pd.read_csv('/usr/src/app/uploadeddata/'+file_name)
    list_of_column_names = list(df.columns)
    return list_of_column_names

def runMLAlghoritms(columnName, datasetName, alghoritmName):
    
    df=pd.read_csv('/usr/src/app/uploadeddata/'+datasetName)
    
    # Dropping the missing values from the dataset
    df.dropna(inplace=True)

    if datasetName=='weatherAUS.csv':
        
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

    elif datasetName=='adult.csv':

        df.replace(' ?', np.nan, inplace=True)
        df['incomeBracket'] = df['incomeBracket'].apply(lambda x: 1 if x==' >50K' else 0)
        df['race'] = df['race'].map({' White': 1, ' Black': 0, ' Other': 2, ' Asian-Pac-Islander': 3, ' Amer-Indian-Eskimo': 4})
        df['workclass'].fillna(' 0', inplace=True)
        df['fnlwgt'] = df['fnlwgt'].apply(lambda x: np.log1p(x))
        df['education'] = df['education'].apply(primary)
        df['occupation'].fillna(' 0', inplace=True)
        df['nativeCountry'].fillna(' 0', inplace=True)
        categorical_features = df.select_dtypes(include=['object']).axes[1]
        for col in categorical_features:
            df = pd.concat([df, pd.get_dummies(df[col], prefix=col, prefix_sep=':')], axis=1)
            df.drop(col, axis=1, inplace=True)

    elif datasetName=='ChurnModelling.csv':

        le = preprocessing.LabelEncoder()
        df.drop(labels = ["RowNumber", "CustomerId","Surname"], axis = 1, inplace = True) 

        df['Geography'].replace("France",1,inplace= True)
        df['Geography'].replace("Spain",2,inplace = True)
        df['Geography'].replace("Germany",3,inplace=True)
        df['Gender'].replace("Female",0,inplace = True)
        df['Gender'].replace("Male",1,inplace=True)
        
    elif datasetName=='winequalityN.csv': 

        df['type'].replace("white",1,inplace= True)
        df['type'].replace("red",0,inplace= True)



    #Splitting the data into training and test datasets
    # X data
    X = df.drop(columnName, axis=1)
    # y data
    y = df[columnName]

    X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.2, random_state=42)

    result = 0

    if alghoritmName=='LinearRegression':
        #Training the Model
        #Linear Regression
        lr = LinearRegression()
        lr.fit(X_train, y_train)
        LinearRegressionScore = lr.score(X_test,y_test)
        ypred = lr.predict(X_test)
        result = LinearRegressionScore*100

    elif alghoritmName=='RandomForestRegressor':
        #Random Forest Regressor
        rf = RandomForestRegressor(n_estimators = 100, random_state = 0)
        rf.fit(X_train,y_train)
        RandomForestRegressorScore = rf.score(X_test,y_test)
        ypred = rf.predict(X_test)
        result = RandomForestRegressorScore*100

    elif alghoritmName=='KNeighborsClassifier':
        #KNeighbors Classifier
        knn = KNeighborsClassifier(4)
        knn.fit(X_train,y_train)
        KNeighborsClassifierScore = knn.score(X_test,y_test)
        ypred = knn.predict(X_test)
        result = KNeighborsClassifierScore*100

    return result, y_test, ypred