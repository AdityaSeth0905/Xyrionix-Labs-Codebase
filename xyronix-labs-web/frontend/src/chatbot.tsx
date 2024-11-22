import React, { useState } from 'react';

const Chatbot = () => {
  const [messages, setMessages] = useState<{ user: string; bot: string }[]>([]);
  const [input, setInput] = useState('');

  const sendMessage = async () => {
    if (!input.trim()) return;

    const userMessage = input;
    setMessages([...messages, { user: userMessage, bot: '' }]);
    setInput('');

    try {
      const response = await fetch('http://localhost:8000/chat/', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ message: userMessage }),
      });

      const data = await response.json();
      const botMessage = data.response;

      setMessages((prev) => [...prev.slice(0, -1), { user: userMessage, bot: botMessage }]);
    } catch (error) {
      setMessages((prev) => [...prev.slice(0, -1), { user: userMessage, bot: 'Error connecting to the server.' }]);
    }
  };

  return (
    <div className="chatbot">
      <div className="messages">
        {messages.map((msg, index) => (
          <div key={index}>
            <p><strong>You:</strong> {msg.user}</p>
            <p><strong>Bot:</strong> {msg.bot}</p>
          </div>
        ))}
      </div>
      <input
        type="text"
        value={input}
        onChange={(e) => setInput(e.target.value)}
        placeholder="Type a message..."
        onKeyDown={(e) => e.key === 'Enter' && sendMessage()}
      />
      <button onClick={sendMessage}>Send</button>
    </div>
  );
};

export default Chatbot;
