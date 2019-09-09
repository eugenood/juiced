from pusher import pusher
from flask import Flask, render_template, request, jsonify, make_response, json
from state import State
import numpy as np

INITIAL_HUMAN_LOCATION = np.array([0, 0])
INITIAL_AGENT_LOCATION = np.array([5, 5])

INITIAL_GRAPE_LOCATIONS = [np.array([1, 1]), np.array([2, 2]), np.array([3, 3]), np.array([4, 4])]
INITIAL_MANGO_LOCATIONS = [np.array([1, 4]), np.array([2, 3]), np.array([3, 2]), np.array([4, 1])]

ACTION_NO_OP = -1
ACTION_UP = 0
ACTION_DOWN = 1
ACTION_LEFT = 2
ACTION_RIGHT = 3
ACTION_SPACE = [ACTION_UP, ACTION_DOWN, ACTION_LEFT, ACTION_RIGHT]

app = Flask(__name__)

pusher = pusher_client = pusher.Pusher(
    app_id="858327",
    key="2f3be046dd1cd0077dbf",
    secret="9ffe595c79d298bf420e",
    cluster="ap1",
    ssl=True
)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/play')
def play():
    global name
    name = request.args.get('username')
    return render_template('play.html')

@app.route("/pusher/auth", methods=['POST'])
def pusher_authentication():
    auth = pusher.authenticate(
        channel=request.form['channel_name'],
        socket_id=request.form['socket_id'],
        custom_data={
            u'user_id': name,
            u'user_info': {
                u'role': u'player'
            }
        }
    )
    return json.dumps(auth)

@app.route('/start')
def start():
    global state, total_reward
    state = State(INITIAL_HUMAN_LOCATION, INITIAL_AGENT_LOCATION, INITIAL_GRAPE_LOCATIONS, INITIAL_MANGO_LOCATIONS)
    total_reward = 0
    grid = str(state.grid).replace(' ', ',')
    return grid

@app.route('/move/<action>-<player>')
def move(action, player):
    global state, total_reward
    if int(player):
        human_action = ACTION_SPACE[int(action)]
        agent_action = ACTION_NO_OP
    else:
        agent_action = ACTION_SPACE[int(action)]
        human_action = ACTION_NO_OP
    reward, next_state = state.step(human_action, agent_action)
    total_reward += reward
    state = next_state
    grid = str(state.grid).replace(' ', ',')
    return grid

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)