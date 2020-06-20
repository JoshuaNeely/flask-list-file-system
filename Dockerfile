FROM    rackspacedot/python37

RUN     python3 -m pip install flask
RUN     apt install -y vim

WORKDIR /home/flask

COPY    flask_webserver.py /home/flask/
COPY    run-flask.sh /home/flask/

CMD     ./run-flask.sh
