"use strict";
var __importDefault = (this && this.__importDefault) || function (mod) {
    return (mod && mod.__esModule) ? mod : { "default": mod };
};
Object.defineProperty(exports, "__esModule", { value: true });
const express_1 = __importDefault(require("express"));
const cors_1 = __importDefault(require("cors"));
const path_1 = __importDefault(require("path"));
const fs_1 = __importDefault(require("fs"));
const app = (0, express_1.default)();
const PORT = process.env.PORT || 5000;
app.use((0, cors_1.default)());
app.use(express_1.default.json());
// Serve static files from React app
const frontendPath = path_1.default.join(__dirname, '../../frontend/dist');
const indexPath = path_1.default.join(frontendPath, 'index.html');
// Check if dist folder exists, if not, create a fallback
if (!fs_1.default.existsSync(frontendPath)) {
    console.warn('Frontend dist folder not found. Creating placeholder.');
    fs_1.default.mkdirSync(frontendPath, { recursive: true });
}
// Fallback index.html if not exists
if (!fs_1.default.existsSync(indexPath)) {
    fs_1.default.writeFileSync(indexPath, `
    <!DOCTYPE html>
    <html>
      <head><title>Xyronix Labs</title></head>
      <body>
        <div id="root">Frontend not built yet</div>
      </body>
    </html>
  `);
}
// Serve static files
app.use(express_1.default.static(frontendPath));
// API routes
app.get('/api/hello', (req, res) => {
    res.json({ message: 'Hello from Xyronix Labs Backend!' });
});
// For any other routes, serve the React app
app.get('*', (req, res) => {
    res.sendFile(indexPath);
});
app.listen(PORT, () => {
    console.log(`Server running on port ${PORT}`);
});
