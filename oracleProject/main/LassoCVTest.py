import pandas as pd
from numpy import arange
from sklearn.linear_model import LassoCV
from sklearn.model_selection import RepeatedKFold

def testLassoCV():
    #specify URL where data is located
    url = "https://raw.githubusercontent.com/Statology/Python-Guides/main/mtcars.csv"
    wildfiredb = "F:\wildfiredb.csv"

    #read in data
    data_full = pd.read_csv(url)
    dbdata = pd.read_csv(wildfiredb, nrows = 10)

    #select subset of data
    data = data_full[["mpg", "wt", "drat", "qsec", "hp"]]
    #firedata = dbdata[[""]]

    #view first six rows of data
    data[0:6]

    #define predictor and response variables
    X = data[["mpg", "wt", "drat", "qsec"]]

    y = data["hp"]

    #define cross-validation method to evaluate model
    #n_splits is # of folds, n_repeats is # of times cross validator needs to be repeated, random state cpntrols randomness of each cycle
    cv = RepeatedKFold(n_splits=10, n_repeats=3, random_state=1)

    #define model
    model = LassoCV(alphas=None, cv=cv, n_jobs=1)

    #fit model
    model.fit(X.values, y.values)

    #display lambda that produced the lowest test MSE
    #print(model.alpha_)

    #define new observation
    new = [24, 2.5, 3.5, 18.5]

    #predict hp value using lasso regression model
    prediction = model.predict([new])
    returnDict = {'ex': data.to_string(), 'predictor': new, 'response': prediction}
    return (returnDict)