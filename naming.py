__author__ = "kdhht5022@gmail.com"
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import argparse

app = argparse.ArgumentParser()
app.add_argument("-start", "--start_no", type=int, default=1,
                 help="Start number of .jpg files.")
app.add_argument("-end", "--end_no", type=int, default=10,
                 help="End number of .jpg files.")
app.add_argument("-sft", "--shifting_value", type=int, default=200,
                 help="Shifting value.")
args = vars(app.parse_args())

start_no = args["start_no"]
end_no = args["end_no"]
shifting_value = args["shifting_value"]

import subprocess
for i in range(start_no, end_no+1, 1):
    subprocess.Popen('mv /path/to/images/00'+str(i)+'.jpg' \
                     ' /another_path/to/images/00'+str(i+shifting_value)+'.jpg', shell=True)
    subprocess.Popen('rm -f /path/to/images/00'+str(i)+'.jpg', shell=True)
