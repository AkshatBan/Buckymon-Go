import unittest
from unittest.mock import MagicMock, patch
from app import app

class TestFlaskAPI(unittest.TestCase):

    def setUp(self):
        app.testing = True
        self.client = app.test_client()

    @patch('app.request')
    def test_get_data_from_frontend(self, mock_request):
        mock_request.json = MagicMock(return_value={"key": "value"})
        response = self.client.get('/api/Get_Data_From_Frontend')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json, {"message": "Data received successfully"})

    @patch('app.location_data')
    def test_post_data_to_frontend(self, mock_location_data):
        mock_location_data.return_value = [
            {'id': 1, 'long': -89.408, 'lat': 43.0719, 'location_name': 'Union South', 'event_desc': 'description'},
            {'id': 2, 'long': -89.404, 'lat': 43.0757, 'location_name': 'Bascom Hall', 'event_desc': 'something'}
        ]
        response = self.client.get('/api/Post_Data_To_Frontend')
        self.assertEqual(response.status_code, 200)
        self.assertTrue(isinstance(response.json, list))
        self.assertEqual(len(response.json), 2)

if __name__ == '__main__':
    unittest.main()