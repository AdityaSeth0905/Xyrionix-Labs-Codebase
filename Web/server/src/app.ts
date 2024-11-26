import express from 'express';
import cors from 'cors';
import path from 'path';
import { config } from './config';
import helmet from 'helmet';

const app = express();

app.use(helmet());

// Safer CORS Configuration
const CORS_ORIGINS = [
  'http://localhost:3000',
  process.env.CORS_ORIGIN,
  process.env.RENDER_EXTERNAL_URL,
  process.env.RENDER_SERVICE_NAME 
    ? `https://${process.env.RENDER_SERVICE_NAME}.onrender.com` 
    : ''
].filter((origin): origin is string => 
  origin !== undefined && origin.trim() !== ''
);

app.use(cors({
  origin: CORS_ORIGINS.length > 0 ? CORS_ORIGINS : '*',
  credentials: true
}));

app.use(express.json());
app.use(express.urlencoded({ extended: true }));

// More robust static file serving
const clientBuildPath = path.resolve(__dirname, '../../frontend/dist');
console.log('Client Build Path:', clientBuildPath);

try {
  app.use(express.static(clientBuildPath));
} catch (error) {
  console.error('Error serving static files:', error);
}

// Health check route
app.get('/api/health', (_req, res) => {
  res.status(200).json({ 
    status: 'healthy', 
    environment: config.environment 
  });
});

// Catch-all route with error handling
app.get('*', (_req, res) => {
  try {
    res.sendFile(path.join(clientBuildPath, 'index.html'));
  } catch (error) {
    console.error('Error serving index.html:', error);
    res.status(500).send('Server error');
  }
});

export default app;