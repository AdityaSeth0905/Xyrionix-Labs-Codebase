"use strict";
var __importDefault = (this && this.__importDefault) || function (mod) {
    return (mod && mod.__esModule) ? mod : { "default": mod };
};
Object.defineProperty(exports, "__esModule", { value: true });
const config_1 = require("./config");
const app_1 = __importDefault(require("./app"));
const http_1 = __importDefault(require("http"));
const startServer = () => {
    try {
        console.log('Starting server with config:', config_1.config);
        const port = typeof config_1.config.port === 'string'
            ? parseInt(config_1.config.port, 10)
            : config_1.config.port;
        if (isNaN(port) || port <= 0) {
            throw new Error(`Invalid port: ${config_1.config.port}`);
        }
        const server = http_1.default.createServer(app_1.default);
        server.on('error', (error) => {
            if (error.code === 'EADDRINUSE') {
                console.log(`Port ${port} is busy, trying another...`);
                server.listen(0);
            }
            else {
                console.error('Server error:', error);
                process.exit(1);
            }
        });
        server.listen(port, () => {
            const actualPort = server.address().port;
            console.log(`Server running on port ${actualPort}`);
            console.log(`Environment: ${config_1.config.environment}`);
        });
        return server;
    }
    catch (error) {
        console.error('Failed to start server:', error);
        process.exit(1);
    }
};
const server = startServer();
process.on('SIGTERM', () => {
    console.log('SIGTERM received. Shutting down gracefully');
    server?.close(() => {
        console.log('Process terminated');
        process.exit(0);
    });
});
exports.default = server;
//# sourceMappingURL=server.js.map