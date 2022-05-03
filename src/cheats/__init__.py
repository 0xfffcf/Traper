from client import Client

import pymem

"""The client can be accessed by every cheats like this."""
try:
    client = Client()
except pymem.exception.ProcessNotFound:
    print("Please start csgo.exe")
    exit(1) # Leave we do not want exception to appear.