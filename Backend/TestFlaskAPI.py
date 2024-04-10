import unittest
from unittest.mock import MagicMock, patch
from app import app

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

if __name__ == '__main__':
    unittest.main()