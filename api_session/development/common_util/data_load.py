import pandas as pd 
import sklearn
from sqlalchemy import create_engine

engine = create_engine("sqlite:///data.db")

# load data from file
df = pd.read_csv('development\data\iris.csv')

training_data = df[:100]
inference_data = df[100:]

training_data.to_sql('training_data', if_exists='replace')

inference_data =  inference_data.drop('Class', axis=1)
inference_data.to_sql('inference_table', engine, if_exists='replace')