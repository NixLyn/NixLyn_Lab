# LOCAL
from File_man import File_Man
from micro_scans import MicroScans

from da_lab import Da_Lab


# SYS_BASE
import subprocess
import sys
import threading
import ipaddress
import time
import os


# UIX
from alive_progress.styles import showtime
from about_time import about_time
import tqdm





class TestCase_0():
    def __init__(self, **kw):
        super(TestCase_0, self).__init__(**kw)
        self.FM         = File_Man()
        self.MS         = MicroScans()
        self.DL         = Da_Lab()

    # ! BUILD PROFILE
    def make_profile(self, tar_type, tar_val, port_, l_host, l_port, f_name):
        try:
            prof_ = "profiles_/"


            file_dir = ""
            if "http://" in str(tar_val):
                print("[DO NOT USE 'HTTP(S)://']")
                return "HTTP", "ERROR"


            if "URL" in  tar_type.upper():
                IP_ = self.MS.dis_lookup(tar_val)
                print("[URL-IP]:", str(IP_))
            else:
                IP_ = tar_val

            IP_val = self.MS.dis_lookup(tar_val)
            to_save_ = f"[TAR_TYPE]:[>{str(tar_type)}<]\n[TAR_VAL]:[>{str(tar_val)}<]\n[IP_VAL]:[{str(IP_val)}]\n[Re_PORT]:[>{str(port_)}<]\n[L_HOST]:[>{str(l_host)}<]\n[L_PORT]:[>{str(l_port)}<]"


            if f_name:
                file_dir = f_name
            else:
                file_dir = IP_.replace(".", "_")
            print(f"[MAIN_FILE_DIR]:[>{str(file_dir)}<]")

            make_dir = prof_+file_dir
            print(f"[TEST_DIR]:[{str(make_dir)}]")
            make_dir = str(self.FM.check_prof_(make_dir, 0))
            print(f"[AVAILABLE_DIR]:[{str(make_dir)}]")

            save_at = make_dir+"/profile.csv"
            self.FM.make_dir(make_dir)
            print(f"\n@@\n[DIR_TO_MAKE]:[{make_dir}]")
            self.FM.write_file(save_at, to_save_, "\n", "a+")
            print("[IP_OF_PROFILE]:",str(IP_))
            return make_dir, IP_
        except Exception as e:
            print(f"[E]:[MAKING_PROFILE]:[>{str(e)}<]")
            return str(e)

    # ! MAIN # ! OLD
    def start_target_creation(self, f_name):
        try:
            set_tar_type = "_"
            print("\n----------------------------\n[Let's Get Some Basic Details on Your Target]\n----------------------------\n")
            while True:
                #f_name  = input("[FOLDER_NAME]: ")
                print(">> First, We need to know if your target is a URL or an IPv4.. \n (This will help with the order of operations)\n[.     ]")
                type_   = input("[TARGET_TYPE]\n[IP/URL]: ")
                if "URL" in type_:
                    print("[<< GREAT >>]\n(Since it is a >URL<; we can run a few different types of scans such as [Amass, GoBuster, etc], which we can't do with just an IPv4)\n[..    ]")
                    print("[(please do not use 'https://' or 'www.', as we will aply those where needed.. )]")
                if "IP" in type_:
                    print("[<< GOOD >>]\n(You have already determined the exact IP address of your target, so we can start scanning info using tools such as [nmap, whois, etc])\n[..    ]")


                if not type_:
                    type_ = "IP"

                target_ = input("[TAR_VAL]: ")
                if not target_:
                    print("[MUST_HAVE_TARGET]\n[TRY_AGAIN]\n")
                    time.sleep(1)
                    print("[...]")
                    time.sleep(1)
                    print("[.. ]")
                    time.sleep(1)
                    print("[.  ]")
                    time.sleep(1)
                    return self.main()
                print("[YOU CAN REMOVE PORTS FOR BEING INVOLVED]")
                port_  = input("[Re_PORT]: ")
                print("[BUT WE PROBABLY WON'T, LoL]\n")
                print("[NOW WE NEED TO PRE_SET SOME THINGS FOR MetaSploit]\n[(If you skip these they will have defaults...)]\n[...   ]")
                l_host = input("[L_HOST]: ")
                if not l_host:
                    l_host = "127.0.0.1"
                l_port = input("[....  ]\n[L_PORT]: ")
                if not l_port:
                    l_port = "23"
                print("\n[....  ]")
                print("\n[SETTING_TAGRET]\n")
                print("\n[..... ]")
                prof_dir, IP_ = self.make_profile(type_, target_, port_, l_host, l_port, f_name)
                print("[TAR_DIR]:",str(prof_dir))
                time.sleep(1.5)
                print("[A QUICK 'nslookup <url>' TO GET AN IP ADDR :) ]")
                time.sleep(1.5)
                print("[TAR_IP]: ",str(IP_))
                time.sleep(1.5)
                print("\n[......]")
                time.sleep(1.5)
                print("\n************\n[COMPILED_PROFILE]\n")
                time.sleep(0.5)
                print(f"[TAR_TYPE]:[>{str(type_)}<]")
                time.sleep(0.5)
                print(f"[TAR_VAL]:[>{str(target_)}<]")
                time.sleep(0.5)
                print(f"[IP_VAL]:[>{str(IP_)}<]")
                time.sleep(0.5)
                print(f"[Re_PORT]:[>{str(port_)}<]")
                time.sleep(0.5)
                print(f"[L_HOST]:[>{str(l_host)}<]")
                time.sleep(0.5)
                print(f"[L_PORT]:[>{str(l_port)}<]")
                time.sleep(0.5)
                print("[NOW YOU CAN EITHER GO BACK HOME OR OPEN THE TARGET PROFILE]")
                time.sleep(1.5)
                print("[OPTIONS](INT_ONLY):\n-[1]:[OPEN LAB]\n-[2]:[BACK]\n")
                opt_ = int(input("[OPT_]: "))
                time.sleep(1.5)
                print(f"[SELECTED]:[{str(opt_)}]")
                if type(opt_) != int:
                    time.sleep(1.5)
                    print("[DUDE.. INT_ONLY]")
                    time.sleep(1.4)
                    print("[...]")
                    time.sleep(1.3)
                    print("[.. ]")
                    time.sleep(1.2)
                    print("[.  ]")
                    time.sleep(1.1)
                    return
                if opt_ == 1:
                    self.open_prof(prof_dir)
                if opt_ == 2:
                    return
        except Exception as e:
            print(f"[E]:[TEST_CASE]:[MAIN]:[>{str(e)}<]")
            return False

    # ! OPEN PROFILE FOR DA_LAB
    def open_prof(self, prof_dir):
        try:
            # ? CHECK TARGET PROFILE FILE
            print("[LET'S CHECK WHAT KIND OF TARGET WE GOT HERE...]")
            prof_data = self.FM.read_file_str(prof_dir+"/profile.csv")
            typ_ = ""
            tar_val = ""
            tar_ip = ""
            re_port = ""
            for i, d_ in enumerate(prof_data):
                d_a = str(str(d_).replace("\n", ""))
                #print(f"[{str(i)}]:[{d_a}]")
                if "TYPE" in str(d_a):
                    typ_ = str(str(d_a).replace("[TAR_TYPE]:[>", "")[:-2])
                    print(f"[TYPE]:[-{typ_}-]")
                if "TAR_VAL" in str(d_a):
                    tar_val = str(str(d_a).replace("[TAR_VAL]:[>", "")[:-2])
                    print(f"[TAR_VAL]:[-{tar_val}-]")
                if "IP_VAL" in str(d_a):
                    tar_ip = str(str(d_a).replace("[IP_VAL]:[>", "")[:-2])
                    print(f"[TAR_IP]:[-{tar_ip}-]")
                if "Re_PORT" in str(d_a):
                    re_port = str(str(d_a).replace("[TAR_VAL]:[>", "")[:-2])
                    if len(re_port) > 0:
                        print(f"[Re_PORTS]:[{re_port}]")
                    else:
                        print("[NO PORTS EXCLUDE]")




            # @ @ SCAN TARGET -> ENUMERATE THE BASICS
            print("[LET'S SEE WHAT WE CAN DO WITH OUR TARGET]")
            if "URL" in typ_:
                print("[THIS TARGET IS SET AS A URL_BASE]")

                print(f"[DOMAIN]:[>{tar_val}<]")
                if tar_ip:
                    print(f"[AND AN IP OF]:[{tar_ip}]")
                print("\n[LOOKS LIKE WE CAN START 0PENING OUR LAB SPACE]:\n")


            if "IP" in typ_:
                print("[THIS TARGET IS SET AS A IP_BASE]")
                time.sleep(0.5)
                print(f"[>{tar_val}<]")
                time.sleep(0.5)
                print("[WITH THIS WE CAN DO SOME >>nmap<<, >>whois<<]")
                time.sleep(0.5)
                print("[WE CAN ALSO 'SNIFF' SOME DATA TRAFFIC :P ]\n")
                time.sleep(0.5)


            print("[ALRIGHTY]\n~[LOOKS LIKE WE'RE READY FOR SOME ACTION]")
            time.sleep(1)
            print("[.  ]")
            time.sleep(0.2)
            print("[.. ]")
            time.sleep(0.4)
            print("[...]")
            time.sleep(0.6)
            print("[OPENING_LAB]")
            time.sleep(0.8)

            # ! OFF TO THE LAB_OPTS ! #
            try:
                self.DL.open_lab(tar_val, typ_, prof_dir)
            except Exception as e:
                print(f"[OH_SHIT]:[LAB IS ON FIRE]:\n >> [{str(e)}]")


        except Exception as e:
            print(f"[E]:[CLI]:[OPEN_PROF]:[>{str(e)}<]")

    # ! DISPLAY LIST OF ALL TARGET PROFILES
    def list_profiles_(self):
        try:
            selected_prof = 0
            prof_name = ""
            print("[COLLECTING TARGET PROFILE LIST]")
            # COLLECT LIST OF PROFILES IN 'profiles_' directory
            prof_list = self.FM.file_list('profiles_')
            for i, prof_ in enumerate(prof_list, start=1):
                print(f"[{str(i)}]:[{str(prof_)}]")

            try:
                selected_prof = int(input("[SELECTED TARGET PROFILE]: "))
                if type(selected_prof) != int:
                    print("[DUDE. ]  ^ (INT_ONLY)")
                    return
                else:
                    prof_name = str(prof_list[selected_prof])
                    print(f"[SELECTED TARGET PROFILE]:[>{str(prof_name)}<]")
                    print(f"[OPTIONS]:\
                            \n~[1]:[VIEW PROFILE]\
                            \n~[2]:[OPEN LAB]\
                            \n~[3]:[CREATE NEW]\
                            \n~[4]:[CLONE PROFILE]\
                            \n~[5]:[RENAME PROFILE]\
                            \n~[6]:[BACK]\
                            ")
                    try:
                        opt_ = int(input("[OPTION]:(int_only): "))
                        if type(opt_) != int:
                            print("[DUDE.. ]  ^ (INT_ONLY)")
                            return
                        # ? BACK
                        if opt_ == 6:
                            print("[GOING_BACK]")
                            return

                        # ? RENAME
                        # TODO
                        if opt_ == 5:
                            print("[RENAME_SELECTED]:[todo]")
                            new_name = input("[NEW TARGET PROFILE NAME]: ")
                            print(f"[RENAMING]:[>{str(prof_name)}<]:[TO]:[>{str(new_name)}<]")
                            #self.FM.rename_dir(old, new)

                        # ? CLONE
                        # TODO
                        if opt_ == 4:
                            print("[CLONE_SELECTED]:[todo]")
                            clone_name = input("[CLONE TARGET PROFILE NAME]: ")
                            print(f"[CLONING]:[>{str(prof_name)}<]:[TO]:[>{str(clone_name)}<]")
                            #self.FM.clone_dir(old, new)

                        # ? CREATE
                        if opt_ == 3:
                            print("[CREATE NEW SELECTED]")
                            new_prof = input("[NEW TARGET PROFILE NAME]: ")
                            print(f"[CHECKING AVAILABILITY]")
                            is_there = self.FM.check_dir('profiles_'+str(new_prof))
                            if is_there == True:
                                print("[THAT PROFILE EXSITS]:[SCRIPT WILL START AGAIN]:[ :( ]\n~~(Cause I'm too lazy to add shit for this..)")
                                return
                            if is_there == False:
                                print("[THAT PROFILE DOES NOT EXIST YET]:[STARTING CREATING PROCESS]:[ :D ]")
                                self.start_target_creation(new_prof)

                        # ? OPEN
                        if opt_ == 2:
                            print("[OPENING PROFILE]")
                            self.open_prof("profiles_/"+prof_name)

                        # ? VIEW 
                        if opt_ == 1:
                            print("[DISPLAYING PROFILE]")
                            self.display_prof("profiles_/"+prof_name)

                    except Exception as e:
                        print(f"[E]:[LIST_PROFILE]:[SELECT OPTION]:[>{str(e)}<]")
                        return

            except Exception as e:
                print(f"[E]:[LIST_PROFILE]:[SELECT TARGET PROFILE]:[>{str(e)}<]")
                return

        except Exception as e:
            print(f"[E]:[CLI]:[LIST_PROFILES]:[>{str(e)}<]")

    # ! DISPLAY ENUMERATED DATA FILES OF TARGET PROFILE
    def display_prof(self, prof_dir):
        try:
            file_list = self.FM.file_list(prof_dir)
            for i, f_ in enumerate(file_list):
                print(f"[{str(i)}]:[{str(f_)}]")
            print('[OPTIONS](INT_ONLY):\
                        \n-[1]:[DISPLAY FILE]\
                        \n-[2]:[OPEN LAB]\
                        \n-[3]:[BACK]\
                        ')
            opt_ = int(input("[OPT_]: "))
            print(f"[SELECTED]:[{str(opt_)}]")
            if type(opt_) != int:
                print("[DUDE.. INT_ONLY]")
                return
            if opt_ == 1:
                f_name = input("[ACTUAL FILE NAME]: ")
                try:
                    f_data = self.FM.read_file_str(prof_dir+f"/{f_name}", "\n")
                    for i, d_ in enumerate(f_data):
                        print(f"[{str(i)}]:[{str(d_)}]")
                except Exception as e:
                    print(f"[E]:[COLLECTING FILE DATA]:[{str(e)}]")
            if opt_ == 2:
                self.open_prof(prof_dir)
            if opt_ == 3:
                return
        except Exception as e:
            print(f"[E]:[CLI]:[DISPLAY_PROF]:[>{str(e)}<]")
            return False

    # ! GET STARTED HERE..
    def main(self):
        os.system('cls||clear')
        print("\n")
        print('#######################################################################################')
        time.sleep(0.1)
        print('#######################################################################################')
        time.sleep(0.1)
        print('###      _______   ____ _____ ____  _____      _____ ____   ____    _______   ____  ###')
        time.sleep(0.1)
        print('###      %N_.N|    /N/   %I/   \X\   /X%       /L%    \Y\   %Y/     %N_.N|    /N%   ###')
        time.sleep(0.1)
        print('###     %N/ |N|   /N/   %I/     \X\V/X%       /L%      \Y\_%Y/     %N/ |N|   /N%    ###')
        time.sleep(0.1)
        print('###    %N/  |N|  /N/   %I/       >|X|<       /L%        \YVY/     %N/  |N|  /N%     ###')
        time.sleep(0.1)
        print('###   %N/   |N|_/N/   %I/       /X%^\X\     /L%____.     \Y/     %N/   |N|_/N%      ###')
        time.sleep(0.1)
        print('###  %N/    |N  N/   %I/       /X%   \X\   /L_L_L_L]     |Y|    %N/    |N  N%       ###')
        time.sleep(0.1)
        print('### ~~~~   ~~~~~~~~ ~~~~~    ~~~~~~ ~~~~~ ~~~~~~~~~~    ~~~~~ ~~~~~   ~~~~~~~~      ###')
        time.sleep(0.1)
        print('#######################################################################################')
        time.sleep(0.1)
        print('#######################################################################################\n\n')
        time.sleep(0.2)
        print("[WARNING]:[WEIRD GUY HUMOUR]\n")
        print("[(please keep in mind the tools used in this educational cli are really *LOUD*)]")
        print("[(is it *NOT* recommended to use this for real world purpose)]")
        print("[(even with VPN, tors, or whatever...)]\n")

        try:
            while True:
                # ? DISPLAY OPTS
                print('[OPTIONS](INT_ONLY):\
                    \n-[1]:[CREATE NEW TARGET PROFILE]\
                    \n-[2]:[LIST ALL TARGET PROFILES]\
                    \n-[3]:[OPEN TARGET PROFILE]\
                    ')
                opt_ = int(input("[OPT_]: "))
                print(f"[SELECTED]:[{str(opt_)}]")
                if type(opt_) != int:
                    print("[DUDE.. INT_ONLY]")
                    continue
                if opt_ == 1:
                    print("[CREATE TARGET PROFILE NAME]")
                    f_name  = input("[FOLDER_NAME]: ")
                    self.start_target_creation(f_name)
                if opt_ == 2:
                    print("[LISTING ALL TARGET PROFILES]")
                    self.list_profiles_()
                if opt_ == 3:
                    prof_name = input("[TARGET PROFILE NAME TO SEARCH]: ")
                    print("[SEARCHING...]")
                    is_there = self.FM.check_dir("profiles_"+prof_dir)
                    if is_there == False:
                        print("[THAT TARGET PROFILE DOES NOT EXISTS]")
                    if is_there == True:
                        print(f"[FOUND]:[{str(prof_dir)}]")
                        self.display_prof("profiles_"+prof_dir)


        except Exception as e:
            print(f"[E]:[CLI]:[MAIN]:[>{str(e)}<]")
            return



if __name__=="__main__":
    TC_0 = TestCase_0()
    TC_0.main()