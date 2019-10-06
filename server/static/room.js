window.onload = function() {

    GRID_SIZE = 30
    GRID_PADDING = 2
    BORDER_OFFSET = 4

    MESSAGE_ACT = 'Time to act!'

    var socket = io.connect()
    var isInitialized = false

    socket.on('user_changed' + roomId, function(humanUsername, robotUsername) {

        document.getElementById('human-username').innerHTML = humanUsername
        document.getElementById('robot-username').innerHTML = robotUsername

        if (humanUsername !== null && robotUsername !== null) {
            if (!isInitialized) {
                initializeRoom(state)
            }
        }

    })

    socket.on('state_changed' + roomId, function(state) {
        drawBoard(JSON.parse(state))
    })

    socket.emit('user_entered', { room_id: roomId })

    function initializeRoom(state) {

        document.getElementById('board').setAttribute('height', state.length * GRID_SIZE + BORDER_OFFSET)
        document.getElementById('board').setAttribute('width', state[0].length * GRID_SIZE + BORDER_OFFSET)

        drawBoard(state)

        window.addEventListener('keyup', function(event) {
            if (event.keyCode == 38) moveUp()
            if (event.keyCode == 40) moveDown()
            if (event.keyCode == 37) moveLeft()
            if (event.keyCode == 39) moveRight()
            if (event.keyCode == 32) interact()
        })

        document.getElementById('button-up').addEventListener('click', moveUp)
        document.getElementById('button-down').addEventListener('click', moveDown)
        document.getElementById('button-left').addEventListener('click', moveLeft)
        document.getElementById('button-right').addEventListener('click', moveRight)
        document.getElementById('button-interact').addEventListener('click', interact)

        isInitialized = true
        document.getElementById('message').innerHTML = 'Time to get juicy!'

    }

    function act(action) {
        socket.emit('action_performed', { room_id: roomId, username: username, action: action })
    }

    function moveUp()    { act(1) }
    function moveDown()  { act(2) }
    function moveLeft()  { act(3) }
    function moveRight() { act(4) }
    function interact()  { act(5) }

    function drawBoard(state) {

        var context = board.getContext('2d')

        for (var i = 0; i < state.length; i++)
            for (var j = 0; j < state[i].length; j++)
                drawCell(i, j, state[i][j], context)

    }

    function drawCell(i, j, imageUrl, context) {

        var image = new Image()
        image.src = imageUrl
        image.onload = onImageLoad(i, j, image, context)

    }

    function onImageLoad(i, j, image, context) {

        return function() {

            context.strokeRect(GRID_SIZE * j + GRID_PADDING,
                               GRID_SIZE * i + GRID_PADDING,
                               GRID_SIZE,
                               GRID_SIZE)

            context.drawImage(image, GRID_SIZE * j + (GRID_PADDING * 2),
                                     GRID_SIZE * i + (GRID_PADDING * 2),
                                     GRID_SIZE - (GRID_PADDING * 2),
                                     GRID_SIZE - (GRID_PADDING * 2))

        }

    }

}
