import unittest
import json
from unittest.mock import patch, MagicMock
from functions.process_marketing_opts import lambda_handler

class TestProcessMarketingOpts(unittest.TestCase):
    @patch('functions.process_marketing_opts.table')
    def test_process_marketing_opts(self, mock_table):
        event = {
            'body': [
                {
                    'Email': 'john@example.com',
                    'Name': 'John',
                    'Marketing Opt In': True,
                    'Marketing Interests': ['Sports']
                },
                {
                    'Email': 'jane@example.com',
                    'Name': 'Jane',
                    'Marketing Opt In': False,
                    'Marketing Interests': ['Technology']
                }
            ]
        }
        response = lambda_handler(event, None)
        self.assertEqual(response['statusCode'], 200)
        body = json.loads(response['body'])
        self.assertEqual(body['processed_count'], 1)
        mock_table.put_item.assert_called_once_with(
            Item={
                'Email': 'john@example.com',
                'Name': 'John',
                'MarketingInterests': ['Sports']
            }
        )

    @patch('functions.process_marketing_opts.table')
    def test_no_opt_in_records(self, mock_table):
        event = {
            'body': [
                {
                    'Email': 'jane@example.com',
                    'Name': 'Jane',
                    'Marketing Opt In': False,
                    'Marketing Interests': ['Technology']
                }
            ]
        }
        response = lambda_handler(event, None)
        self.assertEqual(response['statusCode'], 200)
        body = json.loads(response['body'])
        self.assertEqual(body['processed_count'], 0)
        mock_table.put_item.assert_not_called()

    @patch('functions.process_marketing_opts.table')
    def test_error_handling(self, mock_table):
        mock_table.put_item.side_effect = Exception("Test error")
        event = {
            'body': [
                {
                    'Email': 'john@example.com',
                    'Name': 'John',
                    'Marketing Opt In': True,
                    'Marketing Interests': ['Sports']
                }
            ]
        }
        response = lambda_handler(event, None)
        self.assertEqual(response['statusCode'], 500)
        body = json.loads(response['body'])
        self.assertIn('error', body)

if __name__ == '__main__':
    unittest.main()