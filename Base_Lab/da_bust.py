# TO BE CORRECTED

# ─$ gnome-terminal -- bash -c "python3 da_bust.py profiles_/test_2/subs_.txt profiles_/test_2  file_; exec bash"


import sys
import os
import subprocess
import time

# ? GoBuster -> URI_
def buster_uri(uri_, prof_dir):
    print("[URL_DIR_BUSTER]")
    try:
        try:
            loc_b = prof_dir+f"/busts_{uri_}/"
            os.mkdir(loc_b)
        except Exception as e:
            print(f"[DIR READY]:[{loc_b}]:[{str(e)}]")
            pass


        try:
            local_ = prof_dir+f"/busts_{uri_}/sub_bust.txt"
            os.mknod(local_)
        except Exception as e:
            print(f"[DIR READY]:[{local_}]:[{str(e)}]")
            pass

        if "https" not in uri_:
            to_run = f"gobuster dir -u https://{uri_} -w /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt > {local_}"
        else:
            to_run = f"gobuster dir -u {uri_} -w /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt > {local_}"
        print(f"[TO_BUST]:[{uri_}]\n[RUNNING]:[{to_run}]")
        ret_bust = subprocess.getoutput(to_run)
        print(f"\n~~[RET]:[{ret_bust}]")
        if "Error" not in str(ret_bust):
            print(f"[{str(uri_)}]:[BUST_COMPLETED]")
        else:
            print(f"[BUST_ERROR]:[{str(ret_bust)}]")
    except Exception as e:
        print(f"[E]:[THE_DOMS]:[BUSTER_]:[{str(e)}]")

# ? BUST EACH SUB - URL_
def da_subs_buster(sub_list, prof_dir):
    try:
        if len(sub_list) > 1:
            for i, ps_ in enumerate(sub_list):
                # ? REMOVE UNWANTED CHARACTERS FROM STRING
                p_ = ps_.translate( { ord(i): None for i in "['']\n"} )
                print(f"[BUSTING]:[{str(i)}]:[{str(p_)}]")
                buster_uri(str(p_), prof_dir)
            # ? SAVE THE PROBED SUB DOMAINS
    except Exception as e:
        print(f"[E]:[THE_DOMS]:[DA_SUBS]:[{str(e)}]")





# ? RETRIEVE LIST
def read_file(file_name, delim):
    if file_name:
        try:
            with open(file_name, "r") as rf:
                data = rf.readlines()
                rf.close()
                print("[FILE_READ]")
                time.sleep(2)
                print(f"{data}")
                time.sleep(4)
                return str(data).split(delim)
        except Exception as e:
            print("ERROR_READING_FILE", str(e))
            return "E"


print("\n")
print("@ ! ^^^^^^^^^^ ! @")
print("@ ! SUB_BUSTER ! @")
print("@ ! vvvvvvvvvv ! @")
print("\n")
print("[(this terminal will NOT exit on it's own..)]")


time.sleep(1.5)
time.sleep(1.5)
dir_ = str(sys.argv[1])
print(f"[PROF_DIR]:[{dir_}]")

# MUST BE STR -> seperated by ','
sub_file = dir_+"/subs_.txt"
sub_list = read_file(sub_file, ",")

print("[SUB_LIST]:")
for i, val_ in enumerate(sub_list):
    print(f"~[{str(i)}]:[{str(val_)}]")


time.sleep(1.5)
print(f"[LEN_lIST]:[{str(len(sub_list))}]")

da_subs_buster(sub_list, dir_)



