from flask import Blueprint, render_template, request, jsonify, redirect, url_for, Flask, session, flash
from flask import app
import json
from project.forms import ContactForm
from flask_mail import Message, Mail
from run import mail

main = Blueprint('main', __name__)

@main.route('/', methods=['GET', 'POST'])
def index():
    
    form = ContactForm()
    if request.method == 'POST':
      if form.validate() == False:
        flash('All fields are required.')
        return render_template("index.html", form=form)
      else:
        msg = Message(form.subject.data, sender='contact@example.com', recipients=['pavanteja14@gmail.com'])
        msg.body = """
        From: %s &lt;%s&gt;
        %s
        """ % (form.name.data, form.email.data, form.message.data)
        mail.send(msg)
        return render_template('index.html', success=True)
    elif request.method == 'GET':
      return render_template("index.html", form=form)
