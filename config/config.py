import socket
from sys import platform

HOSTNAME = socket.gethostname()
HOST_IP_ADDRESS = socket.gethostbyname(HOSTNAME)
PLATFORM = platform