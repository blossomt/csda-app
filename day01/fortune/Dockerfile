FROM node:23

LABEL maintainer="blossom"

WORKDIR /app

COPY main.js .
COPY *.json .
COPY public public
COPY views views

RUN npm ci
RUN apt update && apt install -y curl

ENV APP_PORT=3000

HEALTHCHECK --interval=30s --timeout=3s --start-period=5s --retries=3 \
    CMD curl -s -f http://localhost:${APP_PORT}/health || exit 1

EXPOSE ${APP_PORT}

ENTRYPOINT node main.js