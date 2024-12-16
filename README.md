# Flask Weather App

A simple Flask-based application that fetches and displays weather information for a specified location. This project is designed for learning and experimenting with Flask and weather APIs.

## Features

- Fetch weather data using a weather API.
- Display weather conditions, temperature, and more for a specified city.
- Easy-to-setup Flask app suitable for beginners.

## Prerequisites

Before running the app, ensure you have the following:

1. **Python** (version 3.6 or higher)
2. **Flask** library
3. An API key from a weather service provider (e.g., OpenWeatherMap, WeatherAPI, etc.)

## Setup and Installation

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/vijayancr/flask-weather-app.git
   cd flask-weather-app
   ```

2. **Install Dependencies:**
   Create a virtual environment (optional but recommended) and install the required libraries:
   ```bash
   python3 -m venv venv
   source venv/bin/activate   # On Windows: venv\Scripts\activate
   pip install -r requirements.txt
   ```

3. **Set API Key:**
   - Add your API key in the application code (e.g., `app.py`) where the weather API is called.

4. **Run the App:**
   ```bash
   flask run
   ```
   The app will be accessible at `http://127.0.0.1:5000`.

## Docker Deployment

To containerize and deploy this app using Docker, follow these steps:

1. **Create a `Dockerfile`:**
   ```dockerfile
   FROM python:3.9-slim

   # Set the working directory
   WORKDIR /app

   # Copy the project files
   COPY . /app

   # Install dependencies
   RUN pip install -r requirements.txt

   # Expose the port the app runs on
   EXPOSE 5000

   # Run the Flask app
   CMD ["flask", "run", "--host=0.0.0.0", "--port=5000"]
   ```

2. **Build and Run the Docker Image:**
   ```bash
   docker build -t flask-weather-app .
   docker run -d -p 5000:5000 flask-weather-app
   ```

3. **Access the App:**
   Open your browser and navigate to `http://localhost:5000`.

## Contribution

Feel free to fork this repository and make improvements. Pull requests are welcome!

## License

This project is licensed under the MIT License. See the LICENSE file for details.

---

If you encounter any issues or have suggestions, please raise an issue in the repository or contact the maintainer.
