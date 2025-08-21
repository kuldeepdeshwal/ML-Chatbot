document.addEventListener('DOMContentLoaded', function() {
    const chatBox = document.getElementById('chat-box');
    const userInput = document.getElementById('user-input');
    const sendBtn = document.getElementById('send-btn');

    function appendMessage(message, sender) {
        const messageDiv = document.createElement('div');
        messageDiv.classList.add(sender);
        messageDiv.innerText = message;
        chatBox.appendChild(messageDiv);
        chatBox.scrollTop = chatBox.scrollHeight;
    }

    sendBtn.addEventListener('click', async function() {
        const message = userInput.value;
        if (message.trim() === '') return;

        appendMessage(message, 'user');
        userInput.value = '';

        const response = await fetch('/chat', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ message })
        });
        const data = await response.json();
        appendMessage(data.response, 'bot');
    });

    userInput.addEventListener('keypress', function(event) {
        if (event.key === 'Enter') {
            sendBtn.click();
        }
    });
});
