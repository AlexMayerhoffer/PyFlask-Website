from flask import Flask

app = Flask(__name__)


@app.route("/")
def index():
    return """"<html> <body> <img src="https://images-na.ssl-images-amazon.com/images/I/61yoTtDxuiL._SX425_.jpg"> </body> </html>"""


if __name__ == '__main__':
    app.run(port=5000, debug=True)
