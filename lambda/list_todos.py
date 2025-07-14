import json
import boto3

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('todos')

def lambda_handler(event, context):
    try:
        result = table.scan()
        items = result.get("Items", [])
        return response(200, {"todos": items})

    except Exception as e:
        return response(500, {"error": str(e)})

def response(code, body):
    return {
        "statusCode": code,
        "headers": {
            "Access-Control-Allow-Origin": "*",
            "Access-Control-Allow-Methods": "OPTIONS,POST,GET,PUT,DELETE",
            "Access-Control-Allow-Headers": "*"
        },
        "body": json.dumps(body)
    }
