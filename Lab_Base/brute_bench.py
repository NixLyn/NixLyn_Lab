# LOCAL
from File_man import File_Man

# SYS_BASE
import subprocess

# BENCH TOOLS


class Brute_Bench_():
    def __init__(self, **kw):
        super(Brute_Bench_, self).__init__(**kw)
        self.FM         = File_Man()


    # ! CONFIGURE ATTACK PROCESS
    def start_attcks(self, target_, typ_, prof_dir, opts_):
        try:
            pass
        except Exception as e:
            print(f"[E]:[Brute_Bench]:[Check_Bench]:[{str(e)}]")


    # ! CHECK BENCH
    def check_bench(self, target_, typ_, prof_dir):
        try:
            os.system('cls||clear')
            print("\n")
            print("@ ! ^^^^^^^^^^^^^^^^ ! @")
            print("@ ! BRUTE WORK BENCH ! @")
            print("@ ! vvvvvvvvvvvvvvvv ! @")
            print("\n")

            while True:
                print("[Brute Bench]:[OPTIONS]:")
                print(" ~ [1]:[List Tools]")
                print(" ~ [2]:[Check Prof]")
                print(" ~ [3]:[Start Brutes]")
                print(" ~ [4]:[Clean]")
                print(" ~ [5]:[Back]")


                opt_ = int(input("[OPTION]:(int_only): "))
                if type(opt_) != int:
                    print("[DUDE.. ]  ^ (INT_ONLY)")
                    continue

                # ? BACK
                if opt_ == 5:
                    print("[GOING_BACK]")
                    return

                # ? RENAME
                if opt_ == 1:
                    print("[List of Tools]")
                    print("~ [1]:[HYDRA]")
                    print("~ [2]:[MEDUSA]")
                    print("~ [3]:[WRUTE]")




                if opt_ == 2:
                    print("[Checking Profile For Past Attacks]")
                    #self.FM.get_list(prof_dir+"/brutes")

                if opt_ == 3:
                    print("[Start Brutes]:[OPTIONS]")
                    print("~ [1]:[HYDRA]")
                    print("~ [2]:[MEDUSA]")
                    print("~ [3]:[WRUTE]")
                    print("~ [4]:[ALL_!]")
                    opt_b = int(input("[OPTION]:(int_only): "))
                    if type(opt_b) != int:
                        print("[DUDE.. ]  ^ (INT_ONLY)")
                        continue
                    else:
                        print("[Brute Attacks can be a very time consuming]")
                        print("[so we will run each selected attack in a seperate terminal]\n\n\n[nothings happening cause I haven't does this part yet]")



                if opt_ == 4:
                    print("[Clean]")
                    print("[ToDo]")
                    #self.AD.recon_room(target_, typ_, prof_dir)



        except Exception as e:
            print(f"[E]:[Brute_Bench]:[Check_Bench]:[{str(e)}]")








