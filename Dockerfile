FROM tensorflow/tensorflow:latest-gpu

RUN mkdir /home/code
WORKDIR /home/code

COPY . .

RUN pip3 install -r requirements.txt

CMD python3 main.py