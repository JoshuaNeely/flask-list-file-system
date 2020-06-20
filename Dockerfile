FROM    rackspacedot/python37

RUN     python3 -m pip install flask
RUN     apt install -y vim

WORKDIR /home/flask

COPY    flask_webserver.py /home/flask/
COPY    flaskignore.py /home/flask/

CMD     python3 flask_webserver.py
