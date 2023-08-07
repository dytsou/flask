from flask import Flask,  request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import text

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://dytsou:dyt50u@127.0.0.1:5432/testdb'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

@app.route('/')
def index():
      return "db connected successfully"

@app.route('/setup')
def setup():
      sql = """
      CREATE TABLE students2 (
            sid serial NOT NULL,
            name character varying(50) NOT NULL,
            tel character varying(50),
            addr character varying(200),
            email character varying(100),
            PRIMARY KEY (sid))
      """
      db.session.execute(text(sql))
      db.session.commit()
      return "db setup successfully"

@app.route('/insert')
def insert():
      sql = """
      INSERT INTO students2 (name, tel, addr, email)
      VALUES ('John', '12345678', 'Taipei', 'John@mail.org')
      """
      db.session.execute(text(sql))
      db.session.commit()
      return "db insert successfully"

@app.route('/update/<int:uid>')
def update(uid):
      sql = "UPDATE students2 SET addr = 'Kaohsiung(modified)' WHERE sid = " + str(uid)
      db.session.execute(text(sql))
      db.session.commit()
      return "db update successfully"

if __name__ == '__main__':
      app.run()
