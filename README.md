# UDP File Transfer Scripts
This project is a set of scripts that allow you to transfer files from a client to a server.
## Server
Use `python udpserver.py` to run the server first. The server will now run until closed by the user.
## Client
Use `python udpclient.py` to run the client. The client will ask for the IP of the host running the UDP Server script. It will then ask for the name of the file the user wishes to transfer. 

Note: This file must be in the same directory as the udpclient.py file.