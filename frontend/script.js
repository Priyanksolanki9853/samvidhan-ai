// This URL must match where Member A is running the backend
const API_URL = "http://127.0.0.1:8000"; 
async function sendMessage() {
    const inputField = document.getElementById("user-input");
    const modeSelect = document.getElementById("mode-select"); // Get the switch
    const chatContainer = document.getElementById("chat-container");
    
    const message = inputField.value.trim();
    const mode = modeSelect.value; // Get the selected mode ("constitution" or "bns")

    if (message === "") return;

    // Add User Message
    addMessage(message, "user-message");
    inputField.value = "";

    // Add Loading Animation
    const loadingId = addMessage('<span class="typing-indicator">Consulting Legal Archives...</span>', "bot-message");

    try {
        // SEND MODE TO BACKEND
        const response = await fetch(`http://127.0.0.1:8000/search?query=${encodeURIComponent(message)}&mode=${mode}`);
        const data = await response.json();

        // 4. Remove "Thinking..."
        removeMessage(loadingId);
        
        // 5. Format the Answer
        // 'marked.parse' converts **bold** to <b>bold</b> and * lists to <li>
        let formattedText = "";
        if (data.result) {
            formattedText = marked.parse(data.result);
        } else {
            formattedText = "I could not find an answer.";
        }

        // Create the final HTML structure
        const finalHTML = `
            <div class="formatted-content">${formattedText}</div>
            <div class="source-citation"><small>Source: ${data.source || "Samvidhan AI Legal Database"}</small></div>
        `;

        addMessage(finalHTML, "bot-message");

    } catch (error) {
        console.error(error);
        const loadingMsg = document.getElementById(loadingId);
        if (loadingMsg) loadingMsg.remove();
        addMessage("⚠️ Connection Error. Ensure Backend is running.", "bot-message");
    }
}

function addMessage(text, className) {
    const chatBox = document.getElementById("chat-box");
    const msgDiv = document.createElement("div");
    msgDiv.className = `message ${className}`;
    msgDiv.innerHTML = text; // Using innerHTML to allow bold text/breaks
    msgDiv.id = "msg-" + Date.now();
    chatBox.appendChild(msgDiv);
    chatBox.scrollTop = chatBox.scrollHeight; // Auto-scroll to bottom
    return msgDiv.id;
}

function removeMessage(id) {
    const msg = document.getElementById(id);
    if (msg) msg.remove();
}

// Allow pressing "Enter" key to send
document.getElementById("user-input").addEventListener("keypress", function(event) {
    if (event.key === "Enter") {
        sendMessage();
    }
});