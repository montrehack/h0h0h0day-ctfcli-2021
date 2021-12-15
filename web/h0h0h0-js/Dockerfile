FROM node:lts-alpine

WORKDIR /usr/src/app
COPY --chown=node:node src/ /usr/src/app

RUN npm install

EXPOSE 8888

USER node
CMD [ "node", "index.js" ]
