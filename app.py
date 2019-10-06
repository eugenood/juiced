from flask import Flask, json, redirect, render_template, request, send_from_directory, url_for
from flask_socketio import SocketIO

from juiced.level import Level
from server.room import Room


app = Flask(__name__, static_folder='server/static', template_folder='server/templates')
socket = SocketIO(app)
rooms = {}


@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")


@app.route("/login", methods=["POST"])
def login():
    global rooms
    username = request.form.get("username")
    room_id = request.form.get("room_id")
    if room_id not in rooms:
        level_id = "small"
        if len(room_id.split(".")) == 2:
            level_id = room_id.split(".")[1]
        rooms[room_id] = Room(room_id, Level.get_level(level_id))
    elif rooms[room_id].is_full():
        return "Room is full"
    rooms[room_id].add_player(username)
    return redirect(url_for("room", room_id=room_id, username=username))


@app.route("/room/<room_id>/<username>", methods=["GET"])
def room(room_id, username):
    global rooms
    if room_id in rooms:
        state = json.dumps(rooms[room_id].get_state(in_url=True))
        return render_template("room.html", room_id=room_id, username=username, state=state)
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
        rooms[room_id].human_act(action)
    elif username == rooms[room_id].robot_username:
        rooms[room_id].robot_act(action)
    state = json.dumps(rooms[room_id].get_state(in_url=True))
    reward = rooms[room_id].get_reward()
    rooms[room_id].dump_history()
    socket.emit('state_changed' + room_id, data=(state, reward))


if __name__ == '__main__':
    socket.run(app, host="0.0.0.0")
