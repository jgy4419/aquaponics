from flask import Flask, render_template, make_response, redirect, jsonify
from data import *
import numpy as np
import pandas as pd
import json

app = Flask(__name__)

@app.route('/')
def setup():
    connection()
    return redirect('/main')

@app.route('/main')
def mainPage():
    return render_template('main.html')

@app.route('/chart')
def chart():
    try:
        df = dataFind()
        ren = ['Humidity', 'Temperature', 'SoilHumidity', 'Light', 'pH']
        opt = ['humidity', 'temperature', 'soilHumidity', 'light', 'ph']
        ttxt = ['System Humidity', 'System Temperature', 'System Soil Humidity', 'System Light', 'Water PH']
        ytxt = ['Humidity', 'Temperature', 'Soil Humidity', 'Light', 'pH']
        info = []
        for i in range(5):
            chart = {"renderTo": ren[i], "defaultSeriesType": "spline", "events": {"load": "requestData"}}
            series = getSerial(df, opt[i])
            title = {"text": ttxt[i]}
            xAxis = {"type": "datetime", "range": 1000*3600}
            yAxis = {"title": {"text": ytxt[i]}}
            info.append([chart, series, title, xAxis, yAxis])
        # dataInput()
        return render_template('chart.html', chartInfo = info)
    except:
        return redirect('/')

def getSerial(df, option):
    ser = '[{"name":"sensor", "data":['
    for t, ir in zip(df.index, df.iterrows()):
        ser += '[['  + str(t).split()[1].replace(':', ', ')[:-1] + '], ' + str(ir[1][option]) + '],'
    ser = ser[:-1]
    ser += ']}]'
    return ser

@app.route('/control')
def controlSetup():
    return render_template('control.html')

@app.route('/pumpOn')
def controlPanelOn():
    pushData([1])
    return redirect('/control')

@app.route('/pumpOff')
def controlPanelOff():
    pushData([0])
    return redirect('/control')

@app.route('/end')
def end():
    disconnection()

if __name__ == '__main__':
    try:
        #app.run(debug=True, host='192.168.43.16', port=5000) # hotspot
        app.run(debug=True, host='192.168.0.7', port=5000)
    except KeyboardInterrupt:
        disconnection()