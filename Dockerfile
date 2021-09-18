FROM tensorflow/tensorflow:latest-gpu

RUN mkdir /home/code
WORKDIR /home/code

COPY main.py .

CMD python3 main.py