#Contains all what is dynamic

datapath = "development/data/iris.csv"
data_base = "sqlite:///data.db"
modeloutput = "development/artifacts/model.pkl"
rawfields = ["Sepal_Length", "Sepal_Width", "Petal_Length", "Petal_Width"]
target = "Class"
testsize = 0.3
randomstate = 50