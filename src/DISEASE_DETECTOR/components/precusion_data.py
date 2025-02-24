import numpy as np
import pandas as pd
import matplotlib.pyplot as plt



class Precausion:
    def __init__(self):
        pass


    def precausion_list(self, prediction:str):
        df = pd.read_csv("research\data\Disease precaution.csv")
        symptoms_list = ['Malaria', 'Migraine', 'Typhoid', 'Pneumonia', 'Chronic cholestasis']
        for i in symptoms_list:
            if i == prediction:
                causion = df[df['Disease'] == prediction]
                c1 = causion["Precaution_1"]
                c2 = causion["Precaution_2"]
                c3 = causion["Precaution_3"]
                c4 = causion["Precaution_4"]
        print(c1.values, c2.values, c3.values, c4.values)
        return (c1.values, c2.values, c3.values, c4.values)