# install flask-restful 
from flask import Flask, request, jsonify 
from flask_restful import Api, Resource
app = Flask(__name__)
api = Api(app)

def checkPosted(data, functionName):
    if (functionName in ("add", "subtract", "multiply")):
        if "x" not in data or "y" not in data:
            return 301
        else:
            return 200

    if (functionName == "divide"):
        if "x" not in data or "y" not in data:
            return 301
        elif data["x"] == 0 or data["y"] == 0:
            return 302
        else:
            return 200

class Add(Resource):
    def post(self):
        # passing json into post requests 
        data = request.get_json()

        # validate posted data
        status_code = checkPosted(data, "add")
        if (status_code !=200):
            mapping = {
                'Message': "Err: One or more params are missing",
                'Status Code': 301
            }
            return jsonify(mapping)
            
        # if (isinstance(x,int) and isinstance(y,int)):
        x = data["x"]
        y = data["y"]
        x = int(x)
        y = int(y)
        # result
        res = x+y
        mapping = {
                'Sum': res,
                'Status Code': 200
            }
        return jsonify(mapping)
        return app

        # if im here requests something
    def get(self):
        pass

class Subtract(Resource):
    def post(self):
        # passing json into post requests 
        data = request.get_json()

        # validate posted data
        status_code = checkPosted(data, "subtract")
        if (status_code !=200):
            mapping = {
                'Message': "Err: One or more params are missing",
                'Status Code': 301
            }
            return jsonify(mapping)
            
        # if (isinstance(x,int) and isinstance(y,int)):
        x = data["x"]
        y = data["y"]
        x = int(x)
        y = int(y)
        # result
        res = x-y
        mapping = {
                'Difference': res,
                'Status Code': 200
            }
        return jsonify(mapping)
        return app

    def get(self):
        pass

class Divide(Resource):
    def post(self):
    # passing json into post requests 
        data = request.get_json()

        # validate posted data
        status_code = checkPosted(data, "divide")
        if (status_code !=200):
            mapping = {
                'Message': "Err: One or more params are missing",
                'Status Code': 301
            }
            if (status_code == 302):
                mapping = {
                'Message': "Err: One or more params is 0",
                'Status Code': 302
                }
            return jsonify(mapping)
            
        # if (isinstance(x,int) and isinstance(y,int)):
        x = data["x"]
        y = data["y"]
        x = int(x)
        y = int(y)
        # result
        res = x // y
        mapping = {
                'Quotient': res,
                'Status Code': 200
            }
        return jsonify(mapping)
        return app

class Multiply(Resource):
    def post(self):
        # passing json into post requests 
        data = request.get_json()

        # validate posted data
        status_code = checkPosted(data, "multiply")
        if (status_code !=200):
            mapping = {
                'Message': "Err: One or more params are missing",
                'Status Code': 301
            }
            return jsonify(mapping)
            
        # if (isinstance(x,int) and isinstance(y,int)):
        x = data["x"]
        y = data["y"]
        x = int(x)
        y = int(y)
        # result
        res = x*y
        mapping = {
                'Product': res,
                'Status Code': 200
            }
        return jsonify(mapping)
        return app

        # if im here requests something
    def get(self):
        pass

# add resource and setup listening API 
api.add_resource(Add, "/add")
api.add_resource(Subtract, "/subtract")
api.add_resource(Divide, "/divide")
api.add_resource(Multiply, "/multiply")