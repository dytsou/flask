# $pip install flask
from flask import Flask   #import Flask module
from flask import render_template
app = Flask(__name__)     #set up Flask object

@app.route('/', methods=['GET']) #set web route '/'
def hello(): #set func.
    return render_template('hello.html')

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000)
