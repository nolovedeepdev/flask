from flask import Flask, render_template, url_for, redirect
from app import app

@app.route("/index")
@app.route("/")

def index():
    return render_template('index.html')


