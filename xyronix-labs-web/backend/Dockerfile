# Use Python base image
FROM python:3.9-slim

# Set working directory
WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy source files
COPY . .

# Expose the backend port
EXPOSE 8000

# Run FastAPI with uvloop for better performance
CMD ["uvicorn", "src.chatbot:app", "--host", "0.0.0.0", "--port", "8000", "--reload", "--loop", "uvloop"]
