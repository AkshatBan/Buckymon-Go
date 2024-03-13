# The following code uses the Flask framework for the API, establishing communication between the backend and frontend upon the latter making a request for route data. Currently we do not have a database setup to extract information, but we do have ER diagram implemented that we'll use as our placeholder methods. 

# Imports necessary Flask modules
from flask import Flask, jsonify, request
from flask_cors import CORS

# Creates a Flask application
app = Flask(__name__)
CORS(app, resources={r"/api/*": {"origins": "http://localhost:3000"}})



# Sample location data (will change later)
location_data = [
            {   
                'id': 1,
                'long': -89.408, 
                'lat': 43.0719,
                'location_name': 'Union South',
                'event_desc': 'description'
            },
            {
                'id': 2,
                'long': -89.4040, 
                'lat': 43.0757, 
                'location_name': 'Bascom Hall',
                'event_desc': 'something'
            }

]

# May create a method that queries the event data from the database once setup.

# Retrieves data from database, packages it into JSON format, and sent to frontend.
@app.route('/api/Post_Data_To_Frontend', methods=['GET'])
def Post_Data_To_Frontend():
    # Extract event data from database.
    # query = 'SELECT * FROM your_table_name' # will replace with actual database name
    
    # Initialize data for
    data = location_data

    # Package event data in JSON.

    if data:
        # Returns data in JSON format
        return jsonify(data)

# Receives the data from the frontend. When user clicks "Complete Event" button, this method will retrieve all event details, including the name, id, and location and stores it into the database.
@app.route('/api/Get_Data_From_Frontend', methods = ['GET', 'POST'])
def Get_Data_From_Frontend():
        # Access the JSON data from the request body
    data = request.json
    print(request.json)
    print("Received JSON data:", data)
    return jsonify({"message": "Data received successfully"}), 200
    # Gets the data from the request upon user completing an event in JSON format.
    
    # Process the data and store to the database.

    # Once, the data is stored in the database, return a response (indicator of receiving the request successfully)



# Runs the Flask application.
    if __name__ == '__main__':
        app.run(debug = True)
