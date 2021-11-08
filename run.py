##     Import Libraries & Modules  ##
from flask import Flask, app
from flask_mail import Message, Mail
mail = Mail()





def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'devkey'
    app.config["MAIL_SERVER"] = "smtp.gmail.com"
    app.config["MAIL_PORT"] = 465
    app.config["MAIL_USE_SSL"] = True
    app.config["MAIL_USERNAME"] = 'pavanteja14@gmail.com'
    app.config["MAIL_PASSWORD"] = 'fuckme@10PM'
    mail.init_app(app)
    
    
    from project.main import main as main_blueprint
    app.register_blueprint(main_blueprint)


    

    return app
