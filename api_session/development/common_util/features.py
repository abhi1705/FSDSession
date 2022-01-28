import numpy as np
import pandas as pd
from sklearn.decomposition import PCA
import math

def process(X):
    X['log_Peatal_Width'] = X['Petal_Width'].apply(lambda x: math.log(float(x)))
    return X


def pca(X, pca_components):
    pca = PCA(n_components=pca_components)
    Y = pca.fit_transform(X)
    principalDfs = pd.DataFrame(data = Y, columns = ['PC1', 'PC2'])
    return principalDfs
