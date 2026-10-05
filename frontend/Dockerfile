FROM node:20-alpine

WORKDIR /app

# Copy dependency structures first to leverage Docker layer caching
COPY package*.json ./
RUN npm install

# Copy the rest of your local files
COPY . .

EXPOSE 5173

CMD ["npm", "run", "dev"]