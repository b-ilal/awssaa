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

        body = json.loads(event['body'])

        if 'task' not in body or 'completed' not in body:
            return response(400, {"error": "Missing task or completed field"})

        table.update_item(
            Key={"id": todo_id},
            UpdateExpression="SET task = :t, completed = :c",
            ExpressionAttributeValues={
                ":t": body['task'],
                ":c": body['completed']
            }
        )

        return response(200, {"message": "Todo updated"})

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
