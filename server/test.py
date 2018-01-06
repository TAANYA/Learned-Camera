#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 28 18:02:21 2017

@author: tanya
"""

from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return "hellooooo"

if __name__ == "__main__":
    app.run(port= 8000 , debug = True)