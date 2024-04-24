import unittest
from flask import url_for
from unittest.mock import MagicMock, patch
from Backend.py import app, Complete_Event, Get_User_Achievements, Active_Events, Get_List_Of_Locations
import json

# Uses python's unittest mocking library to mock requests to the client
class TestFlaskAPI(unittest.TestCase):

    # Sets up the testing enviroment by creating a test client
    def setUp(self):
        app.testing = True
        self.client = app.test_client()

    @patch('Frontend_To_Backend_Data_Passage.pymysql.connect') # replaces pymysql connect import with a mock    
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
                "e_desc": "House party"
            },
            {
                "e_desc": "Lamer house party"
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
                "event_desc": "House party"
            },
            {
                "id": 2,
                "lat": 11,
                "long": 8,
                "location_name": "Their house",
                "event_desc": "Lamer house party"
            }
        ]
        self.assertEqual(response, json.dumps(expected))
        
    # @patch('Frontend_To_Backend_Data_Passage.request') # replaces the request import with a mock import
    @patch('Frontend_To_Backend_Data_Passage.pymysql.connect') # replaces pymysql connect import with a mock    
    def test_complete_event(self, mock_connect):
        with app.test_request_context(
        "/api/Complete_Event", method="POST", json={"username": "Aaron",
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
    @patch('Frontend_To_Backend_Data_Passage.pymysql.connect') # replaces pymysql connect import with a mock    
    def test_active_events(self, mock_connect):
        # replaces request.json function with a mock fcn that returns
        # hard-coded dict
        # mock_request.json = MagicMock(return_value={"username": "Aaron"})
        with app.test_request_context(
        "/api/Active_Events", method="GET", json={"username": "Aaron"}
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
                    "event_description": "the number after three"
                },
                {
                    "event_id": 5,
                    "lat": 43,
                    "long": -89,
                    "location_name": "Bascom Hall",
                    "event_score": 20, 
                    "event_description": "the number after four"
                }
            ]
            
            self.assertEqual(response, json.dumps(expected))
        
        
    # @patch('Frontend_To_Backend_Data_Passage.request') # replaces the request import with a mock import
    @patch('Frontend_To_Backend_Data_Passage.pymysql.connect') # replaces pymysql connect import with a mock 
    def test_get_user_achievements(self, mock_connect):
        # replaces request.json function with a mock fcn that returns
        # # hard-coded dict
        # mock_request.json = MagicMock(return_value={"username": "Aaron"})
        
        with app.test_request_context(
        "/api/Get_User_Achievements", method="GET", json={"username": "Aaron"}
        ):
        
            # mock uses of connection.cursor() fcn and its execute, fetchone,
            # and fetchall fcns
            # mock_cursor1 mocks the first cursor() call
            mock_cursor1 = MagicMock()
            mock_cursor1.__enter__ = MagicMock()
            mock_cursor1.__enter__.return_value = MagicMock()
            mock_cursor1.__enter__.return_value.execute = MagicMock()
            # mock cursor.fetchone, having it return hardcoded dict
            mock_cursor1.__enter__.return_value.fetchone = MagicMock()
            mock_cursor1.__enter__.return_value.fetchone.return_value = {"u_id": 1, "u_score": 30}
            
            # mock_cursor2 mocks the second cursor() call
            mock_cursor2 = MagicMock()
            mock_cursor2.__enter__ = MagicMock()
            mock_cursor2.__enter__.return_value = MagicMock()
            mock_cursor2.__enter__.return_value.execute = MagicMock()
            # mock cursor.fetchall, having it return list of hardcoded dict
            dictList = []
            dict1 = {"achieves_a_id": 1}
            dict2 = {"achieves_a_id": 2}
            dictList.append(dict1)
            dictList.append(dict2)
            fetchallMock = MagicMock(return_value=dictList)
            mock_cursor2.__enter__.return_value.fetchall = fetchallMock
            
            # mock_cursor3 mocks the third cursor() call (within the achieved loop)
            mock_cursor3 = MagicMock()
            mock_cursor3.__enter__ = MagicMock()
            mock_cursor3.__enter__.return_value = MagicMock()
            mock_cursor3.__enter__.return_value.execute = MagicMock()
            # mock cursor.fetchone, having it return hardcoded dict
            fetchoneMock = MagicMock(return_value={"a_id": 1, 
                                                "a_name": "first",
                                                "a_score": 10,
                                                "a_desc": "first achev"})
            mock_cursor3.__enter__.return_value.fetchone = fetchoneMock
            
            # mock_cursor4 mocks the fourth cursor() call 
            # (2nd one within the achieved loop)
            mock_cursor4 = MagicMock()
            mock_cursor4.__enter__ = MagicMock()
            mock_cursor4.__enter__.return_value = MagicMock()
            mock_cursor4.__enter__.return_value.execute = MagicMock()
            # mock cursor.fetchone, having it return hardcoded dict
            fetchoneMock = MagicMock(return_value={"a_id": 2, 
                                                "a_name": "second",
                                                "a_score": 20,
                                                "a_desc": "second achev"})
            mock_cursor4.__enter__.return_value.fetchone = fetchoneMock
            
            # mocks connection(), having it return a different mock cursor 
            # depending on when it is called
            mock_conn1 = MagicMock()
            mock_conn1.cursor = MagicMock(side_effect=[mock_cursor1, mock_cursor2])
                
            mock_conn2 = MagicMock()
            mock_conn2.cursor = MagicMock(return_value=mock_cursor3)
            mock_conn3 = MagicMock()
            mock_conn3.cursor = MagicMock(return_value=mock_cursor4)
            
            cursorMocks = [mock_cursor1, mock_cursor2, mock_cursor3, mock_cursor4]
            mockConnList = [mock_conn1, mock_conn2, mock_conn3]
            # mock_connect.return_value = mock_conn1
            mock_connect.side_effect = mockConnList
            
            # gets the response by calling the test client
            # note: this response is not a mock
            response = Get_User_Achievements()
            
            # assert that the retrieved response is successful
            self.assertEqual(response[1], 200)
            
            # assert that connection() and cursor()
            # functions were called the appropriate number of times
            self.assertEqual(mock_connect.call_count, 3)
            self.assertEqual(mock_conn1.cursor.call_count, 2)
            self.assertEqual(mock_conn2.cursor.call_count, 1)
            self.assertEqual(mock_conn3.cursor.call_count, 1)
            
            # check that we get the expected result
            achiev1 = {
                "achievement_id": 1,
                "achievement_name": "first",
                "achievement_score": 10,
                "achievement_description": "first achev"
            }
            achiev2 = {
                "achievement_id": 2,
                "achievement_name": "second",
                "achievement_score": 20,
                "achievement_description": "second achev"
            }
            completedAchievements = [achiev1, achiev2]
            
            expected = {
                "username": "Aaron",
                "user_score" : 30,
                "completed_achievements": completedAchievements
            }
            self.assertEqual(response[0], json.dumps(expected))


if __name__ == '__main__':
    unittest.main()
