FROM mysql

RUN apt update
RUN apt install -y --no-install-recommends python3-pip python3-setuptools libmysqlclient-dev build-essential python3-dev \
    libssl-dev

RUN pip3 install wheel supervisor

WORKDIR /usr/src/app

COPY requirements.txt .
RUN pip3 install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8080

CMD ["supervisord", "-n"]
