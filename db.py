from flask import Flask,  request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://dytsou:dyt50u@127.0.0.1:5432/testdb'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class student(db.Model):
      __tablename__ = 'students'
      sid = db.Column(db.Integer, primary_key=True)
      name = db.Column(db.String(50), nullable=False)
      tel = db.Column(db.String(50))
      addr = db.Column(db.String(200))
      email = db.Column(db.String(100))

      def __init__(self, name, tel, addr, email):
            self.name = name
            self.tel = tel
            self.addr = addr
            self.email = email

@app.route('/create')
def index():
      db.create_all()
      return "Success"

@app.route('/insert/<name>/<tel>/<addr>/<email>')
def insert(name, tel, addr, email):
      data = student(name, tel, addr, email)
      db.session.add(data)
      db.session.commit()
      return "Successfully Inserted"

if __name__ == '__main__':
      app.run()