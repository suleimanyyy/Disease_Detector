import os
import sys
from DISEASE_DETECTOR.exception import CustomException
import numpy as np
from DISEASE_DETECTOR.logger import logging
import pandas as pd
import dill
from sklearn.metrics import accuracy_score


def save_object(file_path, obj):
    logging.info('saving object to file_path')
    try:
        dir_name = os.path.dirname(file_path)
        os.makedirs(dir_name, exist_ok=True)

        with open(file_path, 'wb') as file:
            dill.dump(obj, file)


    except Exception as e:
        raise CustomException(e, sys)
    


def evaluate_model(models, X_train, y_train, X_test, y_test):
    logging.info('evaluate model')
    try:

        report = {}
        trained_model_list = []

        for i in range(len(list(models.values()))):
            model = list(models.values())[i]
            model.fit(X_train, y_train)

            

            y_train_pred = model.predict(X_train)
            y_test_pred = model.predict(X_test)


            train_data_acc_score = accuracy_score(y_train, y_train_pred)
            test_data_acc_score = accuracy_score(y_test, y_test_pred)

            report[list(models.keys())[i]] = test_data_acc_score
            trained_model_list.append(model)

        return (report, trained_model_list)
            
    except Exception as e:
        raise CustomException(e, sys)
        