import pandas as pd

def get_column_names(file_name):
    df = pd.read_csv('/usr/src/app/uploadeddata/'+file_name)
    list_of_column_names = list(df.columns)
    return list_of_column_names

