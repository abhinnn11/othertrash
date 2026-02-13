FROM ubuntu:24.04

ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update && apt-get install -y \
    chromium-browser \
    mitmproxy \
    ca-certificates \
    python3 \
    xvfb \
    curl \
    && rm -rf /var/lib/apt/lists/*

# directory for proxy script
WORKDIR /app

COPY proxy.py /app/proxy.py

EXPOSE 8080

CMD ["bash","-c","xvfb-run -a chromium --headless --no-sandbox --disable-gpu --proxy-server=http://127.0.0.1:8080 https://example.com & mitmdump -s /app/proxy.py --listen-port 8080"]
