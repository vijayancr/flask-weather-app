from flask import Flask, jsonify
import requests

# Initialize Flask app
app = Flask(__name__)

@app.route('/weather/<city>')
def weather(city):
    # Insert your actual API key here
    api_key = "f95f0ea9508f2728c30ca23c95620ced"  # Your OpenWeatherMap API key
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"

    response = requests.get(url)
    data = response.json()

    # Fetch temperature and weather condition from the response
    temperature = f"{data['main']['temp']}°C"
    condition = data['weather'][0]['description']

    return jsonify({
        "city": city,
        "temperature": temperature,
        "condition": condition
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

