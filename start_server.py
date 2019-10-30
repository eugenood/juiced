from flask import Flask, redirect, render_template, request, send_from_directory, url_for
from flask_socketio import SocketIO

from juiced.level import Level
from juiced.metadata import Metadata
from server.room import Room


app = Flask(__name__, static_folder="server/static", template_folder="server/templates")
socket = SocketIO(app)
rooms = {}


@app.route("/", methods=["GET"])
def index():

    return render_template("index.html")


@app.route("/assets/<path:path>")
def assets(path):

    return send_from_directory("juiced/assets", path)


@app.route("/login", methods=["POST"])
def login():

    username = request.form.get("username")
    room_id = request.form.get("room_id")

    if username == "":
        return "Please enter a username."

    if room_id == "":
        return "Please enter a room ID."

    if room_id in rooms and rooms[room_id].is_full():
        return "Room is full. Please try another room."

    if room_id in rooms and rooms[room_id].human_username == username:
        return "Someone with the same username is in the room. Please try another username."

    if room_id not in rooms:

        level_id = room_id.split(".")[1] if len(room_id.split(".")) == 2 else "default"
        rooms[room_id] = Room(room_id, level_id)

    rooms[room_id].add_player(username)

    return redirect(url_for("room", room_id=room_id, username=username))


@app.route("/room/<room_id>/<username>", methods=["GET"])
def room(room_id, username):

    if room_id not in rooms:
        return "Room not found. Please login from the main page."

    return render_template("room.html", room_id=room_id, username=username)


@socket.on("user_entered")
def handle_user_entered(req):

    room_id = req["room_id"]
    room = rooms[room_id]

    human_username = room.human_username
    robot_username = room.robot_username
    state = room.get_state()
    assets_urls = list(map(lambda entry : "/../../../assets/" + entry.url, Metadata.entries))

    socket.emit("user_changed:" + room_id, data=(human_username, robot_username, state, assets_urls))


@socket.on("action_performed")
def handle_action_performed(req):

    room_id = req["room_id"]
    username = req["username"]
    action = req["action"]

    reward = 0

    if username == rooms[room_id].human_username:
        reward = rooms[room_id].human_act(action)

    elif username == rooms[room_id].robot_username:
        reward = rooms[room_id].robot_act(action)

    state = rooms[room_id].get_state()
    rooms[room_id].dump_history()
    socket.emit("state_changed:" + room_id, data=(state, reward))


if __name__ == "__main__":

    socket.run(app, host="0.0.0.0")
