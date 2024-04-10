# The following code uses the Flask framework for the API, establishing communication between the backend and frontend upon the latter making a request for route data. Currently we do not have a database setup to extract information, but we do have ER diagram implemented that we'll use as our placeholder methods. 

# Imports necessary Flask modules
from flask import Flask, jsonify, request
from flask_cors import CORS
import pymysql.cursors
import json

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


# When the user completes an event a post will be sent to the backend with the following body
# {
#    username: 'user123',
#    event_id: 1
#}
@app.route('/api/Complete_Event', methods=['POST'])
def Complete_Event():
    userInfo = request.json
    userName = userInfo['username']
    eventId = userInfo['event_id']
    userScore = 0
    eventScore = 0
    userId = 0
    updatedScore = 0

    # Connect to the database just to access event and get its score value and then get userScore
    connection = pymysql.connect(host='127.0.0.1',
                                user='root',
                                password='Jonah2004*',
                                database='Buckymon_Go_DB',
                                cursorclass=pymysql.cursors.DictCursor)

    with connection:
        #First reads the event score value
        with connection.cursor() as cursor:
            query = 'SELECT e_score FROM Events WHERE e_id = ' + str(eventId)
            cursor.execute(query)
            result = cursor.fetchone()
            eventScore = result['e_score']

        # Now obtains the user's score
        with connection.cursor() as cursor:
            query = 'SELECT u_score FROM User WHERE u_name = ' + '\'' + userName + '\''
            cursor.execute(query)
            result = cursor.fetchone()
            userScore = result['u_score']

        #Gets the userId for later when we need to write to Completes Database
            query = 'SELECT u_id FROM User WHERE u_name = ' + '\'' + userName + '\''
            cursor.execute(query)
            result = cursor.fetchone()
            userId = result['u_id']
        
    # Separate connection to actually write to User Database
    connection2 = pymysql.connect(host='127.0.0.1',
                                user='root',
                                password='Jonah2004*',
                                database='Buckymon_Go_DB',
                                cursorclass=pymysql.cursors.DictCursor)

    #Now writes the new user score to the database
    with connection2.cursor() as cursor:
        updatedScore = userScore + eventScore
        #First writes to User database
        query = 'UPDATE User SET u_score = ' + str(updatedScore) + ' WHERE u_name = ' + '\'' + userName + '\''
        cursor.execute(query)

    #Commits changes to User database
    connection2.commit()

    connection3 = pymysql.connect(host='127.0.0.1',
                                user='root',
                                password='Jonah2004*',
                                database='Buckymon_Go_DB',
                                cursorclass=pymysql.cursors.DictCursor)
    
    with connection3.cursor() as cursor:
        query = 'INSERT INTO Completes (completes_u_id, completes_e_id) Values (' + str(userId) + ',' + str(eventId) + ')'
        cursor.execute(query)

    #Commits change to Completes Database
    connection3.commit()

    #Returns it in JSON format with success code 200
    return json.dumps({
                    'updated_score': updatedScore
                 }), 200

# Runs the Flask application.
if __name__ == '__main__':    
    app.run(debug = True)
