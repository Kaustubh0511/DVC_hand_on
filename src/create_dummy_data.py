import pandas as pd
from sklearn.datasets import load_iris

def create_dummy_data():
    # Load the Iris dataset
    iris = load_iris(as_frame=True)
    
    # Create a DataFrame from the dataset
    df = iris.frame

    #path to save df in
    df.to_csv('data/raw/iris.csv', index=False)

if __name__ == "__main__": 
    create_dummy_data()