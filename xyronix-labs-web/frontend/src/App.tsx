import React from 'react';
import './App.css';
import Chatbot from './chatbot';

function App() {
  return (
    <div className="App">
      <header className="App-header">
        <h1>Welcome to Xyronix Labs</h1>
      </header>
      <main>
        <Chatbot />  {/* Use the chatbot component here */}
      </main>
    </div>
  )
}

export default App
