from flask import Flask

buttonclicks = 0

app = Flask(__name__)

@app.route('/test/')
def test():
    return app.send_static_file('pups.html')

@app.route('/Button',  methods=['POST'])
def Button():
    global buttonclicks
    print('Button wurde geklickt')
    buttonclicks = buttonclicks + 1
    print(buttonclicks)
    return 'Der Button wurde so oft geklickt: ' + str(buttonclicks)

@app.route('/')
def hello_world():
    return 'Hello, World23!'

