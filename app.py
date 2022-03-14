from flask import Flask
from audio_player import play

app = Flask(__name__)


@app.route('/', methods=['GET'])
def index():
    return 'Hello World'


@app.route('/roasted', methods=['POST'])
def roasted():
    play("./sounds/roasted.mp3")
    return ''


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port='5001')
