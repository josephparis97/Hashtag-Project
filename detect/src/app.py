from bottle import route, run, post, request

@route('/')
def index():
    return {"data":"Hello world!"}

@post("/image")
def image():
    res = request.files.get("image")
    if not res:
        return {
            "error": "No image provided"
        }

    return {"keywords": [
        "gym",
        "fromage",
        "Aéroport",
        "plage",
        "dauphin"
    ]}

if __name__ == "__main__":
    import os
    port = os.environ.get("port", 8080)
    run(host='0.0.0.0', port=port)
