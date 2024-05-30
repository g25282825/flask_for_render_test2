'''
from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World!'

if __name__ == '__main__':
    app.run()
'''
from flask import Flask
from waitress import serve

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

if __name__ == '__main__':
    serve(app, port=8000)    

#serve(app, listen='*:8080')   
#serve(app, host='0.0.0.0', port=8080)
