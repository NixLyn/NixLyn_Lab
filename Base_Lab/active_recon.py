# LOCAL
from File_man import File_Man

# LAB TOOLS
from net_map import NetMap
from micro_scans import MicroScans
from get_dom import The_Doms_

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
    # @ ? AmAss & GoBuster..        []



class Active_Recon_():
    def __init__(self, **kw):
        super(Active_Recon_, self).__init__(**kw)
        self.FM         = File_Man()
        self.NM         = NetMap()
        self.MS         = MicroScans()
        self.TD         = The_Doms_()


    # ? MicroScans
    def micro_scans(self, type_, target_, port_, file_dir):
        IP_ = ""
        try:
            IP_ = ""
            if type_ == "URL":
                try:
                    self.MS.all_scans(type_, target_, file_dir)
                    print("[TYPE_URL]...\n[FETCHING_IP]...")
                    # ! NS_LOOK_UP -> IP_
                    IP_ = self.MS.dis_lookup(target_)
                    print(f"[IP_FOUND]:[>{str(IP_)}<]")
                    print(f"[STARTING_]:[MICRO_SCANS]:[&&]:[NET_MAP]")
                    tcp_ = self.NM.og_scan(type_, IP_, file_dir, " ", port_)
                    self.MS.all_scans(type_, target_, file_dir)
                except Exception as e:
                    print(f"[E]:[STD_SCANS]:[>{str(e)}<]")
            else:
                try:
                    self.MS.all_scans(type_, target_, file_dir)
                    print(f"[STARTING_]:[MICRO_SCANS]:[&&]:[NET_MAP]")
                    tcp_ = self.NM.og_scan(type_, IP_, file_dir, " ", port_)
                    self.MS.all_scans(type_, target_, file_dir)
                except Exception as e:
                    print(f"[E]:[STD_SCANS]:[>{str(e)}<]")
            print("[MICRO_SCANS_COMPLETED]")
        except Exception as e:
            print(f"[E]:[START_SCAN]:[>{str(e)}<]")
            return ["ERROR", "OG_SCAN", "START_SCAN"]


    # ? STEP_ONE_A : BASIC NMAP
    def step_one_a(self, target_, typ_, prof_dir):
        try:
            port_list = []
            da_ports_ = []
            ports_ = ""
            print("[IF YOU ARE NOT FAMILIAR WITH 'nmap']")
            time.sleep(1)
            print("[IT IS HIGHLY SUGGESTED TO READ UP IT]")
            print("[THERE ARE MULTIPLE SOURCES ON THE WEB]")
            print("[BUT IT IS ALWAYS BEST PRACTICE TO START WITH THE 'docs']")
            print("[> https://nmap.org <]")
            print("[(if you are using the git clone version of this, have a look at 'net_map.py')]")
            print("[IF YOU ARE FAMILIAR WITH 'nmap']")
            print("[THEN YOU CAN ADD SOME FLAGS]")
            print("[BY DEFAULT WE JUST USE '-A']")
            print("[(please use spaces to seperate the flags, same as you would in a terminal cmd)]")
            print("[(some eg.):")
            print(" ~ [(-v = Verbose)]")
            time.sleep(0.2)
            print(" ~ [(-Pn = quite port scan)]")
            time.sleep(0.2)
            print(" ~ [(-F (Fast (limited port) scan))]")
            time.sleep(0.2)
            print(" ~ [(-sV (Version detection))]")
            time.sleep(0.2)
            print(" ~ [(-O: Enable OS detection ) <- (requires root)]")
            time.sleep(0.2)
            print(" ~ [(-6: Enable IPv6 scanning) <- (usually found when using 'https://')]")
            flags_ = input("[FLAGS]:(optional): ")
            time.sleep(0.5)
            try:
                print("[THIS MIGHT TAKE SOME TIME, PATIENCE IS KEY..]")
                t_1 = time.time()
                ports_ = ""
                ports_ = self.NM.og_scan(typ_, target_, prof_dir, flags_, "params_")
                t_2 = time.time()
                tot_ = t_2 - t_1
                tot_i = int(tot_)
                print(f"[THAT TOOK]:[{str(tot_i)} seconds]")
                print("[IF THAT WORKED, WE SHOULD HAVE A LIST OF OPEN PORTS]")
                if ports_:
                    da_ports_ = ports_.split(",")
                    for i, p_ in enumerate(da_ports_):
                        if p_:
                            port_list.append(str(p_))
                            print(f"[{str(i)}]:[{str(p_)}]")
                else:
                    print("[CHECK THE PROFILE DIR TO SEE IF THERE'S ANY CLUE AS TO WHAT WENT WRONG]")
                
            except Exception as e:
                print(f"[E]:[Da_Lab]:[S_1]:[OG_SCAN]:[{str(e)}]")

        except Exception as e:
            print(f"[E]:[Da_Lab]:[STEP_ONE]:[{str(e)}]")

    # ? STEP_ONE_B : ENUM NMAP todo


    # ? STEP_TWO_A : SUB_FINDER  - URL
    def step_two_a(self, target_, typ_, prof_dir):
        try:
            print("[TO BREAK THE DOMAINS OPEN]")
            time.sleep(1.3)
            print("[WE WILL NEED TO FIRST FIND ALL 'SUB' DOMAINS]")
            time.sleep(1.3)
            print("[(eg. services.domain.com)]")
            time.sleep(1.3)
            print("[THEN WE CAN START BUSTING EACH DOMAIN's DIRECTORY]")
            time.sleep(1.3)
            print("[STARTING 'GET_DOM' TOOL]")
            y = input("[CONTINUE...?]")
            doms_ = self.TD.start_here(target_, typ_, prof_dir)
            if "DONE" in doms_:
                print("[THE DOMAINS WILL CONTINUE TO GET BUSTED IN THE NEW TREMINAL]")
                time.sleep(1.3)
                print("[LONG AS YOU DON'T KILL THE PROCESS OR POWER]")
                time.sleep(1.3)
                print("[IF ALL WENT WELL, THERE SHOULD BE SOME NEW STUFF IN THE PROFILE DIRECTORY :) ]")
            if "ERROR" in doms_:
                print("[LAB_FIRE]:[GET_DOMS]")

        except Exception as e:
            print(f"[E]:[Da_Lab]:[STEP_THREE]:[{str(e)}]")



    # ! # # # # # # # # # ! #
    # ! ACTIVE RECON ROOM ! #
    # ! # # # # # # # # # ! #
    def open_room(self, target_, typ_, prof_dir):
        try:
            os.system('cls||clear')
            print("\n")
            print("@ ! ^^^^^^^^^^^^^^^^^ ! @")
            print("@ ! ReconRoom(active) ! @")
            print("@ ! vvvvvvvvvvvvvvvvv ! @")
            print("\n")

            print("[LET'S BEGIN LOOKING AT OUR LAB RECON TOOLS]")
            time.sleep(1)
            print("[FIRST LET'S GET SOME INFO ON OUR TARGET]")
            time.sleep(1)
            print(f"[SINCE WE ARE WORKING WITH]:[{typ_}]")
            time.sleep(1)
            if "URL" in typ_:
                time.sleep(0.5)
                print(f"[IT MEANS WE HAVE SOME ACTIVE RECON TOOLS WE CAN USE]:")
                time.sleep(0.5)
                print(f"~[NMAP]")
                time.sleep(0.5)
                print(f"~[CURL]")
                time.sleep(0.5)
                print(f"~[CEWL]")
                time.sleep(0.5)
                print(f"~[WHOIS]")
                time.sleep(0.5)
                print(f"~[AMASS]")
                time.sleep(0.5)
                print(f"~[GOBUSTER]")
                time.sleep(0.6)
                print("~[AND MORE, WHICH WE'LL GET INTO LATER]")
                time.sleep(1)
                print("\n[AS ANY SELF RESPECTING PEN_TESTER/HACKER WILL KNOW]")
                time.sleep(1)
                print("[THE FIRST PLACE TO START IS ALWAYS >> NMAP << ]")
                time.sleep(1)

                # ! STEP_ONE_A : NMAP
                self.step_one_a(target_, typ_, prof_dir)

                # TODO 
                # ! STEP_ONE_B : GET_ENCRYPTS
                print("[NMAP PROVIDES LOTS OF INFO ON A TARGET]")
                time.sleep(1)
                print("[ONE OF THEM BEING ENCRYPTION METHODS BEING USED]")
                time.sleep(1)
                print("[BUT WE WILL GET BACK TO THAT LATER..]")


                # ! STEP_TWO : DOMAIN BREAKER
                print("\n[NOW LET'S FIND ALL SUB DOMAINS AND THEIR SUB DIRECTORIES]")

                time.sleep(0.2)
                ready_ = input("[READY FOR STEP TWO?]:[Y/n]: ")
                if "N" not in ready_.upper():
                    self.step_two_a(prof_dir, target_, typ_)


                # ! STEP_THREE : DEEPER DIGS
                print("[NOW THAT WE HAVE EXTRACTED ALL SUB_DOMAINS AND DIRECTORIES]")
                print("[(The threads might still be running though)]\n")
                print("[WE CAN START DoING SOME MORE DIGGING]")
            if "IP" in typ_:
                print("[CAN'T REALLY DO MUCH WITH ONLY THIS]")
                time.sleep(1.2)
                print("[BUT WE CAN DO NMAP TO FIND PORTS & SOME MICRO_SCANS]")
                self.micro_scans(type_, target_, port_, file_dir)


        except Exception as e:
            print(f"[E]:[Active Recon]:[Open Room]:[{str(e)}]")










