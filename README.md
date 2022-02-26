# AWS-Lambda-API-Gateway-Website
In this project I created a simple HTML website using AWS Lambda and AWS API Gateway. AWS X-Ray is being used to trace and analyze user requests as they travel through the Amazon API Gateway to the underlying Lambda function. I also created a custom domain name for the API using Route 53 and assigned it a SSL Certificate using Certificate Manager.

Link to Website: https://api.reggiestestdomain.com/

## Website Breakdown

The website is broken down into the architecture below:

![lambda](https://github.com/rjones18/Images/blob/main/API%20Project.drawio.png)

### Language 

- HTML (Embedded into the Lambda Function) 
- Python (Used to create the Lambda Function)


### Serverless Function

- [Lambda](https://aws.amazon.com/lambda/)


### API Gateway

- [API Gateway](https://aws.amazon.com/api-gateway/)


### Distributed Tracing System

- [X-Ray](https://aws.amazon.com/xray/)


### DNS

- [Route 53](https://aws.amazon.com/route53/)

### SSL Certificate

- [Certificate Manager](https://aws.amazon.com/certificate-manager/)

