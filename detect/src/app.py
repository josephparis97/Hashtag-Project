from flask import Flask, request
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

class ImageDetection(Resource):
    def post(self):
        # print(request.files)
        res = request.files.get("fileInput")

        if not res:
            return {
                "error": "No image provided"
            }

        return {"keywords": [
            "gym",
            "fromage",
            "Aroport",
            "plage",
            "dauphin"
        ]}

api.add_resource(ImageDetection, "/image")

@app.after_request
def after_request(response):
    header = response.headers
    header['Access-Control-Allow-Origin'] = '*'
    return response

if __name__ == '__main__':
    import os
    port = os.environ.get("port", 8080)
    app.run(debug=True, port=port, host="0.0.0.0")
