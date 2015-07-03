import sys
import re
import os
from os.path import basename
from numpy import mean
import shutil
import commands
import subprocess

for filen in os.listdir("./OUT-test1/"):
	subprocess.check_output(["python" ,"graphsol.py", "test1.in", "./OUT-test1/" + filen])
for filen in os.listdir("./OUT-test2/"):
	subprocess.check_output(["python" ,"graphsol.py", "test2.in", "./OUT-test2/" + filen])
for filen in os.listdir("./OUT-test7/"):
	subprocess.check_output(["python" ,"graphsol.py", "test7.in", "./OUT-test7/" + filen])