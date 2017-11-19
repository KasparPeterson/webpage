from flask import Flask

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

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80, threaded=True)
