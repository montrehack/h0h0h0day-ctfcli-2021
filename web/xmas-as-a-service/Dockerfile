FROM node:gallium AS base
# Friendship with npm has ended, now pnpm is my best friend
RUN npm i -g pnpm
RUN pnpm config -g set enable-pre-post-scripts true

# Prepare our working directory
RUN mkdir /app
WORKDIR /app

### FRONTEND
FROM base AS frontend

# Copy package.json & package-lock.json and install before builing to avoid having to reinstall everything on each build
COPY ./client/package* /app/
RUN pnpm install

COPY ./client/ /app/
RUN pnpm run build

### BACKEND
FROM base AS backend

# Copy package.json & package-lock.json and install before builing to avoid having to reinstall everything on each build
COPY ./server/package* /app/
RUN pnpm install

COPY ./server/ /app/
RUN pnpm run build

FROM base AS docker

RUN apt-get update
RUN apt-get install -y \
    ca-certificates \
    curl \
    gnupg \
    lsb-release
RUN curl -fsSL https://download.docker.com/linux/ubuntu/gpg | gpg --dearmor -o /usr/share/keyrings/docker-archive-keyring.gpg
RUN echo "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/docker-archive-keyring.gpg] https://download.docker.com/linux/debian $(lsb_release -cs) stable" > /etc/apt/sources.list.d/docker.list
RUN apt-get update
RUN apt-get install -y docker-ce

RUN usermod -aG docker node

FROM docker AS merged

ENV NODE_ENV production

# Install server packages in production
COPY --from=backend /app/dist /app/
RUN pnpm install

# Place the frontend in the serving folder of the backend
RUN rm -rf /app/public || true
COPY --from=frontend /app/dist /app/public

USER node
ENTRYPOINT [ "node", "main.js" ]
