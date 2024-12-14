import json

def lambda_handler(event,context):
    return {
        'statusCode':200
        'body': json.dumps('Hello from Our CICD github action workflow vscode')

    }
