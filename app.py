
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
ps = PorterStemmer()
################################################################
from flask import Flask ,render_template
app = flask.Flask(__name__)


@app.route('/')
@app.route('/home')
def home():
    #return "Hello World"
    return render_template('index.html')

@app.route('/catsordogs',methods=["POST", "GET"])
def catsordogs():
    #return "Hello World"
    return render_template('catsordogs.html')

@app.route('/facerecognition',methods=["POST", "GET"])
def facerecognition():
    #return "Hello World"
    return render_template('facerecognition.html')

@app.route('/spamhtml',methods=["POST", "GET"])
def spamhtml():
    #return "Hello World"
    return render_template('spamclassifier.html')

@app.route('/index')
def index():
    return index.html
'''

model=pickle.load(open('model.pkl','rb'))
tfidf = pickle.load(open('vectorizer.pkl','rb'))
def transform_text(text):
    text = text.lower()
    text = nltk.word_tokenize(text)
    y = []
    for i in text:
        if i.isalnum():
            y.append(i)
    text = y[:]
    y.clear()
    for i in text:
        if i not in stopwords.words('english') and i not in string.punctuation:
            y.append(i)
    text = y[:]
    y.clear()
    for i in text:
        y.append(ps.stem(i))
    return " ".join(y)
@app.route('/spampredict',methods=['POST','GET'])
def predict():
    model=pickle.load(open('model.pkl','rb'))
    tfidff = pickle.load(open('vectorizer.pkl','rb'))
    print(tfidff)
    input_sms=request.form.get('textmsg')
      # 1. preprocess
    transformed_sms = transform_text(input_sms)
    # 2. vectorize
    vector_input = tfidf.transform([transformed_sms])
    # 3. predict
    result = model.predict(vector_input)[0]
    # 4. Display
    print("vector_input===================",vector_input)
    print("result===================",result)
    if len(input_sms)>0:
        if result == 1:
            return render_template('spamclassifier.html',result2="SPAM")
        else:
            return render_template('spamclassifier.html',result2="NOT SPAM")

'''
if __name__ == "__main__":

    app.run()
