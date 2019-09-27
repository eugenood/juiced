from random import randint

from flask import Flask, json, redirect, render_template, request, send_from_directory, url_for
from flask_socketio import SocketIO

from room import Room

app = Flask(__name__)
socket = SocketIO(app)
rooms = {}


def get_configuration():
    return {
        "stage": (10, 10),
        "human": (randint(0, 9), randint(0, 9)),
        "robot": (randint(0, 9), randint(0, 9)),
        "walls": [(2, 7), (2, 6), (2, 5), (2, 4), (2, 3), (2, 2), (3, 2), (4, 2), (5, 2), (6, 2), (7, 2)],
        "cups": [(2, 0), (4, 0), (6, 0)],
        "juicers": [(2, 9), (4, 9), (6, 9)],
        "apple_storages": [((3, 0), (5, 0)), ((3, 3), (5, 3))],
        "orange_storages": [((3, 9), (5, 9)), ((5, 6), (3, 6))],
    }


@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")


@app.route("/login", methods=["POST"])
def login():
    global rooms
    username = request.form.get("username")
    room_id = request.form.get("room_id")
    if room_id not in rooms:
        rooms[room_id] = Room(room_id, get_configuration())
    elif rooms[room_id].is_full():
        return "Room is full"
    rooms[room_id].add_player(username)
    return redirect(url_for("room", room_id=room_id, username=username))


@app.route("/room/<room_id>/<username>", methods=["GET"])
def room(room_id, username):
    global rooms
    if room_id in rooms:
        state_image = json.dumps(rooms[room_id].get_state_image())
        return render_template("room.html", room_id=room_id, username=username, state_image=state_image)
    return "Room not found"


@app.route('/images/<path:path>')
def images(path):
    return send_from_directory('juiced/images', path)


@socket.on('user_entered')
def handle_user_entered(req):
    global rooms
    room_id = req["room_id"]
    human_username = rooms[room_id].human_username
    robot_username = rooms[room_id].robot_username
    socket.emit('user_changed' + room_id, data=(human_username, robot_username))


@socket.on('action_performed')
def handle_action_performed(req):
    global rooms
    room_id = req["room_id"]
    username = req["username"]
    action = req["action"]
    if username == rooms[room_id].human_username:
        rooms[room_id].stage.human.act(action)
    elif username == rooms[room_id].robot_username:
        rooms[room_id].stage.robot.act(action)
    state_image = json.dumps(rooms[room_id].get_state_image())
    socket.emit('state_changed' + room_id, state_image)


if __name__ == "__main__":
    socket.run(app, host="0.0.0.0", debug=True)
