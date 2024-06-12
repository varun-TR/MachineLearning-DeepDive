from flask import Flask,request,jsonify,render_template
import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler
import pickle


linear_model = pickle.load(open('models/lm_model.pkl','rb'))
scaler = pickle.load(open('models/scaler.pkl','rb'))



application = Flask(__name__)
app=application



@app.route('/', methods=['GET','POST'])
def predictdata_point():
    if request.method == 'POST':
        temperature = float(request.form.get('Temperature'))
        rh = int(request.form.get('RH'))
        ws = int(request.form.get('Ws'))
        rain = float(request.form.get('Rain'))
        ffmc = float(request.form.get('FFMC'))
        dmc = float(request.form.get('DMC'))
        isi = float(request.form.get('ISI'))
        classes = int(request.form.get('Classes'))
        region = int(request.form.get('Region'))

        new_data = scaler.transform([[temperature,rh,ws,rain,ffmc,dmc,isi,classes,region]])
        result = linear_model.predict(new_data)
        return render_template('home.html',results=result[0])

    
    else:
        return render_template('home.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0')