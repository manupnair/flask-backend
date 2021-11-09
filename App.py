from flask import Flask,jsonify
# import pandas as pd
import json

app=Flask(__name__)
f=open("Data Set - Insurance Client.json")

# df = pd.read_csv("Data Set - Insurance Client.csv")
# df = df.to_json("Data Set - Insurance Client.json")


# print(data)
@app.route('/')
def getData():
    data=json.load(f)
    response = jsonify(data)
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response