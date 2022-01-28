from sqlalchemy import create_engine
from development.common_util.config import data_base, rawfields, \
    target, testsize, randomstate, modeloutput
import pickle
import pandas as pd

import os
cwd = os.getcwd()

#Load the saved model
model = pickle.load(open(modeloutput, "rb"))

# engine = create_engine(data_base)

# Load training data  from DB
df = pd.read_sql('inference_table', engine)

X_test = df[rawfields]

#Predictions
df[target] = model.predict(X_test)

# #load predictions to back to table
# df.to_sql('inference_data', engine)

