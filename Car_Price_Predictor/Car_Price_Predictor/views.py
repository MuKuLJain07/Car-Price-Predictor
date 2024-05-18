from django.http import HttpResponse
from django.shortcuts import render

import pandas as pd
import pickle as pkl
import numpy as np

data_path = "E:\Projects\Machine Learning\Second Hand Car Prices Predictor\cleaned car.csv"
model_path = r"E:\Projects\Machine Learning\Second Hand Car Prices Predictor\LinearRegressionModel.pkl"
car = pd.read_csv(data_path)

model = pkl.load(open(model_path, "rb"))

def homepage(request):
    if request.method == "POST":
        company = request.POST.get('company')
        car_model = request.POST.get('car_models')
        year = request.POST.get('year')
        fuel_type = request.POST.get('fuel_type')
        km_driven = request.POST.get('km_Driven')

        # Process the form data here (Predicting the price)
        car_data = [car_model, company, year, km_driven, fuel_type]
        print(car_data)
        prediction = model.predict(pd.DataFrame([car_data], columns=['name','company','year','kms_driven',"fuel_type"]))

        context = {
            'companies': sorted(car['company'].unique()),
            'car_model': sorted(car['name'].unique()),
            'years': sorted(car['year'].unique(), reverse=True),
            'fuel_type': car['fuel_type'].unique(),
            'km_driven': km_driven,
            'prediction': "Rs." + str(np.round(prediction[0],2))
        }

        return render(request,'index.html',context)
    

    companies = sorted(car['company'].unique())
    car_model = sorted(car['name'].unique())
    years = sorted(car['year'].unique(), reverse=True)
    fuel_type = car['fuel_type'].unique()

    data = {'companies': companies, 'car_models': car_model, 'years': years, 'fuel_type': fuel_type, 'prediction' : ""}

    return render(request,'index.html',data)


def aboutUS(request):
    return render(request, 'about.html')