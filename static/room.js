GRID_SIZE = 30
GRID_PADDING = 2
BORDER_OFFSET = 4

var socket = io.connect()

socket.on("state_changed", function(state_image) {
    render_room(JSON.parse(state_image))
})

function initialize_room(state_image) {
    var board = document.getElementById('board')
    board.setAttribute('width', state_image[0].length * GRID_SIZE + BORDER_OFFSET)
    board.setAttribute('height', state_image.length * GRID_SIZE + BORDER_OFFSET)
    window.addEventListener('keydown', act)
    render_room(state_image)
}

function render_room(state_image) {
    if (board.getContext) {
        var context = board.getContext('2d')
        context.clearRect(0, 0, board.width, board.height)
        for (var i = 0; i < state_image.length; i++) {
            for (var j = 0; j < state_image[i].length; j++) {
                context.strokeRect(GRID_SIZE * j + GRID_PADDING,
                               GRID_SIZE * i + GRID_PADDING,
                               GRID_SIZE,
                               GRID_SIZE)
                var image = new Image()
                image.src = state_image[i][j]
                image.onload = image_onload(i, j, image, context)
            }
        }
    }
}

function image_onload(i, j, image, context) {
    return function() {
        context.drawImage(image, GRID_SIZE * j + (GRID_PADDING * 2),
                                 GRID_SIZE * i + (GRID_PADDING * 2),
                                 GRID_SIZE - (GRID_PADDING * 2),
                                 GRID_SIZE - (GRID_PADDING * 2))
    }
}

function act(event) {
    var action = 0
    if (event.keyCode == 38) { action = 0 }
    if (event.keyCode == 40) { action = 1 }
    if (event.keyCode == 37) { action = 2 }
    if (event.keyCode == 39) { action = 3 }
    if (event.keyCode == 32) { action = 4 }
    socket.emit('action_performed', { action: action })
}