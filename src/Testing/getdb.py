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
PRECISION = 10
tests = ["test1", "test2", "test7"]
granuls = [50.0, 12.5, 10.0, 6.25, 5.0, 4.0, 2.5, 2.0, 1.25, 1.0, 0.8, 0.5, 0.4, 0.25]
#granuls = [float(x)/10 for x in range(100,20,-1)]
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
    total = len(granuls) * 3 * 4
    ou = open(outpdir + "results.csv", "w")
    ou.write("testN, Method, Granularity, Time, tempPoint, RemovedSangui" +'\n')
    #Para cada implementacion
    for impl in tests:
      boutdir = outpdir + "OUT-" + impl + "/"
      if not os.path.exists(boutdir):
        os.makedirs(boutdir)
    for granul in granuls:
      param4 = str(granul)
      for test in tests:
        boutdir = outpdir + "OUT-" + test + "/" 
        param1 = inpdir + test +".in"
        for method in range(0,4):
          param2 = boutdir + str(granul).replace('.','-') + "_" + str(method) + ".out"
          param3 = str(method)
          
          time = []
          for x in range(0,PRECISION+1):
            outp = subprocess.check_output([ bindir +"tp", param1, param2, param3, param4]).split(',')
            if (len(outp) < 3): continue
            microseconds = int(outp[0])
            if (microseconds != 0):
                time.append(microseconds)
          done += 1
          print("G="+ param4 + "  Set=" + test + "  Method=" + param3 + ' | ' + str(done) + "of" + str(total) + " | Process " + "{0:.2f}".format(float(done*100)/float(total)) + "%" + " | " + str(outp))
          ou.write(test + ',' + str(method) + ',' + str(granul) + ',' + str(int(trimmean(sorted(time), 0.25))) + ',' + outp[1] + ',' + outp[2] + "\n")

    ou.close()

if __name__ == '__main__':
  main()