import unittest
import json
from functions.validate_schema import lambda_handler

class TestValidateSchema(unittest.TestCase):
    def test_valid_schema(self):
        event = {
            'records': [
                {
                    'Name': 'John Doe',
                    'Email': 'john@example.com',
                    'Marketing Opt In': True,
                    'Marketing Interests': ['Sports', 'Technology']
                }
            ]
        }
        response = lambda_handler(event, None)
        self.assertTrue(response['isValid'])
        self.assertEqual(len(response['validRecords']), 1)
        self.assertEqual(len(response['invalidRecords']), 0)

    def test_invalid_schema(self):
        event = {
            'records': [
                {
                    'Name': 'John Doe',
                    'Email': 'not_an_email',
                    'Marketing Opt In': 'Not a boolean',
                    'Marketing Interests': 'Not a list'
                }
            ]
        }
        response = lambda_handler(event, None)
        self.assertFalse(response['isValid'])
        self.assertEqual(len(response['validRecords']), 0)
        self.assertEqual(len(response['invalidRecords']), 1)

    def test_mixed_valid_and_invalid(self):
        event = {
            'records': [
                {
                    'Name': 'John Doe',
                    'Email': 'john@example.com',
                    'Marketing Opt In': True,
                    'Marketing Interests': ['Sports', 'Technology']
                },
                {
                    'Name': 'Jane Doe',
                    'Email': 'not_an_email',
                    'Marketing Opt In': 'Not a boolean',
                    'Marketing Interests': 'Not a list'
                }
            ]
        }
        response = lambda_handler(event, None)
        self.assertFalse(response['isValid'])
        self.assertEqual(len(response['validRecords']), 1)
        self.assertEqual(len(response['invalidRecords']), 1)

    def test_no_records(self):
        event = {'records': []}
        response = lambda_handler(event, None)
        self.assertFalse(response['isValid'])
        self.assertEqual(response['error'], 'No records provided')

if __name__ == '__main__':
    unittest.main()