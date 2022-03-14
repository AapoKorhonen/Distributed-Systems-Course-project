# Distributed-Systems-Course-project
Distributed Systems Course project

This is Rock-Paper-Scissors server.
https://docs.python.org/3/library/ssl.html#ssl.SSLContext.load_cert_chain
https://www.freecodecamp.org/news/python-property-decorator/ # @property lesson
https://pythonbasics.org/webserver/


#Instructions

There are two parts to this program, a server and a client. The server can be found in the folder RPC_Server and in the file rpc_server.py. Just run it (python rpc_serve.py)

The client is in folder RPC_Client and in the file client.py.



#Docker

 docker build -t python_client .
 
 change DOCKERFILE
 
  docker build -t python_server .
 
server
 
 docker run -it -p 8001:8001 python_server   
 
client
 
 docker run -it --network="host" python_client
 
