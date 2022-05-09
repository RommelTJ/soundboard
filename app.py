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


@app.route('/spaghet', methods=['POST'])
def spaghet():
    play("./sounds/somebody-toucha-my-spaghet.mp3")
    return ''


@app.route('/forest-fires', methods=['POST'])
def forest_fires():
    play("./sounds/forest-fires.mp3")
    return ''


@app.route('/mr-worldwide', methods=['POST'])
def mr_worldwide():
    play("./sounds/mr-worldwide.mp3")
    return ''

@app.route('/boots-of-escaping', methods=['POST'])
def boots_of_escaping():
    play("./sounds/boots-of-escaping.mp3")
    return ''


@app.route('/friday', methods=['POST'])
def friday():
    play("./sounds/friday.mp3")
    return ''


@app.route('/happy-friday-jr', methods=['POST'])
def happy_friday_jr():
    play("./sounds/happy-friday-jr.mp3")
    return ''


@app.route('/lightning-bolt', methods=['POST'])
def lightning_bolt():
    play("./sounds/lightning-bolt.mp3")
    return ''


@app.route('/magic-missile', methods=['POST'])
def magic_missile():
    play("./sounds/magic-missile.mp3")
    return ''


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port='5001')
