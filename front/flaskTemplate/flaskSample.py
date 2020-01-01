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

        # On fait appel au service "detect", on gere le cas d'erreur
        try:
            responseFromDetectService = requests.post(url="http://localhost:8080/image", files=files).json()
        except:
            responseFromDetectService = {'keywords': ''}

        if 'keywords' in responseFromDetectService:

            print(responseFromDetectService['keywords'])

            urlForSelectorService = "http://localhost:1997/selector/" + themeValue
            hashtagsResult = ''

            # On fait appel au service "select", et on gere le cas d'erreur
            try:
                responseFromSelectorService = requests.get(url=urlForSelectorService)

                for key in responseFromSelectorService.json():
                    hashtag = '#' + key
                    hashtagsResult = hashtagsResult + ' ' + hashtag

            except:
                hashtagsResult = getHashtagByTheme(themeValue)

            return hashtagsResult

        elif 'error' in responseFromDetectService:
            return responseFromDetectService['error']

        else:
            return 'There is a problem.<br>Please try again!'

    else:
        return "Please upload only jpg or png file."


def allowed_file(filename):
	return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


def getHashtagByTheme(themeValue):

    hashtagsResult = ''

    if themeValue == 'friends':
        hashtagsResult = '#friend #friends #fun #funny #smile #bff #bf #gf #love #instagood #igers #friendship #party #chill #happy #cute #photooftheday #live #forever #best #bestfriend #lovethem #bestfriends #goodfriends #besties #awesome #memories #goodtimes #goodtime'
    elif themeValue == 'outfit':
        hashtagsResult = '#ootd #outfitoftheday #lookoftheday #TFLers #fashion #fashiongram #style #love #beautiful #currentlywearing #lookbook #wiwt #whatiwore #whatiworetoday #ootdshare #outfit #clothes #wiw #mylook #fashionista #todayimwearing #instastyle #instafashion #outfitpost #fashionpost #todaysoutfit #fashiondiaries'
    elif themeValue == 'sport':
        hashtagsResult = '#sports #sport #active #fit#football #soccer #basketball #futball #ball #gametime #fun #game #games #crowd #fans #play #playing #player #field #green #grass #score #goal #action #kick #throw #pass #win #winning'
    elif themeValue == 'food':
        hashtagsResult = '#food #foodporn #yum #instafood #yummy #amazing #instagood #photooftheday #sweet #dinner #lunch #breakfast #fresh #tasty #food #delish #delicious #eating #foodpic #foodpics #eat #hungry #foodgasm #hot #foods'
    elif themeValue == 'art':
        hashtagsResult = '#art #illustration #drawing #draw #picture #artist #sketch #sketchbook #paper #pen #pencil #artsy #instaart #beautiful #instagood #gallery #masterpiece #creative #photooftheday #instaartist #graphic #graphics #artoftheday'
    elif themeValue == 'music':
        hashtagsResult = '#music #genre #song #songs #melody #hiphop #rnb #pop #love #rap #dubstep #instagood #beat #beats #jam #myjam #party #partymusic #newsong #lovethissong #remix #favoritesong #bestsong #photooftheday #bumpin #repeat #listentothis #goodmusic #instamusic'
    elif themeValue == 'animal':
        hashtagsResult = '#animals #animal #pet #dog #cat #dogs #cats #photooftheday #cute #pets #instagood #animales #cute #love #nature #animallovers #pets_of_instagram #petstagram #petsagram #lovely'
    elif themeValue == 'holiday':
        hashtagsResult = '#happyholidays #holidays #holiday #vacation #winter2016 #2015 #2016 #happyholidays2016 #presents #parties #fun #happy #family #love #pink #happy #lucky #summer2016 #together'
    elif themeValue == 'nature':
        hashtagsResult = '#nature #sky #sun #summer #beach #beautiful #pretty #sunset #sunrise #blue #flowers #night #tree #twilight #clouds #beauty #light #cloudporn #photooftheday #love #green #skylovers #dusk #weather #day #red #iphonesia #mothernature'
    elif themeValue == 'love':
        hashtagsResult = '#love #couple #cute #me #girl #boy #beautiful #instagood #instalove #loveher #lovehim #pretty  #adorable #kiss #kisses #hugs #romance #forever #girlfriend #boyfriend #gf #bf #bff #together #photooftheday #happy #fun #smile #xoxo'
    else:
        hashtagsResult = 'No hashtag detected! :('

    return hashtagsResult

@app.after_request
def after_request(response):
    header = response.headers
    header['Access-Control-Allow-Origin'] = '*'
    return response

if __name__ == '__main__':
    import os
    port = os.environ.get("port", 5000)
    app.run(debug=True, port=port, host="0.0.0.0")

app.run(
    host=app.config.get("HOST", "0.0.0.0"),
    port=app.config.get("PORT", 5000)
)

