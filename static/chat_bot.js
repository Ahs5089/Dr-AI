function addMessage(message, isUser) {
    const chatlogs = document.getElementById('chatlogs');
    const messageDiv = document.createElement('div');
    messageDiv.className = `message ${isUser ? 'user' : 'bot'}`;
    messageDiv.textContent = message;
    chatlogs.appendChild(messageDiv);
    chatlogs.scrollTop = chatlogs.scrollHeight;
}

function connectToDoctor() {
    // Clear previous doctor suggestions
    $('.doctor-suggestion').remove();
    
    // Add visual feedback
    addMessage("Connecting you to a licensed therapist...", false);
    
    // Simulate connection delay
    setTimeout(() => {
        addMessage("Please choose an option:", false);
        const options = `
            <div class="doctor-suggestion">
                <button class="doctor-button" onclick="bookVideoCall()">Video Consultation ($49)</button>
                <button class="doctor-button" onclick="bookChatSession()">Text Chat ($29)</button>
                <button class="doctor-button" onclick="findFreeHelp()">Find Free Resources</button>
            </div>
        `;
        $('#chatlogs').append(options);
    }, 1500);
}

function bookVideoCall() {
    window.open("https://calendly.com/your-clinic/video-consult", "_blank");
}

function bookChatSession() {
    window.open("https://your-website.com/chat-with-doctor", "_blank");
}

function findFreeHelp() {
    addMessage("Here are free resources:", false);
    const freeResources = `
        <div class="doctor-suggestion">
            <a href="https://www.samhsa.gov" target="_blank">SAMHSA National Helpline</a><br>
            <a href="https://www.7cups.com" target="_blank">Free Emotional Support</a>
        </div>
    `;
    $('#chatlogs').append(freeResources);
}

function sendMessage() {
    const userInput = $('#userInput').val();
    if (userInput.trim() === '') return;

    addMessage(userInput, true);
    $('#userInput').val('');

    $.get('/get', { msg: userInput }, function(data) {
        addMessage(data.response, false);
        if (data.emergency) {
            alert('Emergency detected! Please seek immediate help!');
        }
    });
}

$('#userInput').keypress(function(e) {
    if (e.which == 13) {
        sendMessage();
    }
});