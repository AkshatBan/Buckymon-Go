import unittest
from flask import url_for
from unittest.mock import MagicMock, patch
from Backend import app, Complete_Event, Get_User_Achievements, Active_Events, Get_List_Of_Locations, Get_Completed_Events, Log_User, Get_Uncompleted_Achievements
import json
from io import StringIO

# Uses python's unittest mocking library to mock requests to the client
class TestFlaskAPI(unittest.TestCase):

    # Sets up the testing enviroment by creating a test client
    def setUp(self):
        app.testing = True
        self.client = app.test_client()

    @patch('Backend.pymysql.connect') # replaces pymysql connect import with a mock    
    def test_get_list_of_locations(self, mock_connect):
        # setting up mock cursor with proper fetchone and fetchall results
        mock_cursor = MagicMock()
        mock_cursor.execute = MagicMock()
        fetchallResult = [
            {
                "l_id": 1,
                "l_lat": 10,
                "l_long": 20,
                "l_name": "My house"
            },
            {
                "l_id": 2,
                "l_lat": 11.002,
                "l_long": 8.345,
                "l_name": "Their house"
            }
        ]
        mock_cursor.fetchall = MagicMock(return_value=fetchallResult)
        fetchoneResults = [
            {
                "e_desc": "House party",
                "e_id": 1
            },
            {
                "e_desc": "Lamer house party",
                "e_id": 2
            }
        ]
        mock_cursor.fetchone = MagicMock(side_effect=fetchoneResults)
        mock_cursor.close = MagicMock()
        
        mock_connect.return_value = MagicMock()
        mock_connect.return_value.cursor = MagicMock(return_value=mock_cursor)
        mock_connect.return_value.close = MagicMock
        
        # gets the response by calling the method
        response = Get_List_Of_Locations()
        
        expected = [
            {
                "id": 1,
                "lat": 10,
                "long": 20,
                "location_name": "My house",
                "event_desc": "House party",
                "event_id": 1
            },
            {
                "id": 2,
                "lat": 11,
                "long": 8,
                "location_name": "Their house",
                "event_desc": "Lamer house party",
                "event_id": 2
            }
        ]
        self.assertEqual(response, json.dumps(expected))
        
    # @patch('Frontend_To_Backend_Data_Passage.request') # replaces the request import with a mock import
    @patch('Backend.pymysql.connect') # replaces pymysql connect import with a mock    
    def test_complete_event(self, mock_connect):
        with app.test_request_context(
        "/api/Complete_Event?username=Aaron&event_id=40000002", method="POST", json={"username": "Aaron",
                                                    "event_id": 40000002}
        ):
            data={"username": "Aaron", "event_id": 40000002}
            # replaces request.json function with a mock fcn that returns
            # hard-coded dict
            # mock_request.json = MagicMock(return_value={"username": "Aaron",
            #                                             "event_id": 40000002})
            
            # mocks the connection.cursor() object
            mock_cursor = MagicMock()
            mock_cursor.close = MagicMock()
            mock_cursor.execute = MagicMock()
            # mock cursor.fetchone, having it return hardcoded dict
            fetchoneRets = [{"u_id": 1},
                            {"e_score": 10},
                            {"u_score": 30}]
            fetchoneMock = MagicMock(side_effect=fetchoneRets)
            mock_cursor.fetchone = fetchoneMock
            
            # Set up mock connection object
            mock_connect.return_value = MagicMock()
            mock_connect.return_value.commit = MagicMock()
            mock_connect.return_value.cursor = MagicMock(return_value=mock_cursor)
            
            # gets the response by calling the test client
            # note: this response is not a mock
            # response = self.client.get(url_for('Frontend_To_Backend_Data_Passage.Complete_Event', data))
            response = Complete_Event()
            
            # Assertations
            
            # check that the query to update the user score in User db was 
            # executed
            query2 = 'UPDATE User SET u_score = ' + str(40) + ' WHERE u_name = ' + '\'' + "Aaron" + '\''
            mock_cursor.execute.assert_called_with(query2)
            
            # make sure that commit was also called
            mock_connect.return_value.commit.assert_called_once()
            
            # assert that the retrieved response is successful
            self.assertEqual(response[1], 200)
            
            # check that we get an expected updated score of 40
            expected = {
                'updated_score': 40
            }
            
            self.assertEqual(response[0], json.dumps(expected))
    
    # @patch('Frontend_To_Backend_Data_Passage.request') # replaces the request import with a mock import
    @patch('Backend.pymysql.connect') # replaces pymysql connect import with a mock    
    def test_active_events(self, mock_connect):
        # replaces request.json function with a mock fcn that returns
        # hard-coded dict
        # mock_request.json = MagicMock(return_value={"username": "Aaron"})
        with app.test_request_context(
        "/api/Active_Events?username=Aaron", method="GET", json={"username": "Aaron"}
        ):
        
            # setting up the mock cursor with mock values and fcns
            mock_cursor = MagicMock()
            mock_cursor.close = MagicMock()
            fetchoneDicts = [{"u_id": 1},
                            {"l_lat": 43.0719, "l_long": -89.408, "l_name": "Union South"},
                            {"l_lat": 43.0757, "l_long": -89.4040, "l_name": "Bascom Hall"}]
            completedEventDicts = [{"completes_e_id": 2},
                                {"completes_e_id": 3}]
            uncompletedEventDicts = [{"e_id": 4, "e_name": "four", "l_id": 4, "e_score": 10, "e_desc": "the number after three"},
                                    {"e_id": 5, "e_name": "five", "l_id": 5, "e_score": 20, "e_desc": "the number after four"}]
            mock_cursor.execute = MagicMock()
            mock_cursor.fetchone = MagicMock(side_effect=fetchoneDicts)
            mock_cursor.fetchall = MagicMock(side_effect=[completedEventDicts, uncompletedEventDicts])
            
            # attaching the mock cursor to the mock connection 
            mock_connect.return_value = MagicMock()
            mock_connect.return_value.cursor = MagicMock(return_value=mock_cursor)
            mock_connect.return_value.close = MagicMock()
            
            # gets the response by calling the test client
            # note: this response is not a mock
            response = Active_Events()
            
            expected = [
                {
                    "event_id": 4,
                    "lat": 43,
                    "long": -89,
                    "location_name": "Union South",
                    "event_score": 10, 
                    "event_name": "four",
                    "event_description": "the number after three"
                },
                {
                    "event_id": 5,
                    "lat": 43,
                    "long": -89,
                    "location_name": "Bascom Hall",
                    "event_score": 20, 
                    "event_name": "five",
                    "event_description": "the number after four"
                }
            ]
            
            self.assertEqual(response, json.dumps(expected))
        
        
    # @patch('Frontend_To_Backend_Data_Passage.request') # replaces the request import with a mock import
    @patch('Backend.pymysql.connect') # replaces pymysql connect import with a mock 
    def test_get_user_achievements(self, mock_connect):
        # replaces request.json function with a mock fcn that returns
        # # hard-coded dict
        # mock_request.json = MagicMock(return_value={"username": "Aaron"})
        
        with app.test_request_context(
        "/api/Get_User_Achievements?username=Aaron", method="GET", json={"username": "Aaron"}
        ):
        
            # Case 1: User has uncompleted achievements
            mock_cursor = MagicMock()
            mock_cursor.execute = MagicMock()
            # Setting up mock data to be returned by fetchall() calls
            fetchallResults = [
                {
                    "achieves_a_id": 1
                },
                {
                    "achieves_a_id": 2
                },
                {
                    "achieves_a_id": 3
                },
                {
                    "achieves_a_id": 4
                }
            ]
            
            # Setting up mock data to be returned by fetchone() calls
            fetchoneResults = [
                {
                    "u_id": 1
                },
                {
                    "u_score": 75
                },
                {
                    "a_id": 1,
                    "a_name": "Union Yums",
                    "a_score": 5,
                    "a_desc": "Get a meal at the union"
                },
                {
                    "a_id": 2,
                    "a_name": "Pet dog",
                    "a_score": 10,
                    "a_desc": "Pet any dog!"
                },
                {
                    "a_id": 3,
                    "a_name": "Pet a cat",
                    "a_score": 20,
                    "a_desc": "Pet a cat!"
                },
                {
                    "a_id": 4,
                    "a_name": "Abe's Foot",
                    "a_score": 40,
                    "a_desc": "Rub Abe's foot for good luck!"
                }
            ]
            
            # attaching mock fetchall() and fetchone() results to the mock cursor
            mock_cursor.fetchall = MagicMock(return_value=fetchallResults)
            mock_cursor.fetchone = MagicMock(side_effect=fetchoneResults)
            mock_cursor.close = MagicMock()
            
            # attaching the mock cursor to the mock connection returned by 
            # pymysql.connect
            mock_connect.return_value = MagicMock()
            mock_connect.return_value.cursor = MagicMock(return_value=mock_cursor)
            mock_connect.return_value.close = MagicMock()
            
            response1 = Get_User_Achievements()
            
            # the achievements we expect to be completed based on the mock
            # data defined
            complete_achievements = [
                {
                'achievement_id': 1,
                'achievement_name': "Union Yums",
                'achievement_score': 5,
                'achievement_description': "Get a meal at the union"
                },
                {
                'achievement_id': 2,
                'achievement_name': "Pet dog",
                'achievement_score': 10,
                'achievement_description': "Pet any dog!"
                },
                {
                'achievement_id': 3,
                'achievement_name': "Pet a cat",
                'achievement_score': 20,
                'achievement_description': "Pet a cat!"
                },
                {
                'achievement_id': 4,
                'achievement_name': "Abe's Foot",
                'achievement_score': 40,
                'achievement_description': "Rub Abe's foot for good luck!"
                }
            ]
            
            expected = {
            'username': "Aaron",
            'user_score': 75,
            'completed_achievements': complete_achievements
            }
            
            # checking for success code
            self.assertEqual(response1[1], 200)
            self.assertEqual(response1[0], json.dumps(expected))
    
    @patch('Backend.pymysql.connect') # replaces pymysql connect import with a mock 
    def test_get_completed_events(self, mock_connect):
        with app.test_request_context(
        "/api/Get_Completed_Events?username=Aaron", method="GET", json={"username": "Aaron"}
        ):
            mock_cursor = MagicMock()
            mock_cursor.execute = MagicMock()
            # setting up mock data to be returned by fetchone() calls
            fetchoneResults = [
                {
                    "u_id": 1
                },
                {
                    "l_lat": 5,
                    "l_long": 7,
                    "l_name": "This Street"
                },
                {
                    "l_lat": 10,
                    "l_long": 1,
                    "l_name": "Other Street"
                }
            ]
            
            # setting up mock data to be returned by fetchall() calls
            fetchallResults = [
                [
                    {
                        "completes_e_id": 1
                    },
                    {
                        "completes_e_id": 2
                    }
                ],
                [
                    {
                        "e_id": 1,
                        "e_score": 10,
                        "e_name": "Dog!",
                        "e_desc": "Pet a dog",
                        "l_id": 1
                    },
                    {
                        "e_id": 2,
                        "e_score": 20,
                        "e_name": "Cat!",
                        "e_desc": "Pet a cat",
                        "l_id": 2
                    }
                ]
            ]
            
            # attaching fetchall() and fetchone() mock data to the actual
            # mock function calls
            mock_cursor.fetchone = MagicMock(side_effect=fetchoneResults)
            mock_cursor.fetchall = MagicMock(side_effect=fetchallResults)
            mock_cursor.close = MagicMock()
            
            # attaching the mock cursor to the mock connection returned by 
            # pymysql.connect
            mock_connect.return_value = MagicMock()
            mock_connect.return_value.cursor = MagicMock(return_value=mock_cursor)
            mock_connect.return_value.close = MagicMock()
            
            response = Get_Completed_Events()
            
            # The expected completed event list based on the mock data defined 
            # above
            expected = [
                    {
                        "event_id": 1,
                        "lat": 5,
                        "long": 7,
                        "location_name": "This Street",
                        "event_score": 10,
                        "event_name": "Dog!",
                        "event_description": "Pet a dog"
                    },
                    {
                        "event_id": 2,
                        "lat": 10,
                        "long": 1,
                        "location_name": "Other Street",
                        "event_score": 20,
                        "event_name": "Cat!",
                        "event_description": "Pet a cat"
                    }
                ]
            
            
            
            self.assertEqual(response, json.dumps(expected))
    
    @patch('builtins.print') # mock print() method
    @patch('Backend.pymysql.connect') # replaces pymysql connect import with a mock
    def test_log_user(self, mock_connect, mock_print):
        with app.test_request_context(
        "/api/Log_User?username=Aaron", method="POST", json={"username": "Aaron"}
        ):
            # Case 1: username doesn't already exist and is registered successfully
            # setting up mock cursor which tries to query the non-existent user
            mock_cursor1 = MagicMock()
            mock_cursor1.__enter__ = MagicMock() # handles cursor calls within 'with' statements
            mock_cursor1.__enter__.return_value = MagicMock()
            mock_cursor1.__enter__.return_value.execute = MagicMock()
            # have fetchone() return None to indicate username doesn't exist
            mock_cursor1.__enter__.return_value.fetchone = MagicMock(return_value=None)
            
            # setting up mock cursor (the one used to register the user)
            mock_cursor2 = MagicMock()
            mock_cursor2.__enter__ = MagicMock()
            # sets up this cursor to basically do nothing
            mock_cursor2.__enter__.return_value = MagicMock()
            mock_cursor2.__enter__.return_value.execute = MagicMock()
            
            # attaching the mock cursor to the mock connection
            mock_connect.return_value = MagicMock()
            mock_connect.return_value.cursor = MagicMock(side_effect=[mock_cursor1, mock_cursor2])
            
            response1 = Log_User()
            
            # expecting that Aaron was not previously registered
            expected1 = {
                "username": "Aaron",
                "message": "successfully logged in"
            }
            
            self.assertEqual(response1[1], 200)
            self.assertEqual(response1[0], json.dumps(expected1))
            # ensure that a print call with this specific arg was made,
            # which verifies that the username was not already registered
            mock_print.assert_called_with('Aaron not registered in system.')
            
            # Case 2: Username already exists and is registered
            mock_cursor1 = MagicMock()
            mock_cursor1.__enter__ = MagicMock()
            mock_cursor1.__enter__.return_value = MagicMock()
            mock_cursor1.__enter__.return_value.execute = MagicMock()
            # have fetchone() return anything, as long as its not None
            fetchoneRet = {
                "attribute": "blah blah"
            }
            mock_cursor1.__enter__.return_value.fetchone = MagicMock(return_value=fetchoneRet)
            
            
            mock_connect.return_value = MagicMock()
            mock_connect.return_value.cursor = MagicMock(return_value=mock_cursor1)
            mock_connect.return_value.commit = MagicMock()
            
            response2 = Log_User()
            
            # method should print('Aaron is in system') in this case
            mock_print.assert_called_with('Aaron is in system.')
            
        # Case 3: username not provided in request
        # don't provide a username in the url parameters
        with app.test_request_context(
        "/api/Log_User", method="POST", json={"username": None}
        ):
            response3 = Log_User()
            
            self.assertEqual(response3[1], 400)
            self.assertEqual(response3[0], json.dumps({'message': 'No username provided'}))

    @patch('Backend.pymysql.connect') # replaces pymysql connect import with a mock 
    def test_get_uncompleted_achievements(self, mock_connect):
        with app.test_request_context(
        "/api/Get_Uncompleted_Achievements?username=Aaron", method="GET", json={"username": "Aaron"}
        ):
            # Case 1: User has uncompleted achievements
            mock_cursor = MagicMock()
            mock_cursor.execute = MagicMock()
            
            # setting up mock data returned by fetchall()
            # achievements with id 2 and 3 are intended to be the uncompleted ones
            fetchallResults = [
                {
                    "a_id": 1
                },
                {
                    "a_id": 2,
                    "a_name": "Pet dog",
                    "a_score": 10,
                    "a_desc": "Pet any dog!"
                },
                {
                    "a_id": 3,
                    "a_name": "Pet a cat",
                    "a_score": 20,
                    "a_desc": "Pet a cat!"
                },
                {
                    "a_id": 4
                }
            ]
            
            # setting up mock data to be returned by fetchone() calls
            # put a None in place of achievements 2 and 3 to indicate uncompleted
            fetchoneResults = [
                {
                    "a_id": 1
                },
                None,
                None,
                {
                    "a_id": 4
                }
            ]
            
            # attaching mock fetchall() and fetchone() return values to
            # the actual mock function calls
            mock_cursor.fetchall = MagicMock(return_value=fetchallResults)
            mock_cursor.fetchone = MagicMock(side_effect=fetchoneResults)
            mock_cursor.close = MagicMock()
            
            # attaching the mock cursor to the mock connection created by
            # pymysql.connect
            mock_connect.return_value = MagicMock()
            mock_connect.return_value.cursor = MagicMock(return_value=mock_cursor)
            mock_connect.return_value.close = MagicMock()
            
            response1 = Get_Uncompleted_Achievements()
            
            # the achievements we expect to be uncompleted based on the mock data
            uncomplete_achievements = [
                {
                'achievement_id': 2,
                'achievement_name': "Pet dog",
                'achievement_score': 10,
                'achievement_description': "Pet any dog!"
                },
                {
                'achievement_id': 3,
                'achievement_name': "Pet a cat",
                'achievement_score': 20,
                'achievement_description': "Pet a cat!"
                }
            ]
            
            expected = {
            'username': "Aaron",
            'uncompleted_achievements': uncomplete_achievements
            }
            
            self.assertEqual(response1[1], 200)
            self.assertEqual(response1[0], json.dumps(expected))
            
            # Case 2: User has completed all achievements
            mock_cursor = MagicMock()
            mock_cursor.execute = MagicMock()
            # setting up a bunch of sample achievements to be returned by fetchall()
            fetchallResults = [
                {
                    "a_id": 1
                },
                {
                    "a_id": 2,
                    "a_name": "Pet dog",
                    "a_score": 10,
                    "a_desc": "Pet any dog!"
                },
                {
                    "a_id": 3,
                    "a_name": "Pet a cat",
                    "a_score": 20,
                    "a_desc": "Pet a cat!"
                },
                {
                    "a_id": 4
                }
            ]
            
            # setting up mock fetchone() return data that basically
            # indicates all achievements are completed
            fetchoneResults = [
                {
                    "a_id": 1
                },
                {
                    "a_id": 2
                },
                {
                    "a_id": 3
                },
                {
                    "a_id": 4
                }
            ]
            
            # attaching above mock data to be returned by their corresponding functions
            mock_cursor.fetchall = MagicMock(return_value=fetchallResults)
            mock_cursor.fetchone = MagicMock(side_effect=fetchoneResults)
            mock_cursor.close = MagicMock()
            
            # attaching the mock cursor to the mock connection returned by
            # pymysql.connect
            mock_connect.return_value = MagicMock()
            mock_connect.return_value.cursor = MagicMock(return_value=mock_cursor)
            mock_connect.return_value.close = MagicMock()
            
            response2 = Get_Uncompleted_Achievements()
            
            # should identify all achievments as completed based on the mock data
            expected = {
            'username': "Aaron",
            'completedAchievements': 'Great job! You\'ve completed everything!!!'
            }
            
            self.assertEqual(response2[1], 400)
            self.assertEqual(response2[0], json.dumps(expected))

if __name__ == '__main__':
    unittest.main()
