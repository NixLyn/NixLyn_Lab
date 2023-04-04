from torrequest import TorRequest
import time
import os
import requests
import html
from bs4 import BeautifulSoup, SoupStrainer
from urlextract import URLExtract

class Dork_Stack():
    def __init__(self, **kw):
        super(Dork_Stack, self).__init__(**kw)
        self.current_stack = []
        from STACK_PY.file_stack_man import File_man
        self.FM = File_man()



    # FILTER 
    #    [REMOVE_NUANCE]
    def filter_urls(self, url_list):
        try:

            ignore_list = self.FM.read_file("STACK_PY/ingore.txt", "\n")
            ret_list = []
            for url_ in url_list:
                if "google" not in str(url_) and "body jsmodel" not in str(url_):
                    #print(f"[FILTERED_ULR]:[{str(url_)}]")
                    for ig_ in ignore_list:
                        if str(ig_) not in str(url_):
                            ret_list.append(url_)
                            self.current_stack.append(url_)
            return ret_list
        except Exception as e:
            print(f"[E]:[FILETER_URLS_]:[{str(e)}]")


    # FETCH LINKS FOR: [WITH EXTENSIONS]
    def get_stack_of(self, soup):
        try:
            c_urls_ = []
            hrefs = soup.split('href="/url?q=')
            for i, h in enumerate(hrefs):
                if "http" in h:
                    c_urls_.append(str(h.split("&")[0]))
                    #print("[FOUND_]:",str(h.split("&")[0]))
            return self.filter_urls(c_urls_)
        except Exception as e:
            print(f"[E]:[GET_STACK_OF]:[>{str(e)}<]")


    # USES [GOOGLE]:[FIREFOX]:
    #   SCRAPES PAGE -> for links
    def scrape_url(self, tr, pre_url):
        stack_scraped    = ""
        filtered_ = []
        try:
            print("[TO_FIND]:", pre_url)
            r = tr.get(pre_url)
            html = r.text
            soup = BeautifulSoup(html, "html.parser")
            stack_scraped = self.get_stack_of(str(soup.body))
            return stack_scraped
        except Exception as c:
            print(f"[E]:[SEARCH_IT]:[>{str(c)}<]")


    # SOCIAL_PAGES
    # [GOOGLE_DORK]:[FACE_BOOK]
    def fb_dork_(self, tr, number_):
        try:
            to_dork = number_.replace("+27", "")
            fb_dork = f"https://www.google.com/search?q=site%3Afacebook.com+intext%3A%2227{to_dork}%22+OR+intext%3A%22%2B27{to_dork}%22+OR+intext%3A%220{to_dork}%22 "
            r = tr.get(fb_dork)
            html = r.text
            soup = BeautifulSoup(html, "html.parser")
            url_list = self.get_stack_of(str(soup.body))
            if len(url_list) == 0:
                return ["FB_DORK", "NOT_FOUND"]
            else:
                return url_list
        except Exception as c:
            print(f"[E]:[FB_DORK]:[>{str(c)}<]")

    # [GOOGLE_DORK]:[TWITTER]
    def tw_dork_(self, tr, number_):
        try:
            to_dork = number_.replace("+27", "")
            tw_dork = f"https://www.google.com/search?q=site%3Atwitter.com+intext%3A%2227{to_dork}%22+OR+intext%3A%22%2B27{to_dork}%22+OR+intext%3A%220{to_dork}%22"
            r = tr.get(tw_dork)
            html = r.text
            soup = BeautifulSoup(html, "html.parser")
            url_list = self.get_stack_of(str(soup.body))
            if len(url_list) == 0:
                return ["TW_DORK", "NOT_FOUND"]
            else:
                return url_list
        except Exception as c:
            print(f"[E]:[TW_DORK_IT]:[>{str(c)}<]")

    # [GOOGLE_DORK]:[LINKEDIN]
    def li_dork_(self, tr, number_):
        try:
            to_dork = number_.replace("+27", "")
            li_dork = f"https://www.google.com/search?q=site%3Alinkedin.com+intext%3A%2227{to_dork}%22+OR+intext%3A%22%2B27{to_dork}%22+OR+intext%3A%220{to_dork}%22"
            r = tr.get(li_dork)
            html = r.text
            soup = BeautifulSoup(html, "html.parser")
            url_list = self.get_stack_of(str(soup.body))
            if len(url_list) == 0:
                return ["LI_DORK", "NOT_FOUND"]
            else:
                return url_list
        except Exception as c:
            print(f"[E]:[LI_DORK_IT]:[>{str(c)}<]")

    # [GOOGLE_DORK]:[INSTAGRAM]
    def in_dork_(self,tr,  number_):
        try:
            to_dork = number_.replace("+27", "")
            in_dork = f"https://www.google.com/search?q=site%3Ainstagram.com+intext%3A%2227{to_dork}%22+OR+intext%3A%22%2B27{to_dork}%22+OR+intext%3A%220{to_dork}%22"
            r = tr.get(in_dork)
            html = r.text
            soup = BeautifulSoup(html, "html.parser")
            url_list = self.get_stack_of(str(soup.body))
            if len(url_list) == 0:
                return ["IN_DORK", "NOT_FOUND"]
            else:
                return url_list
        except Exception as c:
            print(f"[E]:[IN_DORK_IT]:[>{str(c)}<]")

    # [GOOGLE_DORK]:[SYNC.ME]:[G_SYNC]
    def gs_dork_(self, tr,  number_):
        try:
            to_dork = number_.replace("+27", "")
            go_dork = f"https://www.google.com/search?q=site%3Async.me+intext%3A%2227{to_dork}%22+OR+intext%3A%22%2B27{to_dork}%22+OR+intext%3A%220{to_dork}%22"
            r = tr.get(go_dork)
            html = r.text
            soup = BeautifulSoup(html, "html.parser")
            url_list = self.get_stack_of(str(soup.body))
            if len(url_list) == 0:
                return ["GS_DORK", "NOT_FOUND"]
            else:
                return url_list
        except Exception as c:
            print(f"[E]:[GS_DORK_IT]:[>{str(c)}<]")

    # BUSINESS_IER
    # [GOOGLE_DORK]:[YELLOW_PAGES]
    def yellow_(self, tr, number_):
        try:
            to_dork = number_.replace("+27", "")
            yo_dork = f"https://www.google.com/search?q=site%3Ayellowpages.ca+intext%3A%22%2B27{to_dork}%22"
            r = tr.get(yo_dork)
            html = r.text
            soup = BeautifulSoup(html, "html.parser")
            url_list = self.get_stack_of(str(soup.body))
            if len(url_list) == 0:
                return ["YO_DORK", "NOT_FOUND"]
            else:
                return url_list
        except Exception as c:
            print(f"[E]:[YELLOW]:[>{str(c)}<]")


    # USA_STYLE
    # [GOOGLE_DORK]:[numinfo.net]
    def num_info_(self, tr, number_):
        try:
            to_dork = number_.replace("+27", "")
            num_dork = f"https://www.google.com/search?q=site%3Anuminfo.net+intext%3A%2227{to_dork}%22+OR+intext%3A%22%2B27{to_dork}%22+OR+intext%3A%220{to_dork}%22"
            r = tr.get(num_dork)
            html = r.text
            soup = BeautifulSoup(html, "html.parser")
            url_list = self.get_stack_of(str(soup.body))
            if len(url_list) == 0:
                return ["NI_DORK", "NOT_FOUND"]
            else:
                return url_list
        except Exception as c:
            print(f"[E]:[NUM_FO]:[>{str(c)}<]")



    # ITERATE THROUGH STACK BEFORE CHANGING IP
    # RETURNS LIST OF URL_LIST(s)
    def get_stack_(self, number_):
        try:
            self.current_stack  = []
            fin_stack           = []
            with TorRequest() as tr:
                to_dork = number_.replace("+27", "")
                g_rl_ = f'https://www.google.co.za/search?q=+intext%3A%2227{to_dork}%22+OR+intext%3A%22%2B27{to_dork}%22+OR+intext%3A%220{to_dork}%22 '
                std_ = self.scrape_url(tr, g_rl_)
                fb__ = self.fb_dork_(tr, number_)
                tw__ = self.tw_dork_(tr, number_)
                li__ = self.li_dork_(tr, number_)
                in__ = self.in_dork_(tr, number_)
                po__ = self.num_info_(tr, number_)
                yo__ = self.yellow_(tr, number_)
                gs__ = self.gs_dork_(tr, number_)
                print("[CHANGING]:[IP]")
                tr.reset_identity()
                response =tr.get('http://ifconfig.me')
                if len(str(response)) < 20:
                    print(response.text)
                else:
                    print("[E]:[FETCHING]:[NEW_IP]")
                fin_stack = self.current_stack
                return fin_stack
        except Exception as e:
            print(f"[E]:[{str(e)}]")
            return "ERROR"




