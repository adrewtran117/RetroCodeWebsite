from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def hello_world():
    title = "Hey Swaggies!"
    return render_template('home.html', title=title)

@app.route("/about")
def one():
    title = "About Us"
    return render_template('about.html', title=title)

@app.route("/game")
def two():
    title = "Games"
    return render_template('game.html', title=title)

@app.route("/hack")
def four():
    title = "Hackathon"
    return render_template('hack.html', title=title)

@app.route("/pong")
def pong():
    title = "Pong"
    return render_template('pong.html', title=title)

@app.route("/maze")
def maze():
    title = "Maze"
    return render_template('maze.html', title=title)