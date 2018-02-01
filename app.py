from flask import Flask
from flask import Response
from flask import request
import json

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
    if date and geo_city:
        return "It's climate warming in " + geo_city + " on " + date
    elif date:
        return "It's really nice and warm on planet earth on " + date
    elif geo_city:
        return "It's warm today in " + geo_city
    else:
        return "It's climate warming warning warming warning...."


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80, threaded=True)
