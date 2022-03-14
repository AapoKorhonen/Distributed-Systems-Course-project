FROM ubuntu:latest

RUN apt update
RUN apt install python3 -y

COPY /RPC_Client ./
COPY Certificates ./

CMD [ "python3", "./client.py"]