# 2024 UNSW SCONES conference
# Author: Jigmey Dorjee, Karthigeyan Ramesh, Halliya Um

# import the libraries...

from flask import Flask 


app = Flask(__name__)
@app.route('/')
def hello():
    return 'Hello, World!'

if __name__ == "__main__":
    app.run(debug=False,host='0.0.0.0',port="5003")


