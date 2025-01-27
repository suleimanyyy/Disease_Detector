import sys
import os
from DISEASE_DETECTOR.exception import CustomException
from DISEASE_DETECTOR.logger import logging
import pandas as pd
from dataclasses import dataclass

@dataclass
class DataIngestionConfig:
    raw_data_path:str = os.path.join('artifacts', "data.csv")


class DataIngestion:
    def __init__(self):
        self.data_ingestion_config = DataIngestionConfig()

    def Initiate_data_ingestion(self):
        logging.info('entered the data ingestion method or component')
        try:
            df = pd.read_csv('research\data\symbipredict_2022.csv')
            logging.info('read the complete data saved as a dataframe')

            maleria = df["prognosis"] == 'Malaria'
            Migraine = df["prognosis"] == 'Migraine'
            Typhoid = df["prognosis"] == 'Typhoid'
            Pneumonia = df["prognosis"] == 'Pneumonia'
            Cholestasis = df["prognosis"] == 'Chronic Cholestasis'

            logging.info('since we are going concerntrating on five illnesses we will narrow the dataframe to all five illnesses')

            mal_symp = [col for col in df.columns.drop('prognosis') if df[maleria][col].sum()>0]
            typh_symp = [col for col in df.columns.drop('prognosis') if df[Typhoid][col].sum()>0]
            mig_symp = [col for col in df.columns.drop('prognosis') if df[Migraine][col].sum()>0]
            pneum_symp = [col for col in df.columns.drop('prognosis') if df[Pneumonia][col].sum()>0]
            choles_symp = [col for col in df.columns.drop('prognosis') if df[Cholestasis][col].sum()>0]

            logging.info('getting the symptoms from the dataframe')
            dd1 = mal_symp + typh_symp + pneum_symp + mig_symp + choles_symp
            symp_list = list(set(dd1))

            logging.info('we put all the symptoms list together and also putting it in a set to avoid duplication')
            combined_df = maleria | Migraine | Typhoid | Pneumonia | Cholestasis

            logging.info('streamlining the dataframe together')
            streamlined_df = df[combined_df][symp_list]
            streamlined_df.replace([0, 1], ['No', 'Yes'], inplace=True)

            logging.info('we just converted the data into yes for 1 and no for 0')

            logging.info('creating the artifacts path')
            os.makedirs(os.path.dirname(self.data_ingestion_config.raw_data_path), exist_ok=True)


            logging.info('Saving the data into the just created path')
            streamlined_df.to_csv(self.data_ingestion_config.raw_data_path, index= False)

            return self.data_ingestion_config.raw_data_path

        except Exception as e:
            raise CustomException(e, sys)
        

if __name__ =="__main__":
    obj = DataIngestion()
    obj.Initiate_data_ingestion()