# -*- coding: utf-8 -*-
"""
Created on Thu Dec  3 20:38:15 2020

@author: vakni
"""

from sklearn.linear_model import LinearRegression
import numpy as np


class LinearRegModel():
    def __init__(self):
        self.regressor = LinearRegression()
    def TrainModel(self,x_train,y_train):
        self.regressor.fit(x_train,y_train)
        
    def PredictTest(self,x_test,y_test):
        self.y_pred =  self.regressor.predict(x_test)
        np.set_printoptions(precision=2)
        print(np.concatenate((self.y_pred.reshape(len(self.y_pred),1), y_test.reshape(len(y_test),1)),1))
        
    
    

















