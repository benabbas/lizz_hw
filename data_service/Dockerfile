FROM python:3.7
ADD . /tmp
WORKDIR /app
COPY requirment.txt requirment.txt
RUN pip3 install -r requirment.txt

COPY consumer.py consumer.py
COPY database.py database.py

CMD [ "python3","consumer.py"]
