from io import BytesIO
from urllib.request import urlopen
import pandas as pd
import sqlite3
from numpy import arange
from sklearn.linear_model import MultiTaskLassoCV
from sklearn.model_selection import RepeatedKFold
import zipfile as zpf
import joblib

def MTLassoCV(userData):
    dataKeys = ["CPU cores", "CPU capacity provisioned [MHZ]", "CPU usage [%]", "Memory capacity provisioned [KB]", "Memory usage [KB]"]
    formKeys = ['amt_CPU', 'amt_vCPU', 'prcnt_CPU', 'amt_Memory', 'prcnt_Memory']
    url = 'https://github.com/sevaiq/Datacenter_dataset/raw/master/Datacenter%20dataset.zip'
    responce = urlopen(url)
    zp = zpf.ZipFile(BytesIO(responce.read()))
    dfList = []
    for filename in zp.namelist():
        df = pd.read_csv(zp.open(filename), sep=';', index_col=None, header=0)
        df.rename(columns=lambda x: x.strip(), inplace=True)
        df.drop(df[df['CPU cores'] == 0].index, inplace=True)
        df.drop(df[df['CPU usage [%]'] < 1].index, inplace=True)
        dfList.append(df)
    fullData = pd.concat(dfList, axis=0, ignore_index=True)
    df = fullData.sample(n=500)
    print ("Training Data Loaded")
    data = df[dataKeys]
    #define cross-validation method to evaluate model
    cv = RepeatedKFold()
    model = MultiTaskLassoCV(cv=cv, n_jobs=-1)
    print ("MultiTaskLassoCV Loaded")

    for key1, key2 in zip(dataKeys, formKeys):
        userData[key1] = userData.pop(key2)
    '''
    userData['CPU cores'] = userData.pop('amt_CPU')
    userData['CPU capacity provisioned [MHZ]'] = userData.pop('amt_vCPU')
    userData['CPU usage [%]'] = userData.pop('prcnt_CPU')
    userData['Memory capacity provisioned [KB]'] = userData.pop('amt_Memory')
    userData['Memory usage [KB]'] = userData.pop('prcnt_Memory')
    '''  
    non_empty_keys = [key for key, value in userData.items() if value]
    empty_keys = [key for key, value in userData.items() if not value]
    print(non_empty_keys)
    print (empty_keys)

    x = data[non_empty_keys]
    y = data[empty_keys]
    model.fit(x.values,y.values)
    print ("MultiTaskLassoCV Fitted")
    
    inputData = {}
    predictData = {}
    for key in non_empty_keys:
        inputData[key] = userData[key]
        predictData[key] = userData[key]
    print(inputData)
    prediction = model.predict([list(inputData.values())])
    i = 0
    for key in empty_keys:
        predictData[key] = round(prediction[0][i],2)
        i+=1
    for key1, key2 in zip(dataKeys, formKeys):
        predictData[key2] = predictData.pop(key1)
    print(predictData)
    '''

    predictData = inputData.update(outputData)
    
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
    '''
    print ("\nDone.")
    return predictData



def main():
    testLassoCV()

if __name__ == "__main__":
    main()


