import webbrowser
from flask import Flask, jsonify, request, render_template, redirect, url_for
from time import sleep
from game import Game, Board, Cube
from secrets import flask_secret_key
import json

#server setup
app = Flask(__name__)
app.config.from_object(__name__)
app.secret_key = flask_secret_key
cube_list = [] # TODO refactor it to a better solution user input

def reset_input():
    global cube_list
    cube_list = []

@app.route("/", methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        data = json.loads(request.data)
        sliced = tuple(data["id"])
        row, col = sliced[1], sliced[4]
        num  = data.get("num")
        if not num:
            print("Bad insert")
        else:
            c = Cube(int(col)-1, int(row)-1,int(num))
            print(f"received: {c}")
            cube_list.append(c)
    return render_template("index.html", cells=[])

@app.route("/fixed_level", methods=['GET', 'POST'])
def fixed_level():
    global cube_list
    cube_list = Game.sudoku4expert
    return redirect(url_for('start_game'))

@app.route("/start", methods=['GET', 'POST'])
def start_game():
    # create game instance
    g = Game(Board(9))
    if g.start(cube_list):
        reset_input()
        return render_template("index.html", solved=True, cells=g.board.grid)

    return render_template("index.html")


@app.route("/reset", methods=['GET', 'POST'])
def reset_board():
    reset_input()
    return render_template("index.html")


if __name__ == '__main__':
    app.run(debug=True)
    sleep(0.5)
    webbrowser.open("http://localhost:5000/")


