import express from 'express';
import path from 'path';
import cors from 'cors'; // To handle Cross-Origin Resource Sharing
import dotenv from 'dotenv'; // For environment variables

// Load environment variables from .env file
dotenv.config();

const app = express();
const port = process.env.PORT || 1000; // Use the PORT from .env, or default to 1000

// Middleware
app.use(express.json()); // Parse JSON payloads
app.use(cors()); // Enable CORS for all routes

// Serve static files from the frontend build directory
const frontendPath = path.join(__dirname, 'frontend', 'dist');
app.use(express.static(frontendPath));

// Chatbot API endpoint
//app.post('/api/chat', (req, res) => {
//  const { message } = req.body;

//  if (!message) {
//    return res.status(400).json({ error: 'Message is required' });
//  }

  // Example logic for chatbot response
//  const chatbotResponse = `You said: ${message}`;

  // Send the response
//  res.json({ response: chatbotResponse });
//});

// Catch-all route to serve the React frontend
app.get('*', (req, res) => {
  res.sendFile(path.join(frontendPath, 'index.html'));
});

// Start the server
app.listen(port, () => {
  console.log(`Server is running at http://localhost:${port}`);
});
