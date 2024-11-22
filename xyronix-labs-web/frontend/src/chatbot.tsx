import React, { useState } from 'react';
import './Chatbot.css';

const Chatbot: React.FC = () => {
  const [isOpen, setIsOpen] = useState(false);
  const [userInput, setUserInput] = useState('');
  const [chatResponse, setChatResponse] = useState('');

  const toggleChatbot = () => setIsOpen(!isOpen);

  const handleUserInput = async () => {
    try {
      const response = await fetch('http://localhost:8000/chat', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ message: userInput }),
      });
      const data = await response.json();
      setChatResponse(data.response);
      setUserInput(''); // Clear input after sending
    } catch (error) {
      console.error('Error communicating with chatbot API:', error);
      setChatResponse('Sorry, there was an error.');
    }
  };

  return (
    <div className="chatbot-container">
      {/* Chatbot Toggle Button */}
      <button className="chatbot-icon" onClick={toggleChatbot}>
        💬
      </button>

      {/* Chatbot Popup */}
      {isOpen && (
        <div className="chatbot">
          <div className="chatbot-header">
            <h2>Chat with Us</h2>
            <button className="close-button" onClick={toggleChatbot}>
              X
            </button>
          </div>
          <div className="chatbot-body">
            <input
              type="text"
              value={userInput}
              placeholder="Type your message..."
              onChange={(e) => setUserInput(e.target.value)}
            />
            <button onClick={handleUserInput}>Send</button>
          </div>
          <div className="chatbot-response">
            <strong>Response:</strong> {chatResponse}
          </div>
        </div>
      )}
    </div>
  );
};

export default Chatbot;
