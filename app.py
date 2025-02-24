from flask import Flask, render_template, request
import sys
import numpy as np
import pandas as pd
from DISEASE_DETECTOR.utils import load_object
from DISEASE_DETECTOR.exception import CustomException
from DISEASE_DETECTOR.pipeline.predict_pipeline import PredictPipeline, CustomData
from DISEASE_DETECTOR.components.precusion_data import Precausion


application = Flask(__name__)

app = application

@app.route("/")
def index():
    return render_template("home.html")


@app.route("/predict", methods = ['GET','POST'])
def predict_datapoint():
    if request.method == "GET":
        return render_template("index.html")
    else:
        data = CustomData(
            toxic_look = request.form.get("toxic_look"),
            excessive_hunger = request.form.get("excessive_hunger"),
            sweating = request.form.get("sweating"),
            diarrhoea = request.form.get("diarrhoea"),
            abdominal_pain = request.form.get("abdominal_pain"),
            yellowish_skin = request.form.get("yellowish_skin"),
            visual_disturbances = request.form.get("visual_disturbances"),
            blurred_and_distorted_vision = request.form.get("blurred_and_distorted_vision"),
            malaise = request.form.get("malaise"),
            fast_heart_rate = request.form.get("fast_heart_rate"),
            phlegm = request.form.get("phlegm"),
            chills = request.form.get("chills"),
            itching = request.form.get("itching"),
            acidity = request.form.get("acidity"),
            nausea = request.form.get("nausea"),
            cough = request.form.get("cough"),
            indigestion = request.form.get("indigestion"),
            fatigue = request.form.get("fatigue"),
            depression = request.form.get("depression"),
            breathlessness = request.form.get("breathlessness"),
            headache = request.form.get("headache"),
            high_fever = request.form.get("high_fever"),
            constipation = request.form.get("constipation"),
            muscle_pain = request.form.get("muscle_pain"),
            belly_pain = request.form.get("belly_pain"),
            loss_of_appetite = request.form.get("loss_of_appetite"),
            chest_pain = request.form.get("chest_pain"),
            rusty_sputum = request.form.get("rusty_sputum"),
            stiff_neck = request.form.get("stiff_neck"),
            yellowing_of_eyes = request.form.get("yellowing_of_eyes"),
            irritability = request.form.get("irritability"),
            vomiting = request.form.get("vomiting")
        )
        feature_df = data.get_feature_df()
        print(feature_df)

        pred_pipeline = PredictPipeline()
        prediction = pred_pipeline.predict(feature_df)
        caution = Precausion()
        c1, c2, c3, c4 = caution.precausion_list(prediction=prediction[0])
        return render_template("index.html", prediction = prediction[0], c1=c1[0], c2=c2[0], c3=c3[0], c4=c4[0])



if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)