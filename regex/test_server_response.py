import unittest
from test import process_server_logs  # Importing the solution function

class TestServerResponseCount(unittest.TestCase):
    def setUp(self):
        # Set up any test-specific configuration or data
        self.log_data = """
        12:10:10 serverIP: 10.3.4.5 UIR /home/website responseCode 400 TTL : 2200
        12:10:10 serverIP: 10.3.4.4 UIR /home/website responseCode 200 TTL : 2000
        12:10:10 serverIP: 10.3.4.5 UIR /home/website responseCode 400 TTL : 2000
        """

    def test_server_response_count(self):
        # The expected outcome
        expected_counts = {
            ('10.3.4.5', '400'): 2,
            ('10.3.4.4', '200'): 1
        }

        # The actual outcome
        server_response_count = process_server_logs(self.log_data)

        # Assert that the result matches the expected outcome
        self.assertEqual(server_response_count, expected_counts)

if __name__ == '__main__':
    unittest.main()
