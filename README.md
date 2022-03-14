# Distributed-Systems-Course-project
Distributed Systems Course project

This is Rock-Paper-Scissors server.
https://docs.python.org/3/library/ssl.html#ssl.SSLContext.load_cert_chain
https://www.freecodecamp.org/news/python-property-decorator/ # @property lesson
https://pythonbasics.org/webserver/




 docker build -t python_client .
 
 change DOCKERFILE
 
  docker build -t python_server .
 
server
 
 docker run -it -p 8001:8001 python_server   
 
client
 
 docker run -it --network="host" python_client
 