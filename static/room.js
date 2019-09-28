window.onload = function() {

    GRID_SIZE = 30
    GRID_PADDING = 2
    BORDER_OFFSET = 4

    function initializeRoom(stateImage) {
        var board = document.getElementById('board')
        board.setAttribute('width', stateImage[0].length * GRID_SIZE + BORDER_OFFSET)
        board.setAttribute('height', stateImage.length * GRID_SIZE + BORDER_OFFSET)
        window.addEventListener('keydown', act)
        document.getElementById('button-up').addEventListener('click', moveUp)
        document.getElementById('button-down').addEventListener('click', moveDown)
        document.getElementById('button-left').addEventListener('click', moveLeft)
        document.getElementById('button-right').addEventListener('click', moveRight)
        document.getElementById('button-interact').addEventListener('click', interact)
        renderRoom(stateImage)
    }

    function act(event) {
        if (event.keyCode == 38) { moveUp() }
        if (event.keyCode == 40) { moveDown() }
        if (event.keyCode == 37) { moveLeft() }
        if (event.keyCode == 39) { moveRight() }
        if (event.keyCode == 32) { interact() }
    }

    function moveUp() {
        socket.emit('action_performed', { room_id: roomId, username: username, action: 0 })
        document.getElementById('message').innerHTML = 'Waiting for opponent...'
    }

    function moveDown() {
        socket.emit('action_performed', { room_id: roomId, username: username, action: 1 })
        document.getElementById('message').innerHTML = 'Waiting for opponent...'
    }

    function moveLeft() {
        socket.emit('action_performed', { room_id: roomId, username: username, action: 2 })
        document.getElementById('message').innerHTML = 'Waiting for opponent...'
    }

    function moveRight() {
        socket.emit('action_performed', { room_id: roomId, username: username, action: 3 })
        document.getElementById('message').innerHTML = 'Waiting for opponent...'
    }

    function interact() {
        socket.emit('action_performed', { room_id: roomId, username: username, action: 4 })
        document.getElementById('message').innerHTML = 'Waiting for opponent...'
    }

    function renderRoom(stateImage) {
        if (board.getContext) {
            var context = board.getContext('2d')
            for (var i = 0; i < stateImage.length; i++) {
                for (var j = 0; j < stateImage[i].length; j++) {
                    context.strokeRect(GRID_SIZE * j + GRID_PADDING,
                                   GRID_SIZE * i + GRID_PADDING,
                                   GRID_SIZE,
                                   GRID_SIZE)
                    var image = new Image()
                    image.src = stateImage[i][j]
                    image.onload = makeClosure(i, j, image, context)
                }
            }
        }
    }

    function makeClosure(i, j, image, context) {
        return function() {
            context.drawImage(image, GRID_SIZE * j + (GRID_PADDING * 2),
                                     GRID_SIZE * i + (GRID_PADDING * 2),
                                     GRID_SIZE - (GRID_PADDING * 2),
                                     GRID_SIZE - (GRID_PADDING * 2))
        }
    }

    var socket = io.connect()

    socket.on('user_changed' + roomId, function(humanUsername, robotUsername) {
        document.getElementById('human-username').innerHTML = humanUsername
        document.getElementById('robot-username').innerHTML = robotUsername
        if (humanUsername !== null && robotUsername !== null) {
            document.getElementById('message').innerHTML= 'Time to move!'
        }
    })

    socket.on('state_changed' + roomId, function(stateImage) {
        renderRoom(JSON.parse(stateImage))
        document.getElementById('message').innerHTML= 'Time to move!'
    })

    initializeRoom(stateImage)
    socket.emit('user_entered', { room_id: roomId })

}
