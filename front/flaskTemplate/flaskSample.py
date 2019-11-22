import flask
from flask import render_template

app = flask.Flask(__name__)
app.config['DEBUG'] = True


@app.route('/', methods=['GET'])
def home():
    return render_template('index.html')

app.run(
    host=app.config.get("HOST", "0.0.0.0"),
    port=app.config.get("PORT", 5000)
)
