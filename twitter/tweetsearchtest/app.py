# the top of your flask app
from flask import Flask
app = Flask(__name__)

# a route example
@app.route(‘/’)
def home():
    return “Hello, Jeffrey Box. U R Kool with a K.”

# the bottom of your flask app
if __name__ == ‘__main__’:
    app.run(debug=True)
