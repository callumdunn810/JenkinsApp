from flask import flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Welcome! :)"

if __name__='__main__':
    app.route(debug=True, port=5000, host='0.0.0.0')