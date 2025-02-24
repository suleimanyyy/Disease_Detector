import sys
import numpy as np
import pandas as pd
from DISEASE_DETECTOR.utils import load_object
from DISEASE_DETECTOR.exception import CustomException



class PredictPipeline:
    def __init__(self):
        pass

    def predict(self, df_features):
        model_path = "artifacts\model.pkl"
        preprocessor_path = "artifacts\processor.pkl"
        model = load_object(model_path)
        preprocessor = load_object(preprocessor_path)
        processed_df = preprocessor.transform(df_features)
        prediction = model.predict(processed_df)

        return prediction
    

class CustomData:
    def __init__(self, toxic_look, excessive_hunger, sweating, diarrhoea,
        abdominal_pain, yellowish_skin, visual_disturbances, blurred_and_distorted_vision, 
        malaise, fast_heart_rate, phlegm, chills, itching, acidity, nausea, cough, indigestion,
       fatigue, depression, breathlessness, headache, high_fever,
       constipation, muscle_pain, belly_pain, loss_of_appetite,
       chest_pain, rusty_sputum, stiff_neck, yellowing_of_eyes,
       irritability, vomiting):
        self.toxic_look = toxic_look
        self.excessive_hunger = excessive_hunger
        self.sweating = sweating
        self.diarrhoea = diarrhoea
        self.abdominal_pain = abdominal_pain
        self.yellowish_skin = yellowish_skin
        self.visual_disturbances = visual_disturbances
        self.blurred_and_distorted_vision = blurred_and_distorted_vision
        self.malaise = malaise
        self.fast_heart_rate = fast_heart_rate
        self.phlegm = phlegm
        self.chills = chills
        self.itching = itching
        self.acidity = acidity
        self.nausea = nausea
        self.cough = cough
        self.indigestion = indigestion
        self.fatigue = fatigue
        self.depression = depression
        self.breathlessness = breathlessness
        self.headache = headache
        self.high_fever = high_fever
        self.constipation = constipation
        self.muscle_pain = muscle_pain
        self.belly_pain = belly_pain
        self.loss_of_appetite = loss_of_appetite
        self.chest_pain = chest_pain
        self.rusty_sputum = rusty_sputum
        self.stiff_neck = stiff_neck
        self.yellowing_of_eyes = yellowing_of_eyes
        self.irritability = irritability
        self.vomiting = vomiting


    def get_feature_df(self):
        try:
            feature_dict = {

                "toxic_look_(typhos)" : [self.toxic_look],
                "excessive_hunger" : [self.excessive_hunger],
                "sweating" : [self.sweating],
                "diarrhoea" : [self.diarrhoea],
                "abdominal_pain" : [self.abdominal_pain],
                "yellowish_skin" : [self.yellowish_skin],
                "visual_disturbances" : [self.visual_disturbances],
                "blurred_and_distorted_vision" : [self.blurred_and_distorted_vision],
                "malaise" : [self.malaise],
                "fast_heart_rate" : [self.fast_heart_rate],
                "phlegm" : [self.phlegm],
                "chills" : [self.chills],
                "itching" : [self.itching],
                "acidity" : [self.acidity],
                "nausea" : [self.nausea],
                "cough" : [self.cough],
                "indigestion" : [self.indigestion],
                "fatigue" : [self.fatigue],
                "depression" : [self.depression],
                "breathlessness" : [self.breathlessness],
                "headache" : [self.headache],
                "high_fever" : [self.high_fever],
                "constipation" : [self.constipation],
                "muscle_pain" : [self.muscle_pain],
                "belly_pain" : [self.belly_pain],
                "loss_of_appetite" : [self.loss_of_appetite],
                "chest_pain" : [self.chest_pain],
                "rusty_sputum" : [self.rusty_sputum],
                "stiff_neck" : [self.stiff_neck],
                "yellowing_of_eyes" : [self.yellowing_of_eyes],
                "irritability" : [self.irritability],
                "vomiting" : [self.vomiting]
                 }
            feature_df = pd.DataFrame(feature_dict)

            return feature_df
        
        except Exception as e:
            raise CustomException(e, sys)