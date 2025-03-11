# Use an official Node.js image as the base
FROM node:22

# Set the working directory inside the container
WORKDIR /app

# Copy package.json and package-lock.json first for better caching
COPY package.json package-lock.json* ./
COPY ./dependencies ./dependencies

# Install dependencies
RUN npm install

# Copy the rest of the project
COPY . .

# Expose port 5173 (default Vite dev server port)
EXPOSE 5173

# Default command for development mode
CMD ["npm", "run", "dev", "--", "--host"]
