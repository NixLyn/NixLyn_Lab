# TO BE CORRECTED

# ─$ gnome-terminal -- bash -c "python3 da_bust.py  profiles_/example_  file_; exec bash"


# BASE
import sys
import os
import os.path
import subprocess
import time
import requests

# UIX
import tqdm
from tqdm import tqdm
from alive_progress import alive_bar




# ? WRITE TO FILE
def write_file(self, file_name, data, delim, rwm):
    print(f"[FILE_NAME]:[IN_Q]:[{str(file_name)}]")
    if "[" in file_name or "]" in file_name:
        print("[BAD_FILE_NAME]")
        return
    text = ""
    if file_name:
        # ? CHECK DATA TYPE
        if type(data) == str:
            text = data
        elif type(data) == list:
            for _ in data:
                text += str(_) + str(delim)
        elif type(data) == str and len(data) == 0:
            text = ""
        # ? WRITE TO FILE -> str (delim seperated)
        with open(file_name, rwm) as wf:
            wf.write(text)
            wf.close()


# ? RETRIEVE LIST FROM FILE
def read_file(file_name, delim):
    if file_name:
        print("[FILE_NAME]",str(file_name))
        try:
            with open(file_name, "r") as rf:
                data = rf.readlines()
                rf.close()
                print("[FILE_READ]")
                time.sleep(1)
            return data
        except Exception as e:
            print("ERROR_READING_FILE", str(e))
            return "E"


# ? CURL EACH URL:
# TODO:
    # ! SCRAPE *.HTML:
        # ! *.CSS(s)
        # ! *.JS(S)
    # ! CURL *.JS *.CSS

def enum_html(da_curl):
    try:
        css_list = []
        js__list = []
        print(f"[!]:[ToDo]: \n ~ ~ ~[COLLECTION *.css, *.js paths]")
        #css_list = get_css(da_curl)
        #js__list = get_js(da_curl)
        #return css_list, js__list

    except Exception as e:
        print(f"[E]:[DA_BUST]:[CURL]:[{str(e)}]")

# ? 
def to_curl(url_, prof_dir, i_):
    try:
        file_ = f"{prof_dir}/curls_/{url_}_{i_}.txt"
        path_ = f"{prof_dir}/curls_/"

        # ? CHECK DIR
        if os.path.ispath(path_) == False:
            os.system(f'mkdir {path_}')
        # ? CHECK FILE
        if os.path.isfile(path_) == False:
            os.system(f'touch {file_}')
        # ? INIT CURL
        to_curl_ = f"curl -v {url_}"
        print(f"[CURL_ing]:[{url_}]\n")
        da_curl = subprocess.getoutput(to_curl_)
        write_file(file_, da_curl, "", "w+")
    except Exception as e:
        print(f"[E]:[DA_BUST]:[CURL]:[{str(e)}]")



# ? CLEAN 
def clean_bust(prof_dir, local_):
    try:
        cl_list = []
        bust_ = read_file(local_, "\n")
        print(f"\n***************\n[CLEANING]:[BUST_]")
        for i, val_ in enumerate(bust_):
            print(f"[{str(i)}]:[{str(val_)}]")
            # to_c = str(str(val_).split("  ")[2]).translate( { ord(i): None for i in " ['']\n~"} )
            to_c = str(val_).translate( { ord(i): None for i in " ['']\n~"} )
            to_curl(str(to_c), prof_dir, str(i))
    except Exception as e:
        print(f"[E]:[DA_BUST]:[CLEAN]:[{str(e)}]")


# ? TEST FOR 404 ERRORs
def test_live(url_):
    to_req = "nslookup "+str(url_)
    print(f"\n~[TESTING]:[{to_req}]")
    # ? DO A GET REQUEST TO TEST ACTIVITY
    try:
        r = subprocess.getoutput(to_req)
        print(str(r))
        if "NXDOMAIN" not in str(r):
            print(f"[+]:[{url_}]")
            return True
        else:
            print(f"[-]:[{url_}]")
            return False
    except Exception as e:
        print(f"[-]:[REQUEST_FAILED]:[FOR]:[{str(url_)}]")
        return False


# ? GoBuster -> URI_
def buster_uri(uri_, prof_dir):
    try:
        # ? TEST URL IF LIVE
        is_live = test_live(uri_)
        if is_live == False:
            return 
        else:
            print("[URL_LIVE]")
    except Exception as e:
        print(f"[FIRE_LIVE_TEST]:[{str(e)}]")
        return

    print("[URL_DIR_BUSTER]")
    try:
        try:
            loc_a = prof_dir+f"/busts_/"
            is_dir_ = os.path.isdir(loc_a)
            if is_dir_ == False:
                os.mkdir(loc_a)
        except Exception as e:
            print(f"[DIR READY]:[{loc_a}]:[{str(e)}]")
            pass


        try:
            loc_b = prof_dir+f"/busts_/{uri_}/"
            is_dir_ = os.path.isdir(loc_b)
            if is_dir_ == False:
                os.mkdir(loc_b)
        except Exception as e:
            print(f"[DIR READY]:[{loc_b}]:[{str(e)}]")
            pass
        try:
            local_ = prof_dir+f"/busts_/{uri_}/sub_bust.txt"
            path_to_file = local_
            path = Path(path_to_file)
            if path.is_file():
                pass
            else:
                os.mknod(local_)
        except Exception as e:
            print(f"[DIR READY]:[{local_}]:[{str(e)}]")
            pass



        #if "https" not in uri_:
        #    # ! GO_BUSTER            
        #    to_run = f"gobuster dir -u {uri_} -w /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt > {local_}"
        #else:
        #    # ! GO_BUSTER            
        #    to_run = f"gobuster dir -u {uri_} -w /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt > {local_}"

        to_run = f"gobuster dir -u {uri_} -w /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt > {local_}"

        print(f"[TO_BUST]:[{uri_}]\n[RUNNING]:[{to_run}]")
        try:
            bust_ = subprocess.getoutput(to_run)
            print('\n\n',str(bust_))
            if "Error" in bust_:
                pass
            else:
                print(f"[{str(i)}]:[{str(bust_)}]")
                #write_file(local_, bust_, "", "w+")
            print("[PROCESS_COMPLETE]")
        except Exception as e:
                print("\n[DIR_FIRE]\n",str(e))


    except Exception as e:
        print(f"[E]:[DA_BUST]:[BUSTER_]:[{str(e)}]")

# ? BUST EACH SUB - URL_
def da_subs_buster(sub_list, prof_dir):
    try:
        if len(sub_list) > 1:
            with alive_bar(len(sub_list)) as pbar:
                for i, ps_ in enumerate(sub_list):
                    # ? REMOVE UNWANTED CHARACTERS FROM STRING
                    p_ = ps_.translate( { ord(i): None for i in "['']\n"} )
                    if p_:
                        print(f"[BUSTING]:[{str(i)}]:[{str(p_)}]")
                        buster_uri(str(p_), prof_dir)
                    else:
                        print("LAB_FIRE")
                    pbar()
    except Exception as e:
        print(f"[E]:[DA_BUST]:[DA_SUBS]:[{str(e)}]")




print("\n")
print("@ ! ^^^^^^^^^^ ! @")
print("@ ! SUB_BUSTER ! @")
print("@ ! vvvvvvvvvv ! @")
print("\n")
print("[(this terminal will NOT exit on it's own..)]")


try:
    time.sleep(0.5)
    dir_ = str(sys.argv[1])
    print(f"[PROF_DIR]:[{dir_}]")
    # MUST BE STR -> seperated by ','
    sub_file = dir_+"/subs_.txt"
    sub_list = read_file(sub_file, "\n")
    print("[SUB_LIST]:")
    for i, val_ in enumerate(sub_list):
        print(f"~[{str(i)}]:[{str(val_)}]")
    print(f"[LEN_lIST]:[{str(len(sub_list))}]")
    
    
    da_subs_buster(sub_list, dir_)
    print("[COMPLETE]")
except Exception as e:
    print(f"[LAB_FIRE]:[{str(e)}]")










