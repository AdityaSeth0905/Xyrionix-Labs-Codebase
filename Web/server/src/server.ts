import { config } from './config';
import app from './app';
import http from 'http';

const startServer = () => {
  try {
    console.log('Starting server with config:', config);

    // Safely parse the port
    const port = typeof config.port === 'string' 
      ? parseInt(config.port, 10) 
      : (config.port as number);

    // Validate port
    if (isNaN(port) || port <= 0) {
      throw new Error(`Invalid port: ${config.port}`);
    }

    const server = http.createServer(app);

    server.on('error', (error: any) => {
      if (error.code === 'EADDRINUSE') {
        console.log(`Port ${port} is busy, trying another...`);
        server.listen(0); // Automatically assign an available port
      } else {
        console.error('Server error:', error);
        process.exit(1);
      }
    });

    server.listen(port, () => {
      const actualPort = (server.address() as any).port;
      console.log(`Server running on port ${actualPort}`);
      console.log(`Environment: ${config.environment}`);
    });

    return server;
  } catch (error) {
    console.error('Failed to start server:', error);
    process.exit(1);
  }
};

const server = startServer();

// Optional: Handle process termination
process.on('SIGTERM', () => {
  console.log('SIGTERM received. Shutting down gracefully');
  server?.close(() => {
    console.log('Process terminated');
    process.exit(0);
  });
});

export default server;