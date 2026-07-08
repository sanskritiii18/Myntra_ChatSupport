const socket = io();

socket.on("connect", () => {
    console.log("Connected:", socket.id);
});

function sendMessage() {
    const input = document.getElementById("messageInput");
    const message = input.value;

    socket.emit("send_message", {
        message: message
    });

    input.value = "";
}

socket.on("receive_message", (data) => {
    const messages = document.getElementById("messages");

    const li = document.createElement("li");
    li.textContent = data.message;

    messages.appendChild(li);
});