#!/usr/bin/env python
# -*- coding: utf8 -*-

# блокировка до тех пор, пока не будет соединения с интернетом
from other_functions import wait_internet
wait_internet()
# ==========================================================================================================
# https://ru.stackoverflow.com/questions/225896/%D0%97%D0%B0%D0%BF%D1%83%D1%81%D0%BA-bash-%D0%B8%D0%B7-%D1%81%D0%BA%D1%80%D0%B8%D0%BF%D1%82%D0%B0-python-2-7-3
import subprocess
p = subprocess.Popen(['/home/pi/autocopter/build/rssh.sh'], stdout=subprocess.PIPE)
p2 = subprocess.Popen(['/home/pi/autocopter/build/rssh2.sh'], stdout=subprocess.PIPE)
for line in p.readlines():
    print line
for line2 in p2.readlines():
    print line2
# line = p.stdout.readline()
# потом переделать под это https://pythonworld.ru/moduli/modul-subprocess.html
# ==========================================================================================================