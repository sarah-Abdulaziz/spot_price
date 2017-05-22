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
import matplotlib.pylab as plt
from matplotlib.pylab import rcParams
rcParams['figure.figsize'] = 15, 6

def file_name():
    p="/*_m4.2xlarge_linux"
    mypath=r'2x'
    allFiles = glob.glob(mypath + p)
    result=list()
    traning=list()
    file_list=list()
    for files in allFiles:
        FilesName=files.split('.')
        FileName=FilesName[0]
        readfiles= pd.read_csv(files , names=['Date','values'])
        readfiles['Date'] = pd.to_datetime(readfiles['Date'])
        indexed_df = readfiles.set_index('Date')  
        df = indexed_df['values']
#        print (ts.head(5))
         df_week = df.resample('W').mean()
        for _ in df:
              df_week = df.resample('W').mean()
              plt.plot(df_week)
##        df=readfiles.values
#        train=df[:2879]
#        until= len(df)-12
#        sumArmse=list()
#        sumtraning=list()
#        for _ in df:
#           train=df[:len(train)+1]
#           test = df[len(train):len(train)+12]   
#           if len(train) == until:
#                break
#           history = [x for x in train]
#           model = ARIMA(history, order=(2,1,0)).fit(disp=1)
##           history.pop(0)
##           train_output=np.asarray(model.fittedvalues)
#           train_output=pd.Series(model.fittedvalues)
#           print train_output
#           history=np.asarray(history)
#           traning_error=sqrt(mean_squared_error(history, train_output))
#
#           sumtraning.append(traning_error)
#           output = model.forecast(steps=12) 
#           yhat= output[0]
#
#           rmse = sqrt(mean_squared_error(test, yhat))
#           sumArmse.append(rmse)
##           print('Test RMSE: %.3f' % rmse, FileName)
###        print (FilesName[1],sumArmse)
#        result_ave = np.average(sumArmse)
#        result.append(result_ave)
#        result_train=np.average(sumtraning)
#        traning.append(result_train)
#        file_list.append(FileName)  
##        print (FileName,'Test RMSE resuult: ', result,"tran error",traning )
#        with open('2xrmse/T_Tm011output210.txt', 'w') as outfile:
#            for i  in range(len(result)) :
##                for k in  range(len(traning)):
#                    out_list =" "
#                    out_list +=  file_list[i] + ", the RMSE is : " + str(result[i]) +"training error : "+ str(traning[i])
#                    out_list += "\n"
#                    outfile.write( out_list )
#            outfile.close()

file_name()

