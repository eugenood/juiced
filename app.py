from random import randint

from pusher import pusher
from flask import Flask, render_template, request, redirect, json, url_for, send_from_directory

from room import Room


def get_configuration():

    return {

        "stage": (10, 10),
        "human": (randint(0, 10), randint(0, 10)),
        "robot": (randint(0, 10), randint(0, 10)),
        "walls": [(2, 7), (2, 6), (2, 5), (2, 4), (2, 3), (2, 2), (3, 2), (4, 2), (5, 2), (6, 2), (7, 2)],
        "cups": [(2, 0), (4, 0), (6, 0)],
        "juicers": [(2, 9), (4, 9), (6, 9)],
        "apple_storages": [((3, 0), (5, 0)), ((3, 3), (5, 3))],
        "orange_storages": [((3, 9), (5, 9)), ((5, 6), (3, 6))],

    }


app = Flask(__name__)

if app.config["DEBUG"]:
    @app.after_request
    def after_request(response):
        response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate, public, max-age=0"
        response.headers["Expires"] = 0
        response.headers["Pragma"] = "no-cache"
        return response

rooms = {}

pusher = pusher_client = pusher.Pusher(
    app_id="858327",
    key="2f3be046dd1cd0077dbf",
    secret="9ffe595c79d298bf420e",
    cluster="ap1",
    ssl=True
)


@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")


@app.route("/login", methods=["POST"])
def login():
    global rooms
    username = request.form.get("username")
    room_id = request.form.get("room_id")
    if is_valid(username, room_id):
        if room_id not in rooms:
            rooms[room_id] = Room(room_id, get_configuration())
        rooms[room_id].add_player(username)
        return redirect(url_for("room", room_id=room_id))
    return "not available"


@app.route("/room/<room_id>", methods=["GET"])
def room(room_id):
    global rooms
    state_image = json.dumps(rooms[room_id].get_state_image())
    return render_template("room.html", state_image=state_image)


@app.route('/images/<path:path>')
def images(path):
    return send_from_directory('images', path)


def is_valid(username, room_id):
    return True


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
