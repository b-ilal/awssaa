import json, boto3
dynamodb = boto3.resource("dynamodb")
table = dynamodb.Table("todos")

def lambda_handler(event, context):
    todo_id = event.get("id")
    if not todo_id:
        return response(400, {"error": "Missing 'id'"})
    table.delete_item(Key={"id": todo_id})
    return response(200, {"message": f"Deleted todo with id: {todo_id}"})

def response(status, body):
    return {
        "statusCode": status,
        "headers": {
            "Access-Control-Allow-Origin": "*",
            "Access-Control-Allow-Methods": "OPTIONS,POST,GET,PUT,DELETE",
            "Access-Control-Allow-Headers": "*",
            "Content-Type": "application/json"
        },
        "body": json.dumps(body)
    }
