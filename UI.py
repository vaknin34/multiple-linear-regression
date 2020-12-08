# -*- coding: utf-8 -*-
"""
Created on Thu Dec  3 21:36:11 2020

@author: vakni
"""
# -*- coding: utf-8 -*-
"""
Created on Sat Nov 28 17:32:08 2020

@author: vakni
"""
import DataPreProccessing
import LinearRegModel
import pickle
class UI():
    def greetingUser(self):
        print('Hello User and Welcome to Csv Linear Regressor')
        
    def csvUpload(self):
        self.path = input("please enter Path to File  ")
        self.mainMenu()
        
    def DataPre(self):
        self.Data = DataPreProccessing.DataPreProcessing(self.path)
        self.Data.preprocess()
        self.mainMenu()
        
    def TrainModel(self):
        self.lrm = LinearRegModel.LinearRegModel()
        self.lrm.TrainModel(self.Data.x_train,self.Data.y_train)
        self.lrm.PredictTest(self.Data.x_test,self.Data.y_test)
        self.mainMenu()
        
    def saveModel(self):
        filename = 'Linear_Regressor_model.sav'
        pickle.dump(self.lrm.regressor, open(filename, 'wb'))
        self.mainMenu()
   
    def PredictSample(self):
        values = []
        if self.Data.catgory_flag == 1:
            size = self.Data.user_size
        else:
            size = len(self.Data.x_list)
        while (len(values) != size):
            x = input("please enter one sample in this format type " + str(self.Data.x_train.iloc[0])+"  ").split(" ")
            values = list(map(float, x))
        
        print(self.lrm.regressor.predict([values]))
        self.mainMenu()

     
    def printLine(self):
        print(str(self.lrm.regressor.coef_) + " * Variable + " + str(self.lrm.regressor.intercept_) + " intercept")
        self.mainMenu()
       
   
    def mainMenu(self):
        print('choose 1 for csv upload')
        print('choose 2 for Data PreProcess')
        print('choose 3 for Training The Model')
        print('choose 4 to Save The Model')
        print('choose 5 to Predict One Sample')
        print('choose 6 to get Line Equation')
        print('choose 7 to exit')
        self.getUserInput()
    
    def getUserInput(self):
        x = int(input("plz choose Number "))
        while x < 1 or x > 9:
            print("Worng Number")
            x = int(input("plz choose Number "))
        if x == 1:
            self.csvUpload()
        if x == 2:
            self.DataPre()
        if x == 3:
            self.TrainModel()
        if x == 4:
            self.saveModel()
        if x == 5:
            self.PredictSample()
        if x == 6:
            self.printLine()
        if x == 7:
            print("Thank you for use my program see you next time")
   
            
            
            
            
        
            
            
            
            
            
            
