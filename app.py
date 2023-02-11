from flask import Flask, request, jsonify, render_template, url_for
app = Flask(__name__)

@app.route('/')
def home():
    return 'Hello World'