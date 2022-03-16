from flask import Flask,request
import requests, json
app = Flask(__name__)


def get():
    lat = request.args.get('lat')
    lon = request.args.get('lon')
    URL = "https://api.openweathermap.org/data/2.5/weather?lat="+lat+"&lon="+lon+"&appid=6f807e42edb11b81c3439053f342477a"

    
    response = requests.get(URL)
    
    data = response.json()

    return data


