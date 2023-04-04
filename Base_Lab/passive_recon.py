# LOCAL
from File_man import File_Man

# SYS_BASE
import subprocess
import sys
import threading
import ipaddress
import time
import requests
import os


# gnome-terminal <- cmd for opening new terminal


# TODO:
    # @ ? NET_MAP :                 []
        # @ ~ PORTS                 []
        # @ ~ ENCRYPTS              []
        # @ ~ SERVICES + VERSIONS   []
    # @ ? NET SNIFFER..             []
        # @ ~ PACKET CAPTURE        []
        # @ ~ PACKET DECRYPTION..   []

    # @ ? SQL INJECTOR..            []



class Passive_Recon_():
    def __init__(self, **kw):
        super(Passive_Recon_, self).__init__(**kw)
        self.FM         = File_Man()


    # ! # # # # # # # ! #
    # !  OPEN PASSIVE ! #
    # ! # # # # # # # ! #
    def open_room(self, target_, typ_, prof_dir):
        try:
            print("[PASSIVE RECON IS UNDER CUNSTUCTION]")
            time.sleep(3)
            print("[WE WILL BE IMPLEMENTING A PACKET SNIFFER IN THIS ROOM :D ]")
            time.sleep(3)
            print("[BYE FOR NOW]")
            return

        except Exception as e:
            print(f"[E]:[Passive Recon]:[Open Room]:[{str(e)}]")



