
import flask
import os
from flask import send_from_directory
from flask import Flask ,render_template,request
from flask import Flask ,render_template,request
import numpy as np
import pickle
import string
from nltk.corpus import stopwords
import nltk
from nltk.stem.porter import PorterStemmer
from flask import Flask, render_template, Response
#ps = PorterStemmer()
################################################################
from flask import Flask ,render_template
app = flask.Flask(__name__)


@app.route('/')
@app.route('/home')
def home():

    return render_template('index.html')

if __name__ == "__main__":

    app.run()
