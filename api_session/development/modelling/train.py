import pandas as pd
from development.common_util.config import data_base, rawfields, \
    target, testsize, randomstate, modeloutput
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
import pickle
import sys,os
from sqlalchemy import create_engine



import os
cwd = os.getcwd()
print(cwd)

engine = create_engine(data_base)

# Load training data  from DB
df = pd.read_sql('training_data', engine)

# Select independent and dependent variable
X = df[rawfields]
y = df[target]

print(df)
# Split the dataset into train and test
X_train, X_test, y_train, y_test = train_test_split(X, y,
                                    test_size=testsize, random_state=randomstate)

# Instantiate the model
classifier = RandomForestClassifier()

# Fit the model
classifier.fit(X_train, y_train)

# Make pickle file of our model
pickle.dump(classifier, open(modeloutput, "wb"))

#Load the saved model
model = pickle.load(open(modeloutput, "rb"))

#Predictions
output = model.predict(X_test)
print(output)