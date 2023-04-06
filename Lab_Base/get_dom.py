# LOCAL
from File_man import File_Man

# SYS_BASE
from torrequest import TorRequest

import subprocess
from threading import Thread
import time
import socket
import struct
import textwrap
import requests
import os

# UIX
from alive_progress import alive_bar
from alive_progress.styles import showtime
from about_time import about_time
import tqdm
from tqdm import tqdm
from tqdm.notebook import tqdm as nt



# ! USES:
# ! ~ AMASS
# ! ~ HTTP PROBE -> Prove the sub domain
# ! ~ GoBust each SubDomain
class The_Doms_():
    def __init__(self, **kw):
        super(The_Doms_, self).__init__(**kw)
        self.FM             = File_Man()

    # ? OBSOLETE, BUT EDUCATIONAL
    def mass_thread_(self, to_run):
        try:
            print("[STARTED THREAD FOR AMASS]")
            ret_mass = subprocess.getoutput(to_run)
            print(f"[RET_MASS]:~~[!]:[{str(ret_mass)}]")
            for i, sub_ in enumerate(ret_mass):
                print(f"[{str(i)}]:[{str(sub_)}]")
                r_ = requests.get(str(sub_))
                print(f"\n~~[REQUEST_RET]:\n ~~~[>> {str(r_)} <<]")
        except Exception as e:
            print(f"[E]:[THE_DOMS]:[AMASS_THREAD]:[{str(e)}]")

    # @ CHANGE IP FOR EACH PROBE .. for future things
    def set_tor_(self,  uri_):
        try:
            with TorRequest() as tr:
                print("[CHANGING]:[IP]")
                tr.reset_identity()
                response =tr.get('http://ifconfig.me')
                if len(str(response)) < 20:
                    print(response.text)
                    probe_ = tr.get(f"{uri_}")
                    if probe_:
                        return probe_
                else:
                    print("[E]:[FETCHING]:[NEW_IP]")
            return
        except Exception as e:
            print(f"[E]:[{str(e)}]")
            return "ERROR"

    # TODO 
        # @ GoBuster [IP] 

    # ? GoBuster -> IP_
    def buster_IP(self, IP_, port_, prof_dir):
        print("[IP_DIR_BUSTER]")
        try:
            l_dir = prof_dir+f"/busts_IP/"
            self.FM.make_dir(l_dir)
            n_dir = prof_dir+f"/busts_IP/sub_busts/"
            self.FM.make_dir(n_dir)
            local_ = prof_dir+f"/busts_IP/sub_busts/subs.csv"
            self.FM.write_file(local_, "", "", "w+")
            to_run = f"gobuster dir -u https://{IP_}:{port_} -w /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt -o {local_}"
            print(f"[TO_BUST]:[{IP_}]\n[RUNNING]:[{to_run}]")
            ret_bust = subprocess.getoutput(to_run)
            if "Error" not in str(ret_bust):
                print(f"[{str(IP_)}]:[BUST_COMPLETED]")
            else:
                print(f"[BUST_ERROR]:[{str(ret_bust)}]")
        except Exception as e:
            print(f"[E]:[THE_DOMS]:[BUSTER_]:[{str(e)}]")


    # ? TEST IF SUB_DOMAIN IS ACTIVE
    def clear_subs_(self, sub_list):
        try:
            ret_list = []
            with alive_bar as bar:
                for j, sub_ in enumerate(sub_list):
                    to_req = "https://"+str(sub_)
                    print(f"\n~[{j}]:[{to_req}]")
                    # ? DO A GET REQUEST TO TEST ACTIVITY
                    try:
                        r = requests.get(to_req, timeout=5)
                        if r:
                            if "404" not in str(r):
                                print(f"[+]:[{sub_}]")
                                ret_list.append(str(sub_))
                            else:
                                print("[NOT_ACTIVE]")
                    except Exception as e:
                        print(f"[-]:[REQUEST_FAILED]:[FOR]:[{str(sub_)}]")
                    bar()
            return ret_list
        except Exception as e:
            print(f"[E]:[THE_DOMS]:[CLEAR_SUBS]:[{str(e)}]")

    # ? CHECK ACTIVE SUBS - URL_
    def check_sub_act(self, sub_list):
        try:
            ret_list = []
            for j, sub_ in enumerate(sub_list):
                print(f"~[{j}]:[{str(sub_)}]")
                time.sleep(0.01)
            print(f"[TOTAL_SUBS]:[{str(len(sub_list))}]")
            time.sleep(0.8)
            print("[SO NOW WE HAVE THIS LIST..]")
            time.sleep(0.8)
            print("[BUT WHAT CAN WE DO WITH IT..?]")
            time.sleep(0.8)
            print("[WELL FOR STARTERS, LET'S CHECK IF THEY ARE EVEN ACTIVE]")
            time.sleep(0.8)
            print("[TO DO SO, THERE ARE MANY TOOLS]")
            time.sleep(0.8)
            print("[BUT, THE EASIEST FOR MY LAZINESS]")
            time.sleep(0.8)
            print("[IS A SIMPLE 'GET' REQUEST]")
            time.sleep(0.8)
            print("[(since you know by now that I love the 'docs')]")
            print("[> https://requests.readthedocs.io/en/latest/user/quickstart/ <]")
            time.sleep(1.5)
            print("[THIS IS WHERE WE WILL ADD 'http://'...]")
            print("[(so if you added that before, it might cause problems here.. just type'n)]")
            time.sleep(1.5)
            re_ = input("[CONTINUE..?]")

            ret_list = self.clear_subs_(sub_list)

            time.sleep(0.5)
            print(f"\n[TOTAL ACTIVE SUBS FOUND]:[{str(len(ret_list))}]\n")
            if len(ret_list) > 1:
                print(f"[LOOKS LIKE WE HAVE FILTERED OUT ALL ACTIVE SUB_DOMAINS]")
            else:
                print("[LOOKS LIKE THERE AREN'T ANY ACTIVE SUB_DOMAINS..]")
            return ret_list
        except Exception as e:
            print(f"[E]:[THE_DOMS]:[DA_MASS]:[{str(e)}]")
            return "ERROR"


    #  ? ? ? 
    def get_sub(self, to_run_):
        return subprocess.getoutput(to_run_)


    # ? Amass or SubFinder - URL_
    def da_mass(self, prof_dir, tar_, typ_):
        try:
            da_subs = ""
            subs_list = []
            clean_subs = []
            print(f'[DA_MASS]::\n    [!]:[TARGET_]:[{tar_}]\n    [!]:[TYPE_]:[{typ_}]\n')
            probes_ = []
            to_run = f"amass enum -d {tar_} -silent"
            print(f'[WE CAN NOW RUN]:\n{to_run}')
            time.sleep(0.5)
            print("[THIS WILL TAKE SOME TIME..]")
            time.sleep(0.5)
            print("[SINCE THAT IS AN ANCIENT RELIC..]")
            time.sleep(0.5)
            mass_ = input("[DO YOU WANT TO RUN IT ANYWAY?]\n[y/N]: ")
            if "Y" in mass_.upper():
                print("[OK.. ]")
                print("[BUT WE'LL NEED TO USE MULTI_THREADING... CAUSE DAMN..]")
                Thread(target=self.mass_thread_, args=(to_run,)).start()
            else:
                print("..\n[GOOD]")
            time.sleep(0.3)
            print("[SO LET'S USE SOMETHING BETTER]")
            time.sleep(0.5)
            print("[SUBFINDER]")
            time.sleep(1)
            print("[(once again, reading the docs is always best practice)]")
            print("[(but since this is on github.. goodluck)]")
            print(">> subfinder -d <url> -silent")
            to_run_ = f"subfinder -d {tar_} -o {prof_dir}/subs_.txt -silent"
            print(f"[RUNNING]:[>{to_run_}<]")
            print("[THIS MIGHT TAKE A MINUTE OR 2...]")
            t_1 = time.time()
            try:
                with alive_bar(1000) as bar:
                    da_subs = self.get_sub(to_run_)  # subprocess.getoutput(to_run_)
                    bar()
            except Exception as e:
                print(f"[E]:[SUBFINDER]:[SUB_PROCESS]:[>{str(e)}<]")
                time.sleep(5)
            t_2 = time.time()
            tot_ = t_2 - t_1
            tot_i = int(tot_)
            print(f"[THAT TOOK]:[{str(tot_i)} seconds]")
            time.sleep(1.5)
            if da_subs:
                print("[LET'S SEE WHAT WE FOUND]:")
                subs_list = da_subs.split("\n")
                clean_subs = self.check_sub_act(subs_list)
                print(f"[NOW LET'S SAVE THEM TO THE PROFILE]")
                fi_name = prof_dir+"/subs_.txt"
                #self.FM.write_file(fi_name, clean_subs, "\n", "w+")
                print("[GREAT]\n[NOW WE CAN RUN 'GOBUSTER' ON EACH ONE :D ]\n[(cause i'm crazy like that)]")
                print("[To make things easier, we will run this process in a seperate terminal]")
                print("[Then we can continue to work on other things while we wait for that process..]")
                print("[(The terminal will NOT close by itself... but the code will terminate once completed)]")
                print("[(ToDo: add loading bar using alive-progress)]\n\n\n")
                print("[!][!][!][!][!][!][!][!][!][!][!][!][!]")
                print("[!]:[THE FOLLOW MIGHT REQUIRE SUDO]:[!]")
                print("[!][!][!][!][!][!][!][!][!][!][!][!][!]\n")

                cont_ = input("[CONTINUE..?]")
                try:
                    to_term = f"gnome-terminal -- bash -c 'python3 da_bust.py {prof_dir}; exec bash'"
                    print("[(to open a seperate terminal and run a cmd we use: )]")
                    print(to_term)
                    os.system(to_term)
                except Exception as e:
                    print(f"[E]:[THE_DOMS]:[DA_MASS]:[{str(e)}]")


                opt_ = int(input("[1]:[CONTINUE_BACK]\n[2]:[FIRST_CHECK_SUBS_FILE]\n[OPT_]: "))
                if opt_ == 1:
                    print("[CLOSING]")
                    time.sleep(1)
                    return "DONE"
                if opt_ == 2:
                    print(self.FM.read_file(prof_dir+"subs_.txt", "\n"))
                    cont_ = input("[CONTINUE..?]")

            else:
                print("** [LAB_FIRE]:[NO SUBS FOUND] **")
                print("[(the next step might cause problems.. i think, :~| )]")
                return "LAB_FIRE"

        except Exception as e:
            print("[LAB_FIRE]")
            print(f"[E]:[THE_DOMS]:[DA_MASS]:[{str(e)}]")
            return "ERROR"


    # ! # # # # # # # ! #
    # !  SUBS & DIRS  ! #
    # ! # # # # # # # ! #
    def start_here(self, prof_dir, target_, typ_):
        try:
            os.system('cls||clear')
            print("\n")
            print("@ ! @/@/@/@/@/@/@ ! @ ")
            print("@ !  SUBS & DIRS  ! @ ")
            print("@ ! @/@/@/@/@/@/@ ! @ ")
            print("\n")

            if "URL" in typ_:
                t_1 = time.time()
                print("[LAB TOOL @ HAND]:[GET_DOMS]")
                ret_ = sub_list = self.da_mass(prof_dir, target_, typ_)
                if "DONE" in ret_:
                    print("[Back to ReconRoom]")
                t_2 = time.time()
                tot_ = t_2 - t_1
                tot_i = int(tot_)
                print(f"[THAT TOOK]:[{str(tot_i)} seconds]")
            else:
                t_1 = time.time()
                print("[LAB TOOL @ HAND]:[GET_DOMS]")
                sub_list = self.da_mass(prof_dir, target_, typ_)
                t_2 = time.time()
                tot_ = t_2 - t_1
                tot_i = int(tot_)
                print(f"[THAT TOOK]:[{str(tot_i)} seconds]")
            return "DONE"
        except Exception as e:
            print(f"[E]:[THE_DOMS]:[START_FUNC]:[{str(e)}]")
            return "ERROR"




