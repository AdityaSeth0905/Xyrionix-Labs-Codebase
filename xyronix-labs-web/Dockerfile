# Stage 1: Build the frontend (React + Vite)
FROM node:18 AS frontend-build

# Set working directory for frontend
WORKDIR /app/frontend

# Copy package.json and package-lock.json for frontend
COPY frontend/package*.json ./

# Install frontend dependencies
RUN npm install

# Copy the rest of the frontend application
COPY frontend ./ 

# Build the frontend (Production build for deployment)
RUN npm run build

# Stage 2: Build the backend (FastAPI + Uvicorn)
FROM python:3.9-slim AS backend-build

# Set working directory for backend
WORKDIR /app/backend

# Copy the requirements.txt for backend
COPY backend/requirements.txt ./

# Install Python dependencies for backend
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the backend source code
COPY backend ./ 

# Stage 3: Final image (combining both frontend and backend)
FROM python:3.9-slim

# Set working directory
WORKDIR /app

# Copy the built frontend assets from frontend-build stage
COPY --from=frontend-build /app/frontend/dist /app/frontend/dist

# Copy the backend code and dependencies from backend-build stage
COPY --from=backend-build /app/backend /app/backend

# Install necessary backend dependencies (Uvicorn for FastAPI)
RUN pip install uvicorn

# Install necessary dependencies to run the frontend (optional: if you want to serve the frontend directly from the backend)
RUN apt-get update && apt-get install -y \
    curl \
    && rm -rf /var/lib/apt/lists/*

# Expose the ports for frontend and backend
EXPOSE 5173 8000

# Set environment variables for frontend and backend if needed
ENV FRONTEND_PORT=5173
ENV BACKEND_PORT=8000

# Command to run both frontend (Vite) and backend (FastAPI) simultaneously
CMD ["sh", "-c", "npm --prefix /app/frontend run dev & uvicorn src.chatbot:app --host 0.0.0.0 --port 8000 --reload --loop uvloop"]
