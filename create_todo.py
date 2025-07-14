import json
import uuid
import boto3

dynamodb = boto3.resource("dynamodb")
table = dynamodb.Table("todos")

def lambda_handler(event, context):
    print("EVENT:", event)  # For debugging in CloudWatch

    # In proxyless, 'task' comes as a top-level event field
    task = event.get("task")
    if not task:
        return response(400, {"error": "Missing 'task'"})

    item = {
        "id": str(uuid.uuid4()),
        "task": task,
        "completed": False
    }

    try:
        table.put_item(Item=item)
        return response(201, item)
    except Exception as e:
        print("DynamoDB error:", e)
        return response(500, {"error": "DB error", "details": str(e)})

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
