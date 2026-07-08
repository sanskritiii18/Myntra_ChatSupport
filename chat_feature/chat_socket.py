def register_chat_socket(socketio):

    @socketio.on("connect")
    def handle_connect():
        print("Client connected")

    @socketio.on("send_message")
    def handle_message(data):
        print("Message received:", data)

        socketio.emit("receive_message", {
            "message": data["message"]
        })