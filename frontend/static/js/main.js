async function sendMessage() {
    const input = document.getElementById("user-input");
    const message = input.value.trim();
    if (!message) return;

    const chatBox = document.getElementById("chat-box");
    chatBox.innerHTML += `<p class="user">You: ${message}</p>`;

    input.value = "";

    await fetch("http://127.0.0.1:3001/chat", {
        method: "POST",
        headers: {
          "Content-Type": "application/json"
        },
        body: JSON.stringify({ message: userInput })
      });
      

    const data = await res.json();
    chatBox.innerHTML += `<p class="bot">Bot: ${data.reply}</p>`;
    chatBox.scrollTop = chatBox.scrollHeight;
}
