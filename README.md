# Python RestAPI with flask-restful module
November-2022

#### Scope: 
This repository contains a Python Flask application that exposes a REST API for performing basic mathematical operations. The API accepts JSON POST requests that specify the operation to be performed and the operands. The supported operations are addition, subtraction, multiplication, and division. The API returns the result of the operation as a JSON response. 

Key technical components of this web service:

- Assign endpoints for the server to hit. 
  - utilizing the flask web server to off load computation from a mobile app by relying on responses.
- Enabled users to use the web to POST requests to a server.
  - Back-end functions and classes performed the work
    - Add
    - Subtract
    - Multiply
    - Divide
 - Setup Build API model for functionality, methods, resources, params and status codes
 - Ensure erorr handling was in place for responses 
 
 #### Test Drive Development:
 -  Used VSCode IDE as my development environment. 
    - cmd to deploy locally:
      - export FLASK_APP=app.py
      - flask run
      
 -  Postman Client was used throghout this process to test API running on localhost server (POST/GET requests).
 
 #### Framework:
 Flask was used as the web framework as it includes the flask_restful module for building RestAPI seamlessly. 
 -  Api and Resource were used to setup listening API on specified PORT.  
 
 
####  Comments:
I hope other developers can use this idea to spark them to build a complex REST API with their preferred Python framework.
