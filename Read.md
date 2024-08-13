# Customer Marketing Preferences Processing

This application processes customer marketing preference data using AWS serverless technologies. It validates input data, removes duplicates, and stores opted-in customer information in a DynamoDB table.

## Table of Contents
1. [General Information](#general-information)
2. [Architecture](#architecture)
3. [Development](#development)
4. [Deployment](#deployment)
5. [Testing](#testing)
6. [Infrastructure as Code](#infrastructure-as-code)

## General Information

This application is designed to handle customer marketing preferences. It consists of three main components:
1. ValidateSchema: Validates the input data structure
2. RemoveDuplicates: Removes duplicate records based on email
3. ProcessMarketingOpts: Stores opted-in customer data in DynamoDB

The workflow is orchestrated using AWS Step Functions.

## Architecture

- AWS API Gateway: Receives incoming data
- AWS Lambda: Processes data (3 functions)
- AWS Step Functions: Orchestrates the workflow
- Amazon DynamoDB: Stores processed data

## Development

### Prerequisites
- AWS CLI installed and configured
- AWS SAM CLI installed
- Python 3.8 or later

### Local Development
1. Clone this repository
2. Navigate to the project directory
3. Create a virtual environment:
    python -m venv venv
      # On Windows use venv\Scripts\activate

4. Install dependencies:
    pip install -r requirements.txt

5. Build the SAM application:
    sam build

6. Deploy the application:
    sam deploy --guided
