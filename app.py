from flask import Flask, render_template, request
from bcrypt import hashpw, gensalt
from  databaseSetup import User, Base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


def hashedPassword(password):
    return hashpw(password, gensalt())


def matchHash(hashed, password):
    if hashpw(password, hashed) == hashed:
        return True
    else:
        return False


app = Flask(__name__)

engine = create_engine('sqlite:///blogDatabase.db')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()


@app.route('/signup', method=['post'])
def signup():
    error = None
    if request.method == "post":
        passwd = request.form['passwd']
        repasswd = request.form['repasswd']
        email = request.form['email']
        users = session.query(User).all()
        for i in users:
            if i.email == email:
                error = "Pre registerd email"
                return render_template('signup.html', error)
        if passwd == repasswd:
            hash = hashedPassword(passwd)
            newUser = User(firstName=request.form['fname'], lastName=request.form['lname'],
                           email=email, password=hash)
            session.add(newUser)
            session.commit()
            

if __name__ == '__main__':
    app.run()
