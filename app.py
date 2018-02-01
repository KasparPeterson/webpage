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
    json_request = request.json

    text = 'This is a sample response from your webhook!'
    json_response = json.dumps({"speech": text, "displayText": text})
    resp = Response(json.dumps(json_request))
    resp.headers['Content-Type'] = 'application/json'
    return resp


weather_api_endpoint = 'api.worldweatheronline.com'
weather_api_key = 'ac171efc8a0540f7a6f120039180102'



if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80, threaded=True)
