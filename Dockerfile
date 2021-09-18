FROM tensorflow/tensorflow:latest-gpu

RUN mkdir /home/code
WORKDIR /home/code

COPY . .

RUN python3 -m pip install --upgrade pip
RUN pip3 install -r requirements.txt

CMD python3 main.py
