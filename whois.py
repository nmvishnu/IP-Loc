#Simple IP Location check using Whois
#Created by Vishnu N M on 14th May 2020
#IMPORTANT: VIEW README

import sys, getopt
import subprocess
import time

def main(argv):
   inputfile = ''
   outputfile = ''
   try:
      opts, args = getopt.getopt(argv,"hi:o:",["ifile=","ofile="])
   except getopt.GetoptError:
      print 'whois.py -i <inputfile> -o <outputfile>'
      sys.exit(2)
   for opt, arg in opts:
      if opt == '-h':
         print 'whois.py -i <inputfile> -o <outputfile>'
         sys.exit()
      elif opt in ("-i", "--ifile"):
         inputfile = arg
      elif opt in ("-o", "--ofile"):
         outputfile = arg
   print 'Input file is "', inputfile
   print 'Output file is "', outputfile

   List = open(inputfile,"rb").readlines()
   List = ' '.join(List).split() 

   for i in List: 
      print(i)
      cmd = "whois "+ i + " | grep 'city:\|City:\|country:\|Country:' >> " + outputfile
      cmd1 = "echo " + i + "\"\n\" >> " + outputfile
      subprocess.call(cmd, shell=True) 
      subprocess.call(cmd1, shell=True) 
      time.sleep(1.5) #Default time delay is 1.5 seconds. Optimal for > 1000IPs

if __name__ == "__main__":
   main(sys.argv[1:])
