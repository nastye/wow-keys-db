FROM python:3.10

WORKDIR /opt/keys

ADD requirements.txt .
ADD src/* ./

RUN apt install -y libsqlite3-dev && pip install -r requirements.txt

RUN mkdir -p /var/opt/keys && chown 1000 /var/opt/keys

USER 1000
EXPOSE 8080

ENTRYPOINT [ "python", "main.py" ]
