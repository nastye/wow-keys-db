FROM python:3

WORKDIR /opt/keys

RUN pip install discord
RUN pip install bottle
RUN pip install git+https://github.com/SirAnthony/slpp

RUN apt install -y libsqlite3-dev
RUN pip install peewee

RUN mkdir -p /var/opt/keys && chown 1000 /var/opt/keys

USER 1000
EXPOSE 8080

COPY . .

ENTRYPOINT [ "python", "main.py" ]