FROM python:3.8 AS builder

RUN python -m venv /opt/venv
ENV PATH=/opt/venv/bin:$PATH

WORKDIR /usr/src/app
COPY requirements.txt .
RUN pip install -r requirements.txt

FROM python:3.8-slim-buster
COPY --from=builder /opt/venv /opt/venv
ENV PATH=/opt/venv/bin:$PATH

WORKDIR /usr/src/app
COPY . .

EXPOSE 8080

CMD ["python3", "-m", "swagger_server"]
