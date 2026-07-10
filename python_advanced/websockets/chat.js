const socket = new WebSocket("ws://localhost:8000/ws")

const display = document.getElementById("display_message")
const messageInput = document.getElementById("message_input");
const sendButton = document.getElementById("send_button");

socket.onmessage = (event) => {
    console.log(event.data);
    display.innerHTML += `<p>${event.data}</p>`;
};

sendButton.addEventListener("click", () => {
    const texte = messageInput.value;

    if (texte.trim() !== "") {
        socket.send(texte);
        messageInput.value = "";
    }
});
