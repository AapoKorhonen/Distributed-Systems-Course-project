# Distributed-Systems-Course-project
Distributed Systems Course project

This is Rock-Paper-Scissors server.
https://docs.python.org/3/library/ssl.html#ssl.SSLContext.load_cert_chain
https://www.freecodecamp.org/news/python-property-decorator/ # @property lesson
https://pythonbasics.org/webserver/


Perjantai 11.3 muokatut tiedostot:

client.py
communication_handler.py
rpc_server.py
user.py

Uudet tiedostot

log.py
login.py
play.py
register.py
stats.py



 docker build -t python_client .
 
 VAIHDA DOCKERFILE
 
  docker build -t python_server .
 
 SERVERI PYÖRIMÄÄN CONTAINERIIN
 
 docker run -it -p 8001:8001 python_server   
 
 CLIENT PYÖRIMÄÄN
 
 docker run -it --network="host" python_client
 