from flask import Flask,  request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://dytsou:dyt50u@127.0.0.1:5432/testdb'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class students(db.Model):
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
      
@app.route('/updateusr/<int:uid>', methods=['GET', 'POST']) #use GET, POST method
def updateusr(uid):
      stu = students.query.get(uid)
      if request.method == "POST":
            name, tel, addr, email = "", "", "", ""
            if request.values['name'] != "":
                  name = request.values['name']
                  stu.name = name + "(modified)"
            if request.values['tel'] != "":
                  tel = request.values['tel']
                  stu.tel = tel + "(modified)"
            if request.values['addr'] != "":
                  addr = request.values['addr']
                  stu.addr = addr + "(modified)"
            if request.values['email'] != "":
                  email = request.values['email']
                  stu.email = email + "(modified)"
            print(name, tel, addr, email)
            db.session.commit()
            if name != "" or tel != "" or addr != "" or email != "":
                  return "Successfully Updated"
      return """
            <form method='post' action=''>
                  <p>name:<input type='text' name='name' /></p>
                  <p>tel:<input type='text' name='tel' /></p>
                  <p>addr:<input type='text' name='addr' /></p>
                  <p>email:<input type='text' name='email' /></p>
                  <p><button type='submit'>summit</button></p>
            </form>
"""

@app.route('/deleteusr/<int:uid>')
def deleteusr(uid):
      stu = students.query.get(uid)
      db.session.delete(stu)
      db.session.commit()
      return "Successfully Deleted"    

@app.route('/create')
def index():
      db.create_all()
      return "Success"

@app.route('/insert/<name>/<tel>/<addr>/<email>')
def insert(name, tel, addr, email):
      data = students(name, tel, addr, email)
      db.session.add(data)
      db.session.commit()
      return "Successfully Inserted"

@app.route('/queryall')
def queryall():
      datas = students.query.all()
      msg = ""
      for stu in datas:
            msg += f"{stu.name},{stu.tel},{stu.addr},{stu.email}<br>"
      return msg

@app.route('/queryuid/<int:uid>')
def queryusr(uid):
      stu = students.query.get(uid)
      return f"{stu.name}<br>{stu.tel}<br>{stu.addr}<br>{stu.email}"

@app.route('/queryname/<string:name>')
def queryname(name):
      stu = students.query.filter_by(name=name).first()
      return f"{stu.name}<br>{stu.tel}<br>{stu.addr}<br>{stu.email}"

if __name__ == '__main__':
      app.run()
