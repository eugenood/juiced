window.onload = function() {

    GRID_SIZE = 30
    GRID_PADDING = 2
    BORDER_OFFSET = 4

    function initializeRoom(stateImage) {
        var board = document.getElementById('board')
        board.setAttribute('width', stateImage[0].length * GRID_SIZE + BORDER_OFFSET)
        board.setAttribute('height', stateImage.length * GRID_SIZE + BORDER_OFFSET)
        window.addEventListener('keydown', act)
        renderRoom(stateImage)
    }

    function act(event) {
        if (event.keyCode == 38) { socket.emit('action_performed', { room_id: roomId, username: username, action: 0 }) }
        if (event.keyCode == 40) { socket.emit('action_performed', { room_id: roomId, username: username, action: 1 }) }
        if (event.keyCode == 37) { socket.emit('action_performed', { room_id: roomId, username: username, action: 2 }) }
        if (event.keyCode == 39) { socket.emit('action_performed', { room_id: roomId, username: username, action: 3 }) }
        if (event.keyCode == 32) { socket.emit('action_performed', { room_id: roomId, username: username, action: 4 }) }
    }

    function renderRoom(stateImage) {
        if (board.getContext) {
            var context = board.getContext('2d')
            context.clearRect(0, 0, board.width, board.height)
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

    socket.on('user_changed', function(humanUsername, robotUsername) {
        document.getElementById('human-username').innerHTML = humanUsername
        document.getElementById('robot-username').innerHTML = robotUsername
    })

    socket.on('state_changed', function(stateImage) {
        renderRoom(JSON.parse(stateImage))
    })

    initializeRoom(stateImage)
    socket.emit('user_entered', { room_id: roomId })

}