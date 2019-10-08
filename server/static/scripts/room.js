window.onload = function() {

    GRID_SIZE = 30

    var socket = io.connect()
    var isInitialized = false

    var assets = []
    var numAssetsLoaded = 0

    socket.emit("user_entered", { room_id: roomId })

    socket.on("user_changed:" + roomId, function(humanUsername, robotUsername, state, assetsUrls) {

        if (isInitialized) return;

        document.getElementById("human-username").innerHTML = humanUsername
        document.getElementById("robot-username").innerHTML = robotUsername

        if (humanUsername !== null && robotUsername !== null) initializeRoom(state, assetsUrls)

    })

    socket.on("state_changed:" + roomId, function(state) {

        drawBoard(state)

    })

    function initializeRoom(state, assetsUrls) {

        initializeBoard(state, assetsUrls)
        initializeEvents()

        var board = document.getElementById("board")
        board.setAttribute("width", state[0].length * GRID_SIZE)
        board.setAttribute("height", state.length * GRID_SIZE)

        isInitialized = true
        document.getElementById("message").innerHTML = "Time to get juicy!"

    }

    function initializeBoard(state, assetsUrls) {

        function createClosure(i, image) {

            return function() {

                assets[i] = image
                numAssetsLoaded = numAssetsLoaded + 1

                if (numAssetsLoaded === assetsUrls.length) { drawBoard(state) }

            }

        }

        for (var i = 0; i < assetsUrls.length; i++) {

            var image = new Image()
            image.src = assetsUrls[i]
            image.onload = createClosure(i, image)

        }

    }

    function initializeEvents() {

        window.addEventListener("keyup", function(event) {

            if (event.keyCode == 38) act("up")
            if (event.keyCode == 40) act("down")
            if (event.keyCode == 37) act("left")
            if (event.keyCode == 39) act("right")
            if (event.keyCode == 32) act("interact")

        })

        document.getElementById("button-up").addEventListener("click", function() { act("up") })
        document.getElementById("button-down").addEventListener("click", function() { act("down") })
        document.getElementById("button-left").addEventListener("click", function() { act("left") })
        document.getElementById("button-right").addEventListener("click", function() { act("right") })
        document.getElementById("button-interact").addEventListener("click", function() { act("interact") })

    }

    function act(action) {

        var action_mapping = { "up": 1, "down": 2, "left": 3, "right": 4, "interact": 5 }
        socket.emit("action_performed", { room_id: roomId, username: username, action: action_mapping[action] })

    }

    function drawBoard(state) {

        var context = document.getElementById("board").getContext("2d")

        for (var i = 0; i < state.length; i++) {

            for (var j = 0; j < state[i].length; j++) {

                context.drawImage(assets[0], GRID_SIZE * j, GRID_SIZE * i, GRID_SIZE, GRID_SIZE)
                context.drawImage(assets[state[i][j]], GRID_SIZE * j, GRID_SIZE * i, GRID_SIZE, GRID_SIZE)

            }

        }

    }

}
