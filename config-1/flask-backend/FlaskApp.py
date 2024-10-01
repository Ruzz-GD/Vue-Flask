from flask import Flask,jsonify
from flask_cors import CORS

app = Flask(__name__)

CORS(app)
# this is the main route of your flask http://127.0.0.1:5000
@app.route('/')
def hello_world():
    return 'Hello From Flask'

# now we can make a simple route to make api end point for axios
@app.route('/axios_method',methods=['GET'])
def axios_endpoint():
    # you can try to change the message 
    return jsonify({'message':'hello axios from flask'})

# now we can make a simple route to make api end point for fetch
@app.route('/fetch_method',methods=['GET'])
def fetch_endpoint():
    # you can try to change the message 
    return jsonify({'message':'hello fetch from flask'})

if __name__ == '__main__':
    app.run(debug=True)
