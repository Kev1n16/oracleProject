import pandas as pd
import sqlite3
from numpy import arange
from sklearn.linear_model import MultiTaskLassoCV
from sklearn.model_selection import RepeatedKFold
import zipfile as zpf

def testLassoCV():
    #TODO: DELETE EXAMPLE
    '''
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

    #connect to SQLITE db
    #con = sqlite3.connect("C:\\Users\\blast\\Desktop\\oracle\\oracleProject\\oracleProject\\db.sqlite3")
    #cur = con.cursor()
    #load example data
    print("DB Data")
    #cur.execute("DELETE FROM main_flavor")

    cur.execute("""
                INSERT INTO main_flavor
                (name, id, amt_vCPU, amt_Memory, amt_Volume, amt_Ephemeral_Volume)
                VALUES
                ('Flavor1', 1, 2, 8, 50, 100),
                ('Flavor2', 2, 4, 16, 100, 200),
                ('Flavor3', 3, 8, 32, 200, 500),
                ('Flavor4', 4, 16, 64, 500, 1000),
                ('Flavor5', 5, 32, 128, 1000, 2000),
                ('Flavor6', 6, 4, 12, 75, 50),
                ('Flavor7', 7, 8, 20, 225, 100),
                ('Flavor8', 8, 16, 36, 550, 500),
                ('Flavor9', 9, 32, 68, 1250, 1000)
                """)
    #table to pandas dataframe
    df = pd.read_sql_query("""SELECT * from main_flavor
                            ORDER BY amt_vCPU""", con)
    '''
    zp = zpf.ZipFile('C:\\Users\\blast\\Desktop\\oracle\\datacenter_dataset.zip')
    dfList = []
    for filename in zp.namelist():
        df = pd.read_csv(zp.open(filename), sep=';', index_col=None, header=0)
        df.rename(columns=lambda x: x.strip(), inplace=True)
        df.drop(df[df['CPU cores'] == 0].index, inplace=True)
        df.drop(df[df['CPU usage [%]'] < 1].index, inplace=True)
        dfList.append(df)
    fullData = pd.concat(dfList, axis=0, ignore_index=True)
    df = fullData.sample(n=500)
    #print (df)
    data = df[["CPU cores", "CPU capacity provisioned [MHZ]", "CPU usage [%]", "Memory capacity provisioned [KB]", "Memory usage [KB]"]]
    #define cross-validation method to evaluate model
    cv = RepeatedKFold()
    model = MultiTaskLassoCV(cv=cv, n_jobs=-1)
    #TODO train model on full data and save to file
    '''
    filename = 'finalized_model.sav'
    pickle.dump(model, open(filename, 'wb'))
    '''
    X = data[["CPU usage [%]", "Memory usage [KB]"]]
    testData = [50, 4194304]
    y = data[["CPU cores", "CPU capacity provisioned [MHZ]", "Memory capacity provisioned [KB]"]]
    model.fit(X.values, y.values)

    prediction = model.predict([testData])
    formatData = {
        "CPU cores":round(prediction[0][0]),
        "CPU capacity provisioned [MHZ]":round(prediction[0][1],2),
        "CPU capacity provisioned [GHZ]":round(prediction[0][1]/1000,2),
        "CPU usage [%]":testData[0],
        "Memory capacity provisioned [KB]":round(prediction[0][2],2),
        "Memory capacity provisioned [GB]":round(prediction[0][2]/1e+6,2),
        "Memory usage [KB]":testData[1],
        "Memory usage [GB]":round(testData[1]/1e+6,2),
    }

    for item in formatData:
        print(item + ": " + str(formatData[item]))

    print ("\nDone.")


def main():
    testLassoCV()

if __name__ == "__main__":
    main()


