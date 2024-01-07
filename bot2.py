from flask import Flask, render_template, request, jsonify
import mysql.connector
from pathlib import Path

app = Flask(__name__)

# Replace the MySQL credentials with your actual MySQL database credentials

@app.route('/')
def home():
    # Create the table if it doesn't exist
   
    return render_template('website.html')
@app.route('/hope')
def hope(): 
    return render_template('hope.html')

@app.route('/signup.html')
def signup(): 
    return render_template('signup.html')

@app.route('/yolo')
def yolo(): 
    return render_template('html.html')  

@app.route('/recent') 
def sus(): 
    return render_template("suggestions.html")

@app.route('/sports')
def sports():
    return render_template("sports.html")




if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)
    print("done")