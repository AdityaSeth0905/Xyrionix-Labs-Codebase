import express from 'express';
import path from 'path';
import cors from 'cors'; // To handle Cross-Origin Resource Sharing
import dotenv from 'dotenv'; // For environment variables

// Load environment variables from .env file
dotenv.config();

const app = express();
const port = process.env.PORT || 8000; // Use the PORT from .env, or default to 8000

// Middleware
app.use(express.json());
app.use(cors()); // Enable CORS for all routes

// Serve static files from the frontend build directory (e.g., dist for Vite)
app.use(express.static(path.join(__dirname, 'frontend', 'dist')));

// Chatbot POST route
//app.post('/chat', (req, res) => {
//  const { message } = req.body;
//
//  if (!message) {
//    return res.status(400).json({ error: 'Message is required' });
//  }

  // Logic to generate chatbot response (for now, it simply echoes the message)
//  const chatbotResponse = `You said: ${message}`;

  // Send the response
//  res.json({ response: chatbotResponse });
//});

// Serve the React frontend (SPA)
app.get('*', (req, res) => {
  res.sendFile(path.join(__dirname, 'frontend', 'dist', 'index.html'));
});

// Start the server
app.listen(port, () => {
  console.log(`Server is running at http://localhost:${port}`);
});
