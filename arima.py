# -*- coding: utf-8 -*-
"""
Created on Sat May 06 04:42:44 2017

@author: sara
"""

import pandas as pd
import glob
from sklearn.metrics import mean_squared_error
from math import sqrt
from pandas import datetime
#from matplotlib import pyplot
from statsmodels.tsa.arima_model import ARIMA
import numpy as np


def parser(x):
      return datetime.strptime(x, '%Y-%m-%d %H:%M:%S')
      

def file_name():
    p="/*.2xlarge_linux"
    mypath=r'2x'
    allFiles = glob.glob(mypath + p)
    result=list()
    traning=list()
    file_list=list()
    for files in allFiles:
        FilesName=files.split('.')
        FileName=FilesName[0]
        readfiles= pd.read_csv(files ,header =0 ,parse_dates=[0], index_col=0,squeeze=True, date_parser=parser)
        df=readfiles.values
        train=df[:2879]
        until= len(df)-12
        sumArmse=list()
        sumtraning=list()
        for _ in df:
           train=df[:len(train)+1]
           test = df[len(train):len(train)+12]   
           if len(train) == until:
                break
           history = [x for x in train]
           model = ARIMA(history, order=(0,1,1)).fit(disp=0)
           print len(train)
           history.pop(0)
           train_output=np.asarray(model.fittedvalues)
           history=np.asarray(history)
           traning_error=sqrt(mean_squared_error(history, train_output))

           sumtraning.append(traning_error)
           output = model.forecast(steps=12) 
           yhat= output[0]
           rmse = sqrt(mean_squared_error(test, yhat))
           sumArmse.append(rmse)
        result_ave = np.average(sumArmse)
        result.append(result_ave)
        result_train=np.average(sumtraning)
        traning.append(result_train)
        file_list.append(FileName)  

        with open('2xrmse/m011output.txt', 'w') as outfile:
            for i  in range(len(result)) :

                    out_list =" "
                    out_list +=  file_list[i] + ", the RMSE is : " + str(result[i]) +"training error : "+ str(traning[i])
                    out_list += "\n"
                    outfile.write( out_list )
            outfile.close()

file_name()

