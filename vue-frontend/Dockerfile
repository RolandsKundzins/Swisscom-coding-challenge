FROM node:22

WORKDIR /app

# Copy package.json and package-lock.json first for better caching
COPY package.json package-lock.json* ./
COPY ./dependencies ./dependencies

RUN npm install

COPY . .

EXPOSE 5173

CMD ["npm", "run", "dev", "--", "--host"]
