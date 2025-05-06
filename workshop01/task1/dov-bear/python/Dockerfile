FROM python:3.13

LABEL maintainer="blossom"

WORKDIR /app

COPY . .

RUN pip install -r requirements.txt

ENV PORT=5000
ENV INSTANCE_NAME="my_instance"
ENV INSTANCE_HASH="askjdfh"

HEALTHCHECK --interval=30s --timeout=3s --start-period=5s --retries=3 \
    CMD curl -s -f http://localhost:${PORT}/healthz || exit 1

EXPOSE ${APP_PORT}

CMD ["./run.sh"]