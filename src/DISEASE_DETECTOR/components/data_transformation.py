import sys
import os
from DISEASE_DETECTOR.exception import CustomException
from DISEASE_DETECTOR.logger import logging
from DISEASE_DETECTOR.utils import save_object
import pandas as pd
from dataclasses import dataclass
from sklearn.preprocessing import OrdinalEncoder



@dataclass
class DataTransformationConfig:
    processor_object_file_path: str = os.path.join('artifacts', "processor.pkl")
    logging.info('Creating data transformation path')


class Data_Transformation:
    def __init__(self):
        self.data_transformation_config = DataTransformationConfig()
        logging.info('Importing the path into the config')

    def get_data_transformer(self):
        try:
            logging.info('defining the processor object')
            processor = OrdinalEncoder()
            return processor

        except Exception as e:
            raise CustomException(e, sys)
        
    def Initiate_data_transformation(self, raw_data_path):
        try:
            logging.info('reading the data into a dataframe')
            df = pd.read_csv(raw_data_path)
            logging.info(f'the column order is {df.columns}')

            logging.info('spliting the data into features and target')
            feature_data = df.drop(columns='prognosis')
            logging.info(f'feature data column order is {feature_data.columns}')
            target_data = df["prognosis"]

            preprocessor_object = self.get_data_transformer()

            logging.info('transforming features data initiated')
            feature_array = preprocessor_object.fit_transform(feature_data)

            logging.info('Applying save_object method from utils')
            save_object(

                file_path = self.data_transformation_config.processor_object_file_path,
                obj = preprocessor_object
                )
            
            logging.info('returning feature arrays and targets for data modelling')
            return( 

                feature_array,
                target_data,
                self.data_transformation_config.processor_object_file_path
                
                )
        
        except Exception as e:
            raise CustomException(e, sys)
    