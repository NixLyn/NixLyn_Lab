# LOCAL
from File_man import File_Man
from micro_scans import MicroScans

# SYS_BASE
import subprocess
from threading import Thread
import time




class PortEnum():
    def __init__(self, **kw):
        super(PortEnum, self).__init__(**kw)
        self.FM         = File_Man()
        self.MS         = MicroScans()


    def get_port_info(self, port_num, ip_):
        try:
            to_scan = f"nmap -p{str(port_num)} -A {str(ip_)} | grep {str(port_num)}"
            print(f"[PORT_ENUM]:[>{str(to_scan)}<]")
            ret_scan = str(subprocess.getoutput(to_scan))
            print(f"[PORT_DATA]:[>{str(ret_scan)}<]")
            ret_ = ret_scan.split(" ")
            return ret_
        except Exception as e:
            print(f"[E]:[GET_PORT_ENUM]:[{str(e)}]")





