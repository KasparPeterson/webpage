from flask import Flask
from flask import Response
from flask import request
import json
import requests

app = Flask(__name__)

@app.route("/")
def hello():
    html = "<center>" \
             "<h3>My baddass webpage</h3>" \
             "Contact me:" \
             "<p><a href=\"https://www.linkedin.com/in/kaspar-peterson-98075994\"><b>Linked in</b></a></p>" \
             "<p>or</p>" \
             "<p>kasparpeterson@hotmail.com</p>" \
           "</center>"
    return html.format()


@app.route("/weather", methods = ['POST'])
def weather():
    text = get_response_text(request.json)
    json_response = json.dumps({"speech": text, "displayText": text})
    resp = Response(json_response)
    resp.headers['Content-Type'] = 'application/json'
    return resp


def get_response_text(json_request):
    parameters = json_request['result']['parameters']
    date = parameters['date']
    geo_city = parameters['geo-city']
    return get_text(date, geo_city)


def get_text(date, geo_city):
    json_response = fetch_weather_info(date, geo_city)
    weather = json_response['data']['weather'][0]
    return 'The weather in ' + geo_city + ' on ' + date + ' is from ' + weather['mintempC'] + ' to ' \
           + weather['maxtempC'] + ' degree celsius.'


host = 'http://api.worldweatheronline.com'
end_point = '/premium/v1/weather.ashx'
api_key = 'ac171efc8a0540f7a6f120039180102'


def fetch_weather_info(date, geo_city):
    url = host + end_point
    querystring = {
        "format": "json",
        "num_of_days": "1",
        "q": geo_city,
        "date": date,
        "key": api_key
    }

    response = requests.request("GET", url, params=querystring)
    return json.loads(response.text)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80, threaded=True)
