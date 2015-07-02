import sys
import re
import os
from os.path import basename
from numpy import mean
import shutil
import commands
import subprocess

#Para correr en milagro y no perder los datos!
#outpdir = os.path.expanduser('~') + "/outputdata/"
outpdir = "./outputdata/"
bindir = "../"
inpdir = "./outputdata/"
tests = ["test1", "test2", "test7"]
startp = 10

def main():
  if not os.path.exists(outpdir):
    os.makedirs(outpdir)
  global startp
  if len(sys.argv) == 2:
    startp = float(sys.argv[1])
  process()


def trimmean(arr, percent):
    n = len(arr)
    k = int(round(n*(float(percent)/100)/2))
    return mean(arr[k+1:n-k])

def process():
    done = 0
    total = (startp/0.1) * 3 * 4
    ou = open(outpdir + "results.csv", "w")
    ou.write("testN, Method, Granularity, Time, tempPoint, RemovedSangui" +'\n')
    #Para cada implementacion
    for impl in tests:
      boutdir = outpdir + "OUT-" + impl + "/"
      if not os.path.exists(boutdir):
        os.makedirs(boutdir)
    granul = startp
    last = (startp/0.1) - 1 
    for x in range(last):
      granul -= 0.1
      param4 = str(granul)
      for test in tests:
        boutdir = outpdir + "OUT-" + test + "/" 
        param1 = inpdir + test +".in"
        for method in range(0,4):
          param2 = boutdir + str(granul).replace('.','-') + "_" + str(method) + ".out"
          param3 = str(method)

          outp = subprocess.check_output([ bindir +"tp", param1, param2, param3, param4]).split(',')
          done += 1
          os.system("clear")
          print("G="+ param4 + "  Set=" + test + "  Method=" + param3 + ' | ' + str(done) + "of" + str(total) + " | Process " + str(float(done*100)/float(total)) + "%")
          print(outp)
          if (len(outp) < 3): continue
          ou.write(test + ',' + str(method) + ',' + str(granul) + ',' + outp[0] + ',' + outp[1] + ',' + outp[2] + "\n")

    ou.close()

def getfiles(dir):
  res = []
  for filen in os.listdir(dir):
    match = re.search(r'test-\w+\.bmp', filen)
    if match:
      res.append(filen)

  return sorted(res)  

if __name__ == '__main__':
  main()