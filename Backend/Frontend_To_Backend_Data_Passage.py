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

# Returns list of all location data 
@app.route('/api/Get_List_Of_Locations', methods=['GET'])
def Get_List_Of_Locations():
    # Connect to the database
    connection = pymysql.connect(host='127.0.0.1',
                                user='root',
                                password='Jonah2004*',
                                database='Buckymon_Go_DB',
                                cursorclass=pymysql.cursors.DictCursor)

    cursor = connection.cursor()
    # Selects all Locations
    query = 'SELECT * FROM Locations;'
    cursor.execute(query)
    # Have to use fetch all to make sure it actually returns all matches 
    result = cursor.fetchall()   
    
    #Renames each of the keys to match how its specification in the API Documentation        
    for dictionary in result:
        dictionary['id'] = dictionary.pop("l_id")
        # Converts the latitude and longitude to floats with 5 digits
        dictionary['lat'] = round(float(dictionary.pop("l_lat") ))
        dictionary['long'] = round(float(dictionary.pop("l_long")))
        dictionary['location_name'] = dictionary.pop("l_name")

        #Adds an event description 
        # Selects all Locations
        query = 'SELECT e_desc FROM Events WHERE l_id = ' + str(dictionary['id'])
        cursor.execute(query) 
        description = cursor.fetchone()
                
        #Only adds it if it exists
        if(description != None):
            dictionary['event_desc'] = description['e_desc']    
            
    #Closes cursor and connection at the end
    cursor.close()
    connection.close()

    #Converts the dicionary to json
    return json.dumps(result)

# When the user completes an event a post will be sent to the backend with the following body
# {
#    username: 'user123',
#    event_id: 1
#}
@app.route('/api/Complete_Event', methods=['POST'])
def Complete_Event():
    userInfo = request.json
    
    #For Testing Purposes
    '''
    userInfo = { 
                'username': 'Aaron',
                'event_id': 40000002
              }
    '''

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
    
    cursor = connection.cursor()

    try: 
        #First gets userID to write to the Completes Database
        query = 'SELECT u_id FROM User WHERE u_name = ' + '\'' + userName + '\''
        cursor.execute(query)
        result = cursor.fetchone()
        userId = result['u_id']

        #Now writes to Completes database to signify that user Completed Event
        query = 'INSERT INTO Completes (completes_u_id, completes_e_id) Values (' + str(userId) + ',' + str(eventId) + ')'
        cursor.execute(query)

        #First reads the event score value
        query = 'SELECT e_score FROM Events WHERE e_id = ' + str(eventId)
        cursor.execute(query)
        result = cursor.fetchone()
        eventScore = result['e_score']

        # Now obtains the user's score
        query = 'SELECT u_score FROM User WHERE u_name = ' + '\'' + userName + '\''
        cursor.execute(query)
        result = cursor.fetchone()
        userScore = result['u_score']    

        #Now writes the new user score to the database
        updatedScore = userScore + eventScore

        #Now writes to User database their new score
        query = 'UPDATE User SET u_score = ' + str(updatedScore) + ' WHERE u_name = ' + '\'' + userName + '\''
        cursor.execute(query)

        #Commit all changes 
        connection.commit()

    #This means that a duplicate UserID and EventID were sent in to Complete_Event, which the Frontend shouldn't do,
    # so there is an error on their part
    except Exception as e :
        print(f"An error occurred: {e}")
        return 400

    finally:
        #Closes cursor and connection at the end no matter what happens 
        cursor.close()
        connection.close()

    #Returns it in JSON format with success code 200
    return json.dumps({
                    'updated_score': updatedScore
                 }), 200

#This method takes in a username and returns all the Events that the user has not yet completed
@app.route('/api/Active_Events', methods = ['GET'])
def Active_Events():
    userInfo = request.json

    #For testing purposes
    '''
    userInfo =  {
                    'username': 'Aaron'
                }
    '''

    userName = userInfo['username']
    userId = 0
    eventDict = {}
    # Connect to the database just to access event and get its score value and then get userScore
    connection = pymysql.connect(host='127.0.0.1',
                                user='root',
                                password='Jonah2004*',
                                database='Buckymon_Go_DB',
                                cursorclass=pymysql.cursors.DictCursor)
    
    cursor = connection.cursor()

     #Gets the user id based on the user name
    query = 'SELECT u_id FROM User WHERE u_name = ' + '\'' + userName + '\''
    cursor.execute(query)
    userDict = cursor.fetchone()
    userId = userDict['u_id']

    #Now we get all user's completed event IDs 
    query = 'SELECT completes_e_id FROM Completes WHERE completes_u_id = ' + str(userId)
    cursor.execute(query)
    eventDict = cursor.fetchall()     
    
    #If the user has completed no events, then return code 400. eventdict will be False if it's empty
    if bool(eventDict) == False:
        return 400
    
    #Stores all completed Events in tuple for our query to database
    completedEventsIDs = []
    for dictionary in eventDict:
        completedEventsIDs.append(dictionary['completes_e_id'])

    #Changes completedEventIDs to a string with parantheses
    strRep = str(completedEventsIDs)
    #Replaces the [] with () so it will work with my sql
    strRep = '(' + strRep[1:len(strRep)-1:1] + ')'

    uncompletedEvents = {}
    
    query = 'SELECT * FROM Events WHERE e_id NOT IN ' + strRep
    cursor.execute(query)
    uncompletedEvents = cursor.fetchall()
        
    #Now builds final eventDict while also getting data from Locations table

    for dictionary in uncompletedEvents:
        dictionary['event_id'] = dictionary.pop('e_id')

        query = 'SELECT l_name, l_lat, l_long FROM Locations WHERE l_id = ' + str(dictionary['l_id'])
        cursor.execute(query)
        locationData = cursor.fetchone()

        # Converts the latitude and longitude to floats with 5 digits, adds location name
        dictionary['lat'] = round(float(locationData['l_lat']))
        dictionary['long'] = round(float(locationData['l_long']))
        dictionary['location_name'] = locationData['l_name']

        #Switches name of Event score, and Event Description
        dictionary['event_score'] = dictionary.pop('e_score')
        dictionary['event_description'] = dictionary.pop('e_desc')

        #Gets rid of event name, location id
        dictionary.pop('e_name')
        dictionary.pop('l_id')

    #Closes cursor and connection
    cursor.close()
    connection.close()

    return json.dumps(uncompletedEvents)

#This method takes in a username and returns all the Events that the user has not yet completed
@app.route('/api/Get_Completed_Events', methods = ['GET'])
def Get_Completed_Events():
    userInfo = request.json
    
    #For testing purposes
    '''
    userInfo =  {
                    'username': 'Aaron'
                }
    '''

    userName = userInfo['username']
    userId = 0
    eventDict = {}
    # Connect to the database just to access event and get its score value and then get userScore
    connection = pymysql.connect(host='127.0.0.1',
                                user='root',
                                password='Jonah2004*',
                                database='Buckymon_Go_DB',
                                cursorclass=pymysql.cursors.DictCursor)
    
    cursor = connection.cursor()

    #Gets the user id based on the user name
    query = 'SELECT u_id FROM User WHERE u_name = ' + '\'' + userName + '\''
    cursor.execute(query)
    userDict = cursor.fetchone()
    userId = userDict['u_id']
        
    #Now we get all user's completed event IDs 
    query = 'SELECT completes_e_id FROM Completes WHERE completes_u_id = ' + str(userId)
    cursor.execute(query)
    eventDict = cursor.fetchall()
        
    #If the user has completed no events, then return code 400. eventdict will be False if it's empty
    if bool(eventDict) == False:
        return 400

    #Stores all completed Events in tuple for our query to database
    completedEventsIDs = []
    for dictionary in eventDict:
        completedEventsIDs.append(dictionary['completes_e_id'])

    #Changes completedEventIDs to a string with parantheses
    strRep = str(completedEventsIDs)
    #Replaces the [] with () so it will work with my sql
    strRep = '(' + strRep[1:len(strRep)-1:1] + ')'

    completedEvents = {}
    query = 'SELECT * FROM Events WHERE e_id IN ' + strRep
    cursor.execute(query)
    completedEvents = cursor.fetchall()
        
    #Now builds final eventDict while also getting data from Locations table
    for dictionary in completedEvents:
        dictionary['event_id'] = dictionary.pop('e_id')

        query = 'SELECT l_name, l_lat, l_long FROM Locations WHERE l_id = ' + str(dictionary['l_id'])
        cursor.execute(query)
        locationData = cursor.fetchone() 

        # Converts the latitude and longitude to floats with 5 digits, adds location name
        dictionary['lat'] = round(float(locationData['l_lat']))
        dictionary['long'] = round(float(locationData['l_long']))
        dictionary['location_name'] = locationData['l_name']

        #Switches name of Event score, and Event Description
        dictionary['event_score'] = dictionary.pop('e_score')
        dictionary['event_description'] = dictionary.pop('e_desc')

        #Gets rid of event name, location id
        dictionary.pop('e_name')
        dictionary.pop('l_id')

    #Closes cursor and connection
    cursor.close()
    connection.close()

    return json.dumps(completedEvents)

# When a user attempts to login, a POST request will be sent to the backend with the following body:
# {
#     username: 'user123'
#     password: 'password123'
# }
@app.route('/api/Log_User', methods=['POST'])
def Log_User():
    # Extracts the username and password from request
    userInfo = request.json
    username = userInfo['username']
    password = userInfo['password']
    # TODO: Fix method to return appropriate JSON bodies
    # TODO: Figure out how team wants to log new user and password, especially if it's in a database
# When the user logs in, a GET request will be sent to the backend with the following body:
# {
#    username: 'user123'
# }

# When the user logs in, a GET request will be sent to the backend with the following body:
# {
#    username: 'user123'
# }
@app.route('/api/Get_User_Achievements', methods=['GET'])
def Get_User_Achievements():
    # Acquires username upon GET request
    #userInfo = request.json
    
    userInfo = {
                'username': 'Aaron'
               }
    
    userName = userInfo['username']
    userScore = 0
    # Establishes a table that contain user's completed achievement(s) to reference
    completedAchievements = []
    # Connect to database to read the data
    connection = pymysql.connect(host='127.0.0.1',
                                user='root',
                                password='Jonah2004*',
                                database='Buckymon_Go_DB',
                                cursorclass=pymysql.cursors.DictCursor)
    # Obtains user score and user ID
    with connection:
        with connection.cursor() as cursor:
            # Obtains user ID to reference when we extract user's completed achievements
            query = 'SELECT u_id FROM User WHERE u_name = ' + '\'' + userName + '\''
            cursor.execute(query)
            result = cursor.fetchone()
            userId = result['u_id']
            # References user score to put onto JSON body
            query = 'SELECT u_score FROM User WHERE u_name = ' + '\'' + userName + '\''
            cursor.execute(query)
            result = cursor.fetchone()
            userScore = result['u_score']
        # Gets all user's completed achievements to return in JSON format
        with connection.cursor() as cursor:
            query = 'SELECT achieves_a_id FROM Achieves WHERE achieves_u_id = ' + '\'' + str(userId) + '\''
            cursor.execute(query)
            achieved = cursor.fetchall()
            # Queries through all achievements to extract user's completed achievements
            for dictionary in achieved:
                # References an achieved ID to extract user's completed achievement(s)
                achievedID = str(dictionary['achieves_a_id'])
                # Make a new connection to within for loop
                connection2 = pymysql.connect(host='127.0.0.1',
                                              user='root',
                                              password='Jonah2004*',
                                              database='Buckymon_Go_DB',
                                              cursorclass=pymysql.cursors.DictCursor)
                with connection2.cursor() as cursor:
                    query = 'SELECT * FROM Achievements WHERE a_id = ' + '\'' + achievedID  + '\''
                    cursor.execute(query)
                    currentResult = cursor.fetchone()
                    # Creates the user's completed achievement to add later
                    userAchievement = {
                        'achievement_id': currentResult['a_id'],
                        'achievement_name': currentResult['a_name'],
                        'achievement_score': currentResult['a_score'],
                        'achievement_description': currentResult['a_desc']
                    }
                    completedAchievements.append(userAchievement)
    # Formats the user's completed achievements data according to the API Documentation
    result = {
            'username': userName,
            'user_score' : userScore,
            'completed_achievements': completedAchievements
    }
    # Formats the final result in JSON format with success code 200
    return json.dumps(result), 200

# Runs the Flask application.
if __name__ == '__main__':   
    app.run(debug = True)