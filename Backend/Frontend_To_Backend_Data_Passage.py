# The following code uses the Flask framework for the API, establishing communication between the backend and frontend upon the latter making a request for route data. Currently we do not have a database setup to extract information, but we do have ER diagram implemented that we'll use as our placeholder methods. 

# Imports necessary Flask modules
from flask import Flask, jsonify, request

# Creates a Flask application
app = Flask(__name__)

# Sample location data (will change later)
location_data = {
        'locations': {
            1 : {
                'long': 37.7749, 
                'lat': -122.4194,
                'location_name': 'San Francisco',
                'event_desc': 'Rave at SF'
                }
            2 : {
                'long': 34.0522, 
                'lat': -118.2437, 
                'location_name': 'Los Angeles'
                'event_desc': 'Stars at LA'
                }
        }
}

# May create a method that queries the event data from the database once setup.

# Retrieves data from database, packages it into JSON format, and sent to frontend.
@app.route('/api/Post_Data_To_Frontend', methods=['POST'])
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
@app.route('/api/Get_Data_From_Frontend', methods = ['GET'])
def Get_Data_From_Frontend():
    # Gets the data from the request upon user completing an event in JSON format.
    
    # Process the data and store to the database.

    # Once, the data is stored in the database, return a response (indicator of receiving the request successfully)



# Runs the Flask application.
if __name__ == '__main__':
    app.run(debug = True)
