from flask import Blueprint, render_template, request, jsonify, redirect, url_for, Flask, session, flash
from flask import app
import json

main = Blueprint('main', __name__)

@main.route('/', methods=['GET', 'POST'])
def index():
    return render_template("index.html")
