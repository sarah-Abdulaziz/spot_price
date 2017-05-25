# -*- coding: utf-8 -*-
"""
Created on Sun May 21 11:58:57 2017

@author: sara
"""

from pandas import Series
import glob
from sklearn.metrics import mean_squared_error
from math import sqrt
import numpy as np



def file_name():
    p="/*.2xlarge_linux"
    mypath=r'm4'
    allFiles = glob.glob(mypath + p)
    result=list()
    file_list=list()
    for files in allFiles:
        FilesName=files.split('m4')
        FileName=FilesName[1]
        readfiles= Series.from_csv(files ,header =0 )
        df=readfiles.values
        train=df[:2879]
        until= len(df)-12
        sumArmse=list()
        for _ in df:
           train=df[:len(train)+1]
           test = df[len(train):len(train)+12]          
           if len(train) == until:
                break
#           print (FileName,len(train),len(test))
           window = train[-3:]
           mm=np.mean(window)
           predictions =[mm]*12
           rmse = sqrt(mean_squared_error(test, predictions))
           sumArmse.append(rmse)
        result_ave = np.average(sumArmse)
        result.append(result_ave)
        file_list.append(FileName)
        with open(r'Mm3.txt', 'wb') as outfile:
            for i  in range(len(result)) :
                    out_list =" "
                    out_list +=  file_list[i] + ", the RMSE is : " + str(result[i])+"\n"
                    out_list += "\n"
                    outfile.write( out_list )
            outfile.close()

file_name()
