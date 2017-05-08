""" DESCRIPTION HERE """

from jinja2 import StrictUndefined

from flask_debugtoolbar import DebugToolbarExtension
from flask import Flask, jsonify, render_template, redirect, request, flash, session

from model import User, Contact, Relationship, ContactFrequency, Message, connect_to_db, db


app = Flask(__name__)

app.secret_key = "SOMETHINGHERE"

app.jinja_env.undefined = StrictUndefined #what does this do?