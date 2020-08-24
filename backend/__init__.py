import webbrowser
from flask import Flask, jsonify, request, render_template
from time import sleep
from game import Game, Board, Cube
import json

# page setup
input_page = f''

#server setup
app = Flask(__name__)
app.config.from_object(__name__)
app.secret_key = "$2b$12$O6de.w1FB5HTnee8Ak9WLusDlGoouoVT5CAQGGEwTMfD6nUI/BUiC"
cube_list = []

def reset_input(cube_list):
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

@app.route("/start", methods=['GET', 'POST'])
def start_game():
    # create game instance
    g = Game(Board(9))
    if g.start(cube_list):
        reset_input(cube_list)
        return render_template("index.html", solved=True, cells=g.board.grid)

    return render_template("index.html")


@app.route("/reset", methods=['GET', 'POST'])
def reset_board():
    reset_input(cube_list)
    return render_template("index.html")

if __name__ == '__main__':
    app.run(debug=True)
    sleep(0.5)
    webbrowser.open("http://localhost:5000/")


