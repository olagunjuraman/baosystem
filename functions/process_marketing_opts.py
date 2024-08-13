import json
import boto3
import os

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table(os.environ['DYNAMODB_TABLE'])

def lambda_handler(event, context):
    try:
        records = event.get('body', [])
        
        processed_count = 0
        for record in records:
            if record.get('Marketing Opt In', False):
                table.put_item(
                    Item={
                        'Email': record['Email'],
                        'Name': record['Name'],
                        'MarketingInterests': record.get('Marketing Interests', [])
                    }
                )
                processed_count += 1
        
        return {
            'statusCode': 200,
            'body': json.dumps({
                'message': 'Processing completed',
                'processed_count': processed_count
            })
        }
    except Exception as e:
        print(f"Error: {str(e)}")  # This will log to CloudWatch
        return {
            'statusCode': 500,
            'body': json.dumps({'error': 'Internal server error'})
        }