FROM    faucet/python3
# supports arm
# alpine based

RUN     python3 -m pip install flask

COPY    flask_webserver.py /home/flask/
COPY    flaskignore.py /home/flask/

WORKDIR /home/flask

CMD     python3 flask_webserver.py
