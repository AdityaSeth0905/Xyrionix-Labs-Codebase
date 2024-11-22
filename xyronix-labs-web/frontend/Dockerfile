# Use Node.js base image
FROM node:18

# Set working directory
WORKDIR /app

# Copy package.json and install dependencies
COPY package*.json ./
RUN npm install

# Copy the rest of the application
COPY . .

# Expose Vite's default development server port
EXPOSE 5173

# Run Vite development server
CMD ["npm", "run", "dev"]
