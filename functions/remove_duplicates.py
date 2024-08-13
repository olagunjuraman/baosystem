import json

def lambda_handler(event, context):
    try:
        records = event.get('validRecords', [])
        
        # Remove duplicates based on Email
        unique_records = {record['Email']: record for record in records}.values()
        
        return {
            'statusCode': 200,
            'body': list(unique_records)
        }
    except Exception as e:
        print(f"Error: {str(e)}")  # This will log to CloudWatch
        return {
            'statusCode': 500,
            'body': json.dumps({'error': 'Internal server error'})
        }