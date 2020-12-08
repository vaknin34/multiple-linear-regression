# -*- coding: utf-8 -*-
"""
Created on Thu Dec  3 20:14:55 2020

@author: vakni
"""

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder
import numpy as np

class DataPreProcessing():
    
    def __init__(self,csvfilename):
        self.df = pd.read_csv(csvfilename)
        self.x_list = []
        self.catgory_flag = 0
    
    def preprocess(self):
        col_list = self.getTitel()
        size_of_x =  int(input("please choose Amount of  x Feature column  "))
        for i in range(size_of_x):
            self.build_x(col_list)
        x = self.buildDataSet()
        x = self.fix_catgory(x)
        self.target_y = int(input("please choose target y column number  "))
        self.target_y = col_list[self.target_y]
        y = self.df[self.target_y].values
        x_train,x_test,y_train,y_test = train_test_split(x,y,test_size = 0.2,random_state = 0)
        self.x_train = x_train
        self.x_test = x_test
        self.y_train = y_train
        self.y_test = y_test
        
    def getTitel(self):
        col_list = list(self.df.columns)
        for i in range(len(col_list)):
            print(str(i) + " : " + col_list[i])
        return col_list
    
    def build_x(self,col_list):
        self.feature_x = int(input("please choose feature x column number  "))
        self.feature_x = col_list[self.feature_x]
        x = self.df[self.feature_x].values
        self.x_list.append((self.feature_x ,x))
        
    def buildDataSet(self):
        table = pd.DataFrame()
        for pair in self.x_list:
            table[pair[0]] = pair[1]
        return table
    
    def fix_catgory(self,x):
        size_of_catgory =  int(input("please choose Amount of catgory Features  "))
        old_size = len(x.columns)
        hlp = 0
        for i in range(size_of_catgory):
            catgory_index = int(input("please choose feature x column number  "))
            self.catgory_name =  list(x.columns)[catgory_index]
            self.catgory_flag = 1
            ct = ColumnTransformer(transformers=[('encoder', OneHotEncoder(), [catgory_index+hlp])], remainder='passthrough')
            x = np.array(ct.fit_transform(x))
            x=pd.DataFrame(x)
            hlp += len(x.columns) - old_size
            old_size = len(x.columns)
            self.user_size = old_size
        return x
            
        
        
        
    
    
            
        
        




















