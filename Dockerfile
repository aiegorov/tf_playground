FROM tensorflow/tensorflow:latest-gpu

COPY main.py /
WORKDIR /

CMD python3 main.py