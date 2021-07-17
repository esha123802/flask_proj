from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from send_mail import send_mail

app = Flask(__name__)

ENV = 'prod'

if ENV == 'dev':
    app.debug = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:esha@localhost/contact_esha'
else:
    app.debug = False
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://ibijivhujwxtxr:b482c2cabaed3068229ec041aa4b1324f23b17e2ce4f32cf60f2338504e43019@ec2-54-83-82-187.compute-1.amazonaws.com:5432/deqqc550fpciun'

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class ContactMe(db.Model):
    __tablename__ = 'contact'
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(100), unique = False)
    phone = db.Column(db.Integer, unique = True)
    email = db.Column(db.String(200), unique = True)
    comments = db.Column(db.Text())

    def __init__(self, name, phone, email, comments):
        self.name = name
        self.phone = phone
        self.email = email
        self.comments = comments

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    if request.method == 'POST':
        name = request.form['name']
        phone = request.form['phone']
        email = request.form['email']
        comments = request.form['comments']
        print(name,phone,email,comments)
        if phone == '' or email == '':
            return render_template('index.html', message='Enter required fields', name=request.form['name'], email=request.form['email'], phone=request.form['phone'])
        if db.session.query(ContactMe).filter(ContactMe.email == email).count() == 0 and db.session.query(ContactMe).filter(ContactMe.phone == phone).count() == 0:
            data = ContactMe(name, phone, email, comments)
            db.session.add(data)
            db.session.commit()
            send_mail(name, phone, email, comments)
            return render_template('success.html')
        return render_template('index.html', message='You have already submitted contact info.')

if __name__ == '__main__':
    app.run()

