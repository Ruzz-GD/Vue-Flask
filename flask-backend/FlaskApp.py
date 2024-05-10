from flask import Flask,jsonify,request
from flask_cors import CORS
from DatabaseConnector import db_conn
from DatabaseTable import User

app = Flask(__name__)

CORS(app)
# this is the main route of your flask http://127.0.0.1:5000
@app.route('/')
def hello_world():
    return 'Hello From Flask'

# now we can make a simple route to make api end point for axios
@app.route('/axios_method',methods=['GET'])
def axios_endpoint():
    return jsonify({'message':'hello axios from flask'})

# now we can make a simple route to make api end point for fetch
@app.route('/fetch_method',methods=['GET'])
def fetch_endpoint():
    return jsonify({'message':'hello fetch from flask'})

# this is a simple route with database 
@app.route('/mysql', methods=['POST'])
# This route handles various HTTP methods like POST, DELETE, GET, UPDATE, etc.
def mysql():
    # Get JSON data from the request
    data = request.get_json()
    # Extract 'username' from the JSON data passed from Vue.js through the API
    username = data.get('username')
    
    # Establish a database connection
    connector = db_conn()
    
    # Check if the connector was successfully connected to the database
    if not connector:
        # If there's a problem connecting to the database, return an error response
        return jsonify({'error': 'There was a problem connecting to the database'}), 500

    # If the connector was successfully connected, proceed to add the user to the database
    connector.add(User(username=username))
    # Commit changes to the database
    add_user = connector.commit()
    # Close the database connection
    connector.close()
    # after this you can navigate to you database/table and see if the username row is there
    return jsonify({'message':'username successfully added'})
if __name__ == '__main__':
    app.run(debug=True)
