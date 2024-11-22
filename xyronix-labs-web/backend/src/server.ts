import express from 'express';
import bodyParser from 'body-parser';

const app = express();
const port = 8000;

app.use(bodyParser.json());

// Handle POST requests to the /chat endpoint
app.post('/chat', (req, res) => {
  const userMessage = req.body.message;
  // Here, you can integrate your AI/ML model or predefined responses
  res.json({ response: `You said: ${userMessage}` });
});

app.listen(port, () => {
  console.log(`Server running at http://localhost:${port}`);
});
