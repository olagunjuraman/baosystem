import json

def validate_record(record):
    required_fields = ["Name", "Email", "Marketing Opt In", "Marketing Interests"]
    
    for field in required_fields:
        if field not in record:
            return False, f"Missing required field: {field}"
    
    if not isinstance(record["Name"], str):
        return False, "Name must be a string"
    
    if not isinstance(record["Email"], str) or "@" not in record["Email"]:
        return False, "Invalid email format"
    
    if not isinstance(record["Marketing Opt In"], bool):
        return False, "Marketing Opt In must be a boolean"
    
    if not isinstance(record["Marketing Interests"], list):
        return False, "Marketing Interests must be a list"
    
    return True, "Record validation passed"

def lambda_handler(event, context):
    try:
        records = event.get('records', [])
        if not records:
            return {
                'isValid': False,
                'error': 'No records provided'
            }
        
        valid_records = []
        invalid_records = []
        
        for record in records:
            is_valid, message = validate_record(record)
            if is_valid:
                valid_records.append(record)
            else:
                invalid_records.append({"record": record, "error": message})
        
        return {
            'isValid': len(invalid_records) == 0,
            'validRecords': valid_records,
            'invalidRecords': invalid_records,
            'message': f"Validated {len(records)} records. {len(valid_records)} valid, {len(invalid_records)} invalid."
        }
    except Exception as e:
        print(f"Error: {str(e)}")  # This will log to CloudWatch
        return {
            'isValid': False,
            'error': 'Internal server error'
        }