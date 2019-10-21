import numpy as np
import pandas as pd
import seaborn as sns

from math import sqrt
from sklearn.metrics import mean_squared_error, r2_score, explained_variance_score
from sklearn.linear_model import LinearRegression

def linear_model(X_train, y_train):
    df = pd.DataFrame(y_train)
    lm=LinearRegression()
    lm.fit(X_train,y_train)
    lm_predictions=lm.predict(X_train)
    df['lm']=lm_predictions
    return df

def compute_baseline(y):
    return np.array([y.mean()]*len(y))

def evaluate(actual, model):
    MSE = mean_squared_error(actual, model)
    SSE = MSE*len(actual)
    RMSE = sqrt(MSE)
    r2 = r2_score(actual, model)
    print("MSE: ", MSE, "SSE: ", SSE, "RMSE: ",RMSE, "r^2: ", r2)
    return MSE, SSE, RMSE, r2 
    
def plot_linear_model(actuals, lm, baseline):
    plot = pd.DataFrame({'actual': actuals,
                'lm': lm,
                'baseline': baseline.flatten()})\
    .melt(id_vars=['actual'], var_name='model', value_name='prediction')\
    .pipe((sns.relplot, 'data'), x='actual', y='prediction', hue='model')
    return plot