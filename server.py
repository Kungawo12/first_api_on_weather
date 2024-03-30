from flask import Flask,render_template,redirect,session,request
import os 
import requests
from pprint import pprint

app = Flask(__name__)

app.secret_key= 'Py is life'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get_weather', methods=['POST'])
def get_weather():
    zipcode = request.form['zipcode']
    header = os.environ.get('KEY')
    url = f"https://api.openweathermap.org/data/2.5/weather?zip={zipcode},us&appid={header}"
    response = requests.get(url)
    kelvin = response.json()['main']['temp']
    temp = (kelvin - 273.15) * 9/5 + 32
    print(temp)
    session['name'] = response.json()['name']
    session['condition'] = response.json()['weather'][0]['description']
    session['temp'] = response.json()['main']['temp']
    session['humidity'] = response.json()['main']['humidity']
    return redirect('/')


if __name__ =="__main__":
    app.run(debug=True, port=5001)