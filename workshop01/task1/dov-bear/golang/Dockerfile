# Example of multi-stage build
# Use golang image to build
FROM golang:1.24-bookworm AS builder

WORKDIR /src

COPY go.* .
COPY *.go .

RUN go build -o main .

# Use bookworm image to build running container
FROM debian:12.10

LABEL maintainer="blossom"

WORKDIR /app

RUN apt update && apt install -y curl

# Copy compiled binary from /src/main to /app/main
COPY --from=builder /src/main .
COPY public public
COPY templates templates

ENV PORT=3000 INSTANCE_NAME="my_instance" INSTANCE_HASH="askjdfh"

HEALTHCHECK --interval=30s --timeout=3s --start-period=5s --retries=3 \
    CMD curl -s -f http://localhost:${PORT}/healthz || exit 1

EXPOSE ${APP_PORT}

SHELL [ "/bin/sh", "-c"]

ENTRYPOINT /app/main