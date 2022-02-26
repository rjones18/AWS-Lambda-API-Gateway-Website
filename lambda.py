import json

def lambda_handler(event, context):
    longinformation = '''
    <h1 style="color: #5e9ca0;">This website is deployed using a Lambda Function attached to a API Gateway</h1>
    <h2 style="color: #2e6c80;">How is this possible you may ask?</h2>
    <p>API Gateway provides tools for creating and documenting web APIs that route HTTP requests to Lambda functions. You can secure access to your API with authentication and authorization controls. Your APIs can serve traffic over the internet or can be accessible only within your VPC.
    '''

    return {
        "statusCode": 200,
        "headers": {'Content-Type': 'text/html'},   #it really works by Hector Duran!
        "body": longinformation
    }

