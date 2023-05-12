from io import BytesIO
from urllib.request import urlopen
import pandas as pd
import sqlite3
from numpy import arange
from sklearn.linear_model import MultiTaskLassoCV, RidgeCV, MultiTaskElasticNetCV
from sklearn.model_selection import RepeatedKFold
import zipfile as zpf
import joblib
from sklearn.preprocessing import MinMaxScaler, QuantileTransformer


def machineLearning(userData):
    # attribute keys based on dataset
    dataKeys = ["CPU cores", "CPU capacity provisioned [MHZ]",
                "CPU usage [%]", "Memory capacity provisioned [KB]", "Memory usage [KB]"]
    # attribute keys based on input form
    formKeys = ['amt_CPU', 'amt_vCPU',
                'prcnt_CPU', 'amt_Memory', 'used_Memory']

    # download and clean dataset
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

    # data preprocessing
    mms = MinMaxScaler()
    # minmax scale cpu usage %
    fullData[["CPU usage [%]"]] = mms.fit_transform(
        fullData[["CPU usage [%]"]])

    df = [fullData.sample(n=500), fullData.sample(n=500),
          fullData.sample(n=500)]
    data = [df[0][dataKeys], df[1][dataKeys], df[2][dataKeys]]
    print("Training Data Loaded")
    # define cross-validation method to evaluate model
    cv = RepeatedKFold()
    # load models
    modelMTLassoCV = MultiTaskLassoCV(cv=cv, n_jobs=-1)
    print("MultiTaskLassoCV Loaded")
    modelRidgeCV = RidgeCV(cv=cv)
    print("RidgeCV Loaded")
    modelMTElasticNetCV = MultiTaskElasticNetCV(cv=cv, n_jobs=-1)
    print("MultiTaskElasticNetCV Loaded")

    # convert from input form keys to dataset keys
    for key1, key2 in zip(dataKeys, formKeys):
        userData[key1] = userData.pop(key2)
    # find empty attributes from user input as ML target
    non_empty_keys = [key for key, value in userData.items() if value]
    empty_keys = [key for key, value in userData.items() if not value]
    print(non_empty_keys)
    print(empty_keys)

    # fit training input data and target output data to models
    x = [data[0][non_empty_keys], data[1]
         [non_empty_keys], data[2][non_empty_keys]]
    y = [data[0][empty_keys], data[1][empty_keys], data[2][empty_keys]]
    modelMTLassoCV.fit(x[0].values, y[0].values)
    print("MultiTaskLassoCV Fitted")
    modelRidgeCV.fit(x[1].values, y[1].values)
    print("RidgeCV Fitted")
    modelMTElasticNetCV.fit(x[2].values, y[2].values)
    print("MultiTaskElasticNetCV Fitted")

    # dictionaries of final data for user
    inputData = {}
    predictData = [{}, {}, {}]
    outputData = {}
    # add user input data to dictionaries
    for key in non_empty_keys:
        inputData[key] = userData[key]
        predictData[0][key] = userData[key]
        predictData[1][key] = userData[key]
        predictData[2][key] = userData[key]
    if 'CPU usage [%]' in empty_keys:
        index_prcntCPU = empty_keys.index('CPU usage [%]')

    print("Input:")
    print(inputData)
    predictMTLassoCV = modelMTLassoCV.predict([list(inputData.values())])
    predictMTLassoCV[0][index_prcntCPU] = mms.inverse_transform(predictMTLassoCV)[
        0][index_prcntCPU]
    print("MTLassoCV:")
    print(predictMTLassoCV)
    predictRidgeCV = modelRidgeCV.predict([list(inputData.values())])
    predictRidgeCV[0][index_prcntCPU] = mms.inverse_transform(predictRidgeCV)[
        0][index_prcntCPU]
    print("RidgeCV:")
    print(predictRidgeCV)
    predictMTElasticNetCV = modelMTElasticNetCV.predict(
        [list(inputData.values())])
    predictMTElasticNetCV[0][index_prcntCPU] = mms.inverse_transform(
        predictMTElasticNetCV)[0][index_prcntCPU]
    print("MultiTaskElasticNetCV:")
    print(predictMTElasticNetCV)

    # format predict data into dictionary
    i = 0
    for key in empty_keys:
        valMTLassoCV = round(predictMTLassoCV[0][i], 2)
        valRidgeCV = round(predictRidgeCV[0][i], 2)
        valMTElasticNetCV = round(predictMTElasticNetCV[0][i], 2)
        outputData[key] = round(
            (valMTLassoCV + valRidgeCV + valMTElasticNetCV) / 3, 2)
        i += 1
    # include user input data
    outputData.update(inputData)

    # convert from dataset keys to input form keys
    for key1, key2 in zip(dataKeys, formKeys):
        outputData[key2] = outputData.pop(key1)
    print("Output:")
    print(outputData)
    return outputData


def main():
    machineLearning()


if __name__ == "__main__":
    main()
