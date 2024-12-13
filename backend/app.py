from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

# OpenWeatherMap API key
API_KEY = "24d1f67f493da1e8c753d7be01ed5bc3"

@app.route("/api/air-quality", methods=["GET"])
def air_quality():
    city = request.args.get("city")
    if not city:
        return jsonify({"error": "City is required"}), 400

    # OpenWeatherMap Air Pollution API
    url = f"http://api.openweathermap.org/data/2.5/air_pollution?appid={API_KEY}&q={city}"
    response = requests.get(url)
    if response.status_code != 200:
        return jsonify({"error": "Failed to fetch data"}), response.status_code

    return jsonify(response.json())

if __name__ == "__main__":
    app.run(debug=True)
