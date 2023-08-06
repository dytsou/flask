# $pip install flask
from flask import Flask   #import Flask module
from flask import request
app = Flask(__name__)     #set up Flask object

@app.route('/', methods=['GET']) #set web route '/'
def home(): #set func.
    name = request.args.get('name')
    if name is None:
        name = 'World'
    else:
        name = name.capitalize()
    return 'Welcome {}.'.format(name)
"""
@app.route('/grape')
def grape():
    return 'Hello grape.'

@app.route('/look')
def look():
    return 'Look before you leap.'
"""
@app.route('/<string:name>')
def hello(name):
    name = name.capitalize()
    return 'Hello, {}.'.format(name)

if __name__ == '__main__':
    app.run() #run app