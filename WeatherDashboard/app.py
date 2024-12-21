from flask import Flask, render_template, request
import requests

app = Flask(__name__)

API_KEY = '5129234c1b06b4030c5fc135f5268a02'
BASE_URL = 'http://api.openweathermap.org/data/2.5/weather'

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/weather', methods=['POST'])
def weather():
    city = request.form.get('city')
    if not city:
        return render_template('index.html', error="Please enter a city name.")
    
    try:
        params = {'q': city, 'appid': API_KEY, 'units': 'metric'}
        response = requests.get(BASE_URL, params=params)
        data = response.json()

        if data.get('cod') != 200:
            return render_template('index.html', error=data.get('message', 'Error fetching data.'))

        weather_data = {
            'city': data['name'],
            'temperature': data['main']['temp'],
            'humidity': data['main']['humidity'],
            'description': data['weather'][0]['description'],
            'icon': data['weather'][0]['icon'],
        }
        return render_template('result.html', weather=weather_data)

    except Exception as e:
        return render_template('index.html', error="An error occurred while fetching the data.")

if __name__ == '__main__':
    app.run(debug=True)
