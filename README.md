✅ AWS Certified Solutions Architect – Associate Graduation Project
Serverless To-Do List Application
GitHub Repository: github.com/b-ilal/awssaa
Live Demo: awssaa3a.s3.us-east-1.amazonaws.com/index.html

📌 Project Overview
This project is a fully serverless To-Do List web application built on AWS, designed to demonstrate scalable, secure, and cost-efficient architectural practices. The application allows users to create, read, update (toggle), and delete tasks via a modern RESTful API, all without managing any servers.

🧱 Architecture
The app uses a serverless architecture with the following components:

Amazon API Gateway: Exposes RESTful endpoints (non-proxy integration).

AWS Lambda (Python): Handles logic for all CRUD operations (Create, Read, Update, Delete).

Amazon DynamoDB: Serverless NoSQL database to store to-do items.

Amazon S3: Hosts the static HTML/CSS/JS front-end with full CORS support for public access.

IAM: Manages permissions for Lambda to access DynamoDB securely.

⚙️ Key Features
Fully functional web UI with a responsive and animated To-Do list.

Add, delete, and toggle (mark complete/incomplete) tasks.

Dynamically fetch and render todos using JavaScript and Fetch API.

RESTful API design using method-specific resources with clean routes (e.g., /todos, /todos/{id}).

Deployed using S3 static hosting with public access policy and CORS-enabled API Gateway.

📁 Repository Contents
index.html: Frontend UI (hosted on S3).

lambda/: Contains all Lambda function code for each API method.

diagram.png: Solution architecture diagram.

README.md: Documentation and setup steps.

🎯 Learning Outcomes
Applied AWS services in a real-world serverless solution.

Designed secure, scalable APIs using best practices.

Gained experience in IAM permissions, S3 hosting, and frontend-backend integration.

Solved practical CORS and access control issues in a cloud environment.

