from alive_progress.styles import showtime
from about_time import about_time
import tqdm
from tqdm import tqdm

import time



class timing_():
    def __init__(self, **kw):
        super(timing_, self).__init__(**kw)


    def the_count(self, list_):
        for i, num in tqdm(enumerate(list_)):
            #print(f"[RUNNING]:[{str(i)}]:[{str(num)}]")
            time.sleep(2)

    def main(self):
        list_ = ["1", "2", "3", "4", "5"]

        self.the_count(list_)

if __name__=="__main__":
    t_ = timing_()
    t_.main()


