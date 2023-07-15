from flask import Flask, jsonify, request, render_template, url_for
import random
import requests, json

app = Flask(  # Create a flask app
    __name__,
    template_folder='templates',  # Name of html file folder
    static_folder='static'  # Name of directory for static files
)

# Variables for tasks
image_link = "https://i.imgur.com/o9Znt5k.png"

user_bio = "Middle East Entrepreneurs of Tomorrow. Enabling the next generation of Israeli and Palestinian leaders."

posts = {
    "https://i.imgur.com/1dSgGnG.png": "The cohort of 2022!",
    "https://i.imgur.com/CPEvMk0.jpg": "MEET graduation!",
    "https://i.imgur.com/Cb7LK9o.jpg": "#MEET_HACKATHON",
    "https://i.imgur.com/S5A93Wt.jpg": "Class of 2024's Y1 closing event cohort"}


#####


@app.route('/')  # '/' for the default page
def home():
    return render_template('index.html')


@app.route('/about')  # '/' for the default page
def about():
    return render_template('about.html')


if __name__ == "__main__":  # Makes sure this is the main process
    app.run(debug=True)
