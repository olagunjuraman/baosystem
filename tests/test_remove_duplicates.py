import unittest
import json
from functions.remove_duplicates import lambda_handler

class TestRemoveDuplicates(unittest.TestCase):
    def test_remove_duplicates(self):
        event = {
            'validRecords': [
                {'Email': 'john@example.com', 'Name': 'John'},
                {'Email': 'jane@example.com', 'Name': 'Jane'},
                {'Email': 'john@example.com', 'Name': 'John Doe'}
            ]
        }
        response = lambda_handler(event, None)
        self.assertEqual(response['statusCode'], 200)
        result = response['body']
        self.assertEqual(len(result), 2)
        self.assertTrue(any(r['Name'] == 'John Doe' for r in result))

    def test_no_records(self):
        event = {'validRecords': []}
        response = lambda_handler(event, None)
        self.assertEqual(response['statusCode'], 200)
        self.assertEqual(response['body'], [])

    def test_error_handling(self):
        event = {}  # Missing 'validRecords' key
        response = lambda_handler(event, None)
        self.assertEqual(response['statusCode'], 200)
        self.assertIn('error', json.loads(response['body']))

if __name__ == '__main__':
    unittest.main()