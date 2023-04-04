
import subprocess
from File_man import File_Man




class MicroScans():
    def __init__(self, **kw):
        super(MicroScans, self).__init__(**kw)
        self.FM         = File_Man()


    # ? ALL KINDS
    # ! IP_ -> inetnum
    # !     -> netname
    # !     -> parent: ip_range
    # !     -> IP_ Route
    # !     -> server_location_address
    # !     -> Phone/Fax
    def who_is(self, tar_):
        try:
            print("[RUNNING]:[WHO_IS]")
            to_run = f"whois {str(tar_)}"
            return  subprocess.getoutput(to_run)
        except Exception as e:
            print(f"[E]:[ALL_MICRO_SCANS]:[WHO_IS]:[>{str(e)}<]")

    # ? it's CeWl.. 
    # ! URL -> URL/*enum
    # !     -> EMAILS
    # !     -> meta_data
    def dis_cewl(self, tar_):
        try:
            print("[RUNNING]:[CEWL_IO]")
            to_run = f"cewl -ovace {str(tar_)}"
            return  subprocess.getoutput(to_run)
        except Exception as e:
            print(f"[E]:[ALL_MICRO_SCANS]:[CEWL]:[>{str(e)}<]")

    # ? nslookup
    # ! URL -> IP
    def dis_lookup(self, tar_):
        try:
            print("[RUNNING]:[DIS_LOOKUP]")
            to_run = f"nslookup {str(tar_)} | grep Address | tail -1"
            return  str(subprocess.getoutput(to_run)).replace("Address: ", "")
        except Exception as e:
            print(f"[E]:[ALL_MICRO_SCANS]:[>{str(e)}<]")

    # ? it's CuRlY.. 
    # ! URL -> HTML_Sheet
    def curly_(self, tar_):
        try:
            print("[RUNNING]:[CURL_y]")
            to_run = f"curl -v {str(tar_)}"
            return  subprocess.getoutput(to_run)
        except Exception as e:
            print(f"[E]:[ALL_MICRO_SCANS]:[>{str(e)}<]")


    def all_scans(self, tar_typ, tar_val, dir_name):
        try:
            scans_list = []
            HOST_TYPE = tar_typ
            HOST_VAl  = tar_val


            if "URL" in HOST_TYPE:
                # SCAN URLS
                # ? KEWL
                cewl_ = self.dis_cewl(HOST_VAl)
                self.FM.save_scan(dir_name, "CEWL.csv", cewl_)
                # ? Curly ?
                braces_ = self.curly_(HOST_VAl)
                self.FM.save_scan(dir_name, "CURL.csv", braces_)
                # THEN FECTH IPs
                try:
                    # ? ns_look_up
                    ret_dns = self.dis_lookup(HOST_VAl)
                    self.FM.save_scan(dir_name, "NS_LOOK_UP.csv", ret_dns)
                    # ? Wh0_You_IP
                    IP_ = str(ret_dns.split("\n")[:-1])
                    print("[IP][?]:",IP_)
                    you_ = self.who_is(HOST_VAl)
                    self.FM.save_scan(dir_name, "WHO_IS_URL.csv", you_)
                except Exception as e:
                    print(f"[E]:[GetIp]-[WhoIs]:[>{str(e)}<]")



            if "IP" in HOST_TYPE:
                # SCAN IP 
                you_ = self.who_is(HOST_VAl)
                self.FM.save_scan(dir_name, "WHO_IS_URL.csv", you_)


        except Exception as e:
            print(f"[E]:[ALL_MICRO_SCANS]:[>{str(e)}<]")