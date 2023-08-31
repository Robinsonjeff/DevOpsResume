from flask import Flask, jsonify
import os
from flask import Flask, flash, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine, inspect



app = Flask(__name__)
# app.secret_key = "secret_key"

# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.sqlite3'
# db = SQLAlchemy(app)

@app.route('/')
def index():
    return render_template('index.html')

# @app.route('/login', methods=["POST","GET"])



if __name__ == '__main__':
    app.run(debug=True, port=os.getenv("PORT", default=5000))
