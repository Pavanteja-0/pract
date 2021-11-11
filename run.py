##     Import Libraries & Modules  ##
from flask import Flask, app
from flask_sqlalchemy import SQLAlchemy

from flask_mail import Message, Mail
mail = Mail()


db = SQLAlchemy()
    






def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'devkey'
    app.config["MAIL_SERVER"] = "smtp.gmail.com"
    app.config["MAIL_PORT"] = 465
    app.config["MAIL_USE_SSL"] = True
    app.config["MAIL_USERNAME"] = 'pavanteja14@gmail.com'
    app.config["MAIL_PASSWORD"] = 'fuckme@10PM'
    app.config["SQLALCHEMY_DATABASE_URI"] = 'postgres://aggkiewrrulmjn:e9d157f1b605d8217003576a9f77063ec8a619befb50cff6bed4dfb9de16d2e9@ec2-44-194-232-228.compute-1.amazonaws.com:5432/db88u06ct8an7e'
    mail.init_app(app)
    


    

    db.init_app(app)
    from project.main import main as main_blueprint
    app.register_blueprint(main_blueprint)


    class User(db.Model):
        id = db.Column(db.String(256), primary_key=True)
        email = db.Column(db.String(256), unique=True)
        name = db.Column(db.String(256))


    

    return app
