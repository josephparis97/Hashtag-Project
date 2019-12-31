import flask
from flask import render_template
from flask import request
from flask_cors import CORS
import requests

app = flask.Flask(__name__)
CORS(app, send_wildcard=True)
app.config['DEBUG'] = True

ALLOWED_EXTENSIONS = set(['jpg', 'png'])

@app.route('/', methods=['GET'])
def home():
    return render_template('index.html')

@app.route('/image', methods=['POST'])
def image():

    fileInput = request.files['fileInput']
    themeValue = request.form['themeValue']

    if fileInput and allowed_file(fileInput.filename):

        files = {'fileInput': fileInput}
        #responseFromDetectService = requests.post(url="http://localhost:8080/image", files=files).json()
        responseFromDetectService = {'keywords': ''}

        if 'keywords' in responseFromDetectService:

            print(responseFromDetectService['keywords'])
            urlForSelectorService = "http://localhost:1997/selector/" + themeValue
            print(urlForSelectorService)

            responseFromSelectorService = requests.get(url=urlForSelectorService)
            allHashtag = ''

            for key in responseFromSelectorService.json():
                hashtag = '#' + key
                allHashtag = allHashtag + ' ' + hashtag

            return allHashtag

        elif 'error' in responseFromDetectService:
            return responseFromDetectService['error']

        else:
            return 'There is a problem.<br>Please try again!'

    else:
        return "Please upload only jpg or png file."

def allowed_file(filename):
	return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.after_request
def after_request(response):
    header = response.headers
    header['Access-Control-Allow-Origin'] = '*'
    return response

if __name__ == '__main__':
    import os
    port = os.environ.get("port", 5000)
    app.run(debug=True, port=port, host="0.0.0.0")
'''
app.run(
    host=app.config.get("HOST", "0.0.0.0"),
    port=app.config.get("PORT", 5000)
)
'''