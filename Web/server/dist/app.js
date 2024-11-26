"use strict";
var __importDefault = (this && this.__importDefault) || function (mod) {
    return (mod && mod.__esModule) ? mod : { "default": mod };
};
Object.defineProperty(exports, "__esModule", { value: true });
const express_1 = __importDefault(require("express"));
const cors_1 = __importDefault(require("cors"));
const path_1 = __importDefault(require("path"));
const config_1 = require("./config");
const helmet_1 = __importDefault(require("helmet"));
const app = (0, express_1.default)();
app.use((0, helmet_1.default)());
const CORS_ORIGINS = [
    'http://localhost:3000',
    process.env.CORS_ORIGIN,
    process.env.RENDER_EXTERNAL_URL,
    process.env.RENDER_SERVICE_NAME
        ? `https://${process.env.RENDER_SERVICE_NAME}.onrender.com`
        : ''
].filter((origin) => origin !== undefined && origin.trim() !== '');
app.use((0, cors_1.default)({
    origin: CORS_ORIGINS.length > 0 ? CORS_ORIGINS : '*',
    credentials: true
}));
app.use(express_1.default.json());
app.use(express_1.default.urlencoded({ extended: true }));
const clientBuildPath = path_1.default.resolve(__dirname, '../../frontend/dist');
console.log('Client Build Path:', clientBuildPath);
try {
    app.use(express_1.default.static(clientBuildPath));
}
catch (error) {
    console.error('Error serving static files:', error);
}
app.get('/api/health', (_req, res) => {
    res.status(200).json({
        status: 'healthy',
        environment: config_1.config.environment
    });
});
app.get('*', (_req, res) => {
    try {
        res.sendFile(path_1.default.join(clientBuildPath, 'index.html'));
    }
    catch (error) {
        console.error('Error serving index.html:', error);
        res.status(500).send('Server error');
    }
});
exports.default = app;
//# sourceMappingURL=app.js.map