import unittest
from unittest.mock import MagicMock, patch
from Frontend_To_Backend_Data_Passage import app
import json

# Uses python's unittest mocking library to mock requests to the client
# In the future, may need to implement mocking of the sql db using other 
# libraries. 
class TestFlaskAPI(unittest.TestCase):

    # Sets up the testing enviroment by creating a test client
    def setUp(self):
        app.testing = True
        self.client = app.test_client()

    @patch('app.request') # replaces app.request json with a mock object
    def test_get_data_from_frontend(self, mock_request):
        # replaces the request.json with a json containing
        # singlular empty key-value pair
        mock_request.json = MagicMock(return_value={"key": "value"})
        
        # gets the response by calling the test client
        # note: this response is not a mock
        response = self.client.get('/api/Get_Data_From_Frontend')
        
        # asserts that the response was successful
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json, {"message": "Data received successfully"})

    @patch('app.location_data') # replaces the location data with a mock obj
    def test_post_data_to_frontend(self, mock_location_data):
        # this will be the mock data that we replace the location data with
        mock_location_data.return_value = [
            {'id': 1, 'long': -89.408, 'lat': 43.0719, 'location_name': 'Union South', 'event_desc': 'description'},
            {'id': 2, 'long': -89.404, 'lat': 43.0757, 'location_name': 'Bascom Hall', 'event_desc': 'something'}
        ]
        
        # retrieve (not mocked) response from test client
        response = self.client.get('/api/Post_Data_To_Frontend')
        
        # asser that the retrieved response is successful
        self.assertEqual(response.status_code, 200)
        
        # make sure that we're actually getting json data and that
        # there is only 2 items (since our mock only has 2)
        self.assertTrue(isinstance(response.json, list))
        self.assertEqual(len(response.json), 2)
        
    @patch('app.request') # replaces the request import with a mock import
    @patch('app.pymysql.connect') # replaces pymysql connect import with a mock 
    def Test_Get_User_Achievements(self, mock_request, mock_connect):
        # replaces request.json function with a mock fcn that returns
        # hard-coded dict
        mock_request.json = MagicMock(return_value={"username": "Aaron"})
        
        # mock uses of connection.cursor() fcn and its execute, fetchone,
        # and fetchall fcns
        # mock_cursor1 mocks the first cursor() call
        mock_cursor1 = MagicMock()
        mock_cursor1.execute = MagicMock()
        # mock cursor.fetchone, having it return hardcoded dict
        fetchoneMock = MagicMock(return_value={"u_id": 1, "u_score": 30})
        mock_cursor1.fetchone = fetchoneMock
        
        # mock_cursor2 mocks the second cursor() call
        mock_cursor2 = MagicMock()
        mock_cursor2.execute = MagicMock()
        # mock cursor.fetchall, having it return list of hardcoded dict
        dictList = []
        dict1 = {"achieves_a_id": 1}
        dict2 = {"achieves_a_id": 2}
        dictList.append(dict1)
        dictList.append(dict2)
        fetchallMock = MagicMock(return_value=dictList)
        mock_cursor2.fetchall = fetchallMock
        
        # mock_cursor3 mocks the third cursor() call (within the achieved loop)
        mock_cursor3 = MagicMock()
        mock_cursor3.execute = MagicMock()
        # mock cursor.fetchone, having it return hardcoded dict
        fetchoneMock = MagicMock(return_value={"a_id": 1, 
                                               "a_name": "first",
                                               "a_score": 10,
                                               "a_desc": "first achev"})
        mock_cursor3.fetchone = fetchoneMock
        
        # mock_cursor4 mocks the fourth cursor() call 
        # (2nd one within the achieved loop)
        mock_cursor4 = MagicMock()
        mock_cursor4.execute = MagicMock()
        # mock cursor.fetchone, having it return hardcoded dict
        fetchoneMock = MagicMock(return_value={"a_id": 2, 
                                               "a_name": "second",
                                               "a_score": 20,
                                               "a_desc": "second achev"})
        mock_cursor4.fetchone = fetchoneMock
        
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
        mock_connect.return_value = MagicMock(side_effect=mockConnList)
        
        # gets the response by calling the test client
        # note: this response is not a mock
        response = self.client.get('/api/Get_User_Achievements')
        
        # assert that the retrieved response is successful
        self.assertEqual(response.status_code, 200)
        
        # assert that connection() and cursor()
        # functions were called the appropriate number of times
        self.assertEqual(mock_connect.call_count, 3)
        self.assertEqual(mock_conn1.cursor.call_count, 2)
        self.assertEqual(mock_conn2.cursor.call_count, 1)
        self.assertEqual(mock_conn3.cursor.call_count, 1)
        
        # check that we get the expected result
        achiev1 = {
            'achievement_id': 1,
            'achievement_name': "first",
            'achievement_score': 10,
            'achievement_description': "first achev"
        }
        achiev2 = {
            'achievement_id': 2,
            'achievement_name': "second",
            'achievement_score': 20,
            'achievement_description': "second achev"
        }
        completedAchievements = [achiev1, achiev2]
        
        expected = {
            'username': "Aaron",
            'user_score' : 30,
            'completed_achievements': completedAchievements
        }
        
        self.assertEqual(response.json, json.dumps(expected))


if __name__ == '__main__':
    unittest.main()