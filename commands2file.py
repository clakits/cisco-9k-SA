


#!/usr/bin/env python
"""
N9K vsh: 9300-A# python scripts/show_vmtracker.py
cisco module is not accessible from guestshell - run it as following
guestshell:~$ dohost "python bootflash:scripts/show_vmtracker.py"
"""
import cisco

from cli import *
tmp_file = "/bootflash/testint.out"
out_file = open(tmp_file, "w")

tmps = [" show interface e2/1 ",
       "show interface e2/2"]

for tmp in tmps:
   str = cli(tmp)
   out_file.write(str)

out_file.close()
