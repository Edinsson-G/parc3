#!/usr/bin/python3

from flask import flask, request
app=Flask(__name__)

@app.route('/')
def index():
    return 'Server Works!'
