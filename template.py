# $pip install flask
from flask import Flask   #import Flask module
from flask import render_template
from datetime import datetime
app = Flask(__name__)     #set up Flask object

@app.route('/', methods=['GET']) #set web route '/'
def hello(): #set func.
    return render_template('hello.html')

@app.route('/hello/<string:name>')
def time(name):
    now = datetime.now() #present time
    return render_template('hello2.html', **locals())

@app.route('/img/<string:name>')
def img(name):
    now2 = datetime.now() #present time
    return render_template('hello3.html', **locals())

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000)
