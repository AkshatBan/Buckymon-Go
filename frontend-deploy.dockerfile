FROM node:current-alpine
ENV NODE_ENV production

RUN apk update && apk upgrade

WORKDIR /app
COPY frontend_2/package*.json ./

RUN npm install
RUN npm i -g serve

COPY frontend_2 ./
EXPOSE 3000

RUN npm run build
CMD [ "serve", "-s", "build" ]