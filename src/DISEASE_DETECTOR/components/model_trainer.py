import os
import sys
from dataclasses import dataclass
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC
from sklearn.tree import DecisionTreeClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.neighbors import KNeighborsClassifier
from DISEASE_DETECTOR.utils import save_object, evaluate_model
from DISEASE_DETECTOR.logger import logging
import random
from DISEASE_DETECTOR.exception import CustomException





@dataclass
class ModelTrainerConfig:
    logging.info('creating file path for the model')
    trained_model_file_path:str = os.path.join('artifacts', "model.pkl")

class ModelTrainer:
    logging.info('initializing the path inside the model trainer class')
    def __init__(self):
        self.model_trainer_config = ModelTrainerConfig()
    
    def initiate_model_trianer(self, feature_array, target_data):
        logging.info('model_trainer initiated')
        try:
            logging.info('data splitting into train and test')
            X_train, X_test, y_train, y_test = train_test_split(feature_array, target_data, test_size=0.2, random_state=42)

            logging.info('models selection and defination')
            models = {

                "Logistics Regression": LogisticRegression(),
                "Support Vector Classifier": SVC(),
                "Decision Tree Classifier": DecisionTreeClassifier(),
                "Gussian Naive Baiye": GaussianNB(),
                "KNN Classifier": KNeighborsClassifier()
            }

            logging.info('model training and performance report')
            model_report,  models_list  = evaluate_model(models=models, X_train=X_train, y_train=y_train, X_test=X_test, y_test=y_test)
            print(model_report)
            logging.info(f'{model_report} ')

            logging.info('Since the models all have a perfect performnance we will select one to use at random')
            selected_model = random.choice(models_list)

            save_object(file_path=self.model_trainer_config.trained_model_file_path, obj=selected_model)


        except Exception as e:
            raise CustomException(e, sys)