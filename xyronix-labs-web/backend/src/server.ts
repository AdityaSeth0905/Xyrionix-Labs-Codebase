import express from 'express';
//import bodyParser from 'body-parser';

const app = express();
const port = 8000;

app.use(express.json());

app.post('/chat', (req, res) => {
  const { message } = req.body;

  // Logic to generate chatbot response
  const chatbotResponse = `You said: ${message}`;
  
  res.json({ response: chatbotResponse });
});

app.listen(8000, () => {
  console.log('Chatbot backend is running on http://localhost:8000');
});