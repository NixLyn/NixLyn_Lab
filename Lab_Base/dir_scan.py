import subprocess
from File_man import File_Man


class DirScan_():
	def __init__(self, **kw):
		super(DirScan_, self).__init__(**kw)
		self.FM = File_Man()


	# ! DIRB IS UNTESTED
	def dirb(urls,wordlist):
		try:
			arr=[]
			url=urls
			try:
				if url[:7] != 'http://':
					url="http://"+url
				r=requests.get(url)
				if r.status_code == 200:
					print('Host is up.')
				else:
					print('Host is down.')
					return
				if os.path.exists(os.getcwd()+wordlist):
					fs=open(os.getcwd()+wordlist,"r")
					for i in fs:
						print(url+"/"+i)
						rq=requests.get(url+"/"+i)
						if rq.status_code == 200:
							print(">OK".rjust(len(url+"/"+i)+5,'-'))
							arr.append(str(url+"/"+i))
						else:
							print(">404".rjust(len(url+"/"+i)+5,'-'))
					fs.close()
					print("output".center(100,'-'))
					l=1
					for i in arr:
						print(l, "> ", i)
						l+=1
				else:
					print(wordlist+" don't exists in the directory.")
			except Exception as e:
				print(e)
		except Exception as e:
				print(f"[E]:[DIRB]:[DIR_SCAN]:[>{str(e)}<]")



	# DIR_SEARCH Seems to work fine-ish
	def dir_seach(self, url_, profile_):
		print(f"[URL_]:[{str(url_)}]\n")
		try:
			to_run = f"dirsearch --output='profile_/{str(target_)}/dir_report/report.csv' --crawl -u {url_} > profile_/{str(target_)}/"
			dir_ret_ = subprocess.getoutput(to_run)

			if "Task Completed" in str(dir_ret_):
				# ! SAVE TO PROFILE...
				# FM.write...
				self.FM.write_file(profile_+"dir_search.csv", dir_ret_, "", "a+")


		except Exception as e:
				print(f"[E]:[DIRB]:[DIR_SCAN]:[>{str(e)}<]")


