# UIX
from alive_progress import alive_bar
from alive_progress.styles import showtime
from about_time import about_time
import tqdm
from tqdm import tqdm
from tqdm.notebook import tqdm as nt
import os
import subprocess


to_run_ = "nmap -A leapfrogstudios.com"


# eg. 1
try:
    with alive_bar(10) as bar:
        da_subs = ""
        da_subs = subprocess.getoutput(to_run_)
        bar()
except Exception as e:
    print(f"[E]:[SUBFINDER]:[SUB_PROCESS]:[>{str(e)}<]")
