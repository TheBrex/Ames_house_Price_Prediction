import pandas as pd

def delete(variable):
    del variable

def initialize():
    X_train = pd.read_csv('dataset/train_data.csv')   
    X_test = pd.read_csv('dataset/test_data.csv')
    house_df = pd.read_csv('dataset/dataHouse.csv')
    return X_train,X_test,house_df
