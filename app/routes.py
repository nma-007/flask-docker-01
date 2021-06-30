"""Application routes."""
import uuid
import requests
from requests.exceptions import ConnectionError
from datetime import datetime as dt
from flask import current_app as app
from flask import make_response, redirect, render_template, request, url_for, jsonify

from .models import User, db


@app.errorhandler(404)
def not_found(e): 
  return render_template("404.html"),404

@app.route('/')
def home():
  return render_template("index.html")

@app.route('/sample')
def sample():
	return jsonify(
            [
                {
                "Message": "Welcome", 
                "Response Date": dt.today(), 
                "guid": uuid.uuid4()
                
            }
        ]
    )


