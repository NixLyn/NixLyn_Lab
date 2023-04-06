# LOCAL
from File_man import File_Man

# LAB ROOMS
from active_recon import Active_Recon_
from brute_bench import Brute_Bench_
from passive_recon import Passive_Recon_
from exploit_bench import Exploit_Bench_

# SYS_BASE
import subprocess
import sys
import os


class Da_Lab():
    def __init__(self, **kw):
        super(Da_Lab, self).__init__(**kw)
        self.FM         = File_Man()

        # ! LAB_ROOMS
        self.AR         = Active_Recon_()
        self.PR         = Passive_Recon_()
        self.EB         = Exploit_Bench_()
        self.BB         = Brute_Bench_()



    # ? SCANS

    # ! BASE SCANS
    # ! THREAD TO FINISH BEFORE NEXT ONE CAN START


    # ? EDUCATIONAL ATTACKS






    # TODO:
        # @ ? Active Recon      - [InProgress]
        # @ ? Passive Recon     - ['listener_']
        # @ ? BruteBench        - [hydra, medusa]
        # @ ? ExploitBench      - [NxBreta]
        # @ ? FiringRange       - [VM Clone]



    # ! # # # # # # # ! #
    # !  SELECT ROOM  ! #
    # ! # # # # # # # ! #
    def lab_opts_(self, target_, typ_, prof_dir):
        try:

            while True:
                os.system('cls||clear')
                print("\n")
                print("@ ! ^^^^^^^^^^^^^^^ ! @")
                print("@ ! SELECT LAB ROOM ! @")
                print("@ ! vvvvvvvvvvvvvvv ! @")
                print("\n")
                print("[LAB ROOMS]:")
                print(" ~ [1]:[ReconRoom](active)-beta")
                print(" ~ [2]:[ReconRoom](passive)-inactive")
                print(" ~ [3]:[BruteBench](low)-inactive")
                print(" ~ [4]:[ExploitBench](NxBreta)-inactive")
                print(" ~ [5]:[FiringRange](VM_Clone)-inactive")
                print(" ~ [6]:[Back](Main)")

                opt_ = int(input("[OPTION]:(int_only): "))
                if type(opt_) != int:
                    print("[DUDE.. ]  ^ (INT_ONLY)")
                    continue
                # ? BACK
                if opt_ == 6:
                    print("[GOING_BACK]")
                    return
                # ? RENAME
                # TODO
                if opt_ == 1:
                    print("[OPENING..]:\n ~[ReconRoom](active)")
                    self.AR.open_room(target_, typ_, prof_dir)


                if opt_ == 2:
                    print("[ReconRoom](passive) - [UNDER CUNSTRUCTION] ")
                    self.PR.open_room(target_, typ_, prof_dir)

                if opt_ == 3:
                    print("[BruteBench](low) - (beta)")
                    self.BB.check_bench(target_, typ_, prof_dir)

                if opt_ == 4:
                    print("[ExploitBench](NxBreta) - [UNDER CUNSTRUCTION]")
                    #self.AD.recon_room(target_, typ_, prof_dir)


                if opt_ == 5:
                    print("[FiringRange](VM_Clone) - [UNDER CUNSTRUCTION]")
                    #self.AD.recon_room(target_, typ_, prof_dir)


        except Exception as e:
            print(f"[E]:[Da_Lab]:[LAB_OPTS_]:[{str(e)}]")




    # ! # # # # # # # # # ! #
    # !  LAB LOBBY ROOM   ! #
    # ! # # # # # # # # # ! #
    def open_lab(self, target_, typ_, prof_dir):
        try:
            os.system('cls||clear')
            print("\n")
            print("@ ! ^^^^^^^^^^^^^^^^^ ! @")
            print("@ ! OPENING LAB LOBBY ! @")
            print("@ ! vvvvvvvvvvvvvvvvv ! @")
            print("\n")
            print("[LET'S SEE YOUR CURRENT PROGRESS ON THE TARGET PROFILE]")

            # ? CHECK PROFILE CONTENT:
                # ? PROFILE_
                # ? NMAP_:
                    # ? ~ URL
                    # ? ~ IP
                    # ? ~ PORTS
                # ? SUBS_
                # ? BUSTS/
                # ? FULL_CLONE/
                # ? EMAILS/
            # @ Profile            
            try:
                prof_ = self.FM.read_file(prof_dir+"/profile.csv", "\n")
                if prof_:
                    print("[PROFILE FOUND]:")
                    for i, p_ in enumerate(prof_):
                        print(f" ~ ~[{str(i)}]:[{str(p_)}]")
            except Exception as e:
                print(f"[E]:[LOADING_PROFILE]:[{str(e)}]")

            # @ SubDomains
            try:
                subs_ = self.FM.read_file(prof_dir+"/subs_.csv", ",")
                if subs_:
                    print("[SUB DOMAINS FOUND]:")
                    for i, p_ in enumerate(subs_):
                        print(f" ~ ~[{str(i)}]:[{str(p_)}]")
            except Exception as e:
                print(f"[E]:[LOADING_SUB_DOMAINS]:[{str(e)}]")

            # @ NetMap - URL
            try:
                nmap_U = self.FM.read_file(prof_dir+"/nmap_scan_URL.csv", "\n")
                print(f"[NMAP_SCAN]:[URL]: \n{nmap_U}")
            except Exception as e:
                print(f"[E]:[LOADING_NMAP_URL_SCAN]:[{str(e)}]")

            # @ NetMap - IP
            try:
                nmap_I = self.FM.read_file(prof_dir+"/nmap_scan_IP.csv", "\n")
                print(f"[NMAP_SCAN]:[IP]: \n{nmap_I}")
            except Exception as e:
                print(f"[E]:[LOADING_NMAP_IP_SCAN]:[{str(e)}]")

            # @ PortsList
            try:
                ports_ = self.FM.read_file(prof_dir+"/nmap_ports_.csv", "\n")
                if ports_:
                    print("[PORTS LISTED]:")
                    for i, b_ in enumerate(ports_):
                        print(f" ~ ~[{str(i)}]:[{str(p_)}]")
            except Exception as e:
                print(f"[E]:[LOADING_NMAP_PORTS_SCAN]:[{str(e)}]")

            # @ SubDomain - Busts
            try:
                n_dir = prof_dir+f"/busts_{target_}/sub_busts/"
                busts_ = self.FM.check_list(n_dir)
                if busts_:
                    print("[DOMAINS BUSTED]:")
                    for i, b_ in enumerate(busts_):
                        print(f" ~ ~[{str(i)}]:[{str(p_)}]")
            except Exception as e:
                print(f"[E]:[LOADING_NMAP_PORTS_SCAN]:[{str(e)}]")


            self.lab_opts_(target_, typ_, prof_dir)


        except Exception as e:
            print(f"[E]:[Da_Lab]:[CHECK_LAB]:[{str(e)}]")



