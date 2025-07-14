import json
import boto3

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('todos')

def lambda_handler(event, context):
    try:
        path_params = event.get('pathParameters', {})
        todo_id = path_params.get('id')

        if not todo_id:
            return response(400, {"error": "Missing path parameter: id"})

        result = table.get_item(Key={"id": todo_id})
        item = result.get("Item")

        if not item:
            return response(404, {"error": "Todo not found"})

        return response(200, {"todo": item})

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
