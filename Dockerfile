FROM --platform=linux/amd64 alpine:3.20.1


WORKDIR /app

RUN apk add --no-cache python3 py3-pip bash libc6-compat

COPY . .

RUN python3 -m venv venv && \
    . venv/bin/activate && \
    pip install pandas

ENV PATH="/app/venv/bin:$PATH"

RUN chmod +x /app/testlibcsv

CMD ["sh", "-c", "/app/testlibcsv"]
