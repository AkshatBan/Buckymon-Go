FROM node:alpine
WORKDIR /app
COPY frontend_2/package*.json ./
RUN npm install
COPY frontend_2 ./
EXPOSE 3000

