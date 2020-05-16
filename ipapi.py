#Simple IP Location check using IP API
#Created by Vishnu N M on 16th May 2020
#ip-api limit per day 1000. Monthly 30000

import sys, getopt
import subprocess
import time

def main(argv):
   inputfile = ''
   outputfile = ''
   try:
      opts, args = getopt.getopt(argv,"hi:o:",["ifile=","ofile="])
   except getopt.GetoptError:
      print 'ipapi.py -i <inputfile> -o <outputfile>'
      sys.exit(2)
   for opt, arg in opts:
      if opt == '-h':
         print 'ipapi.py -i <inputfile> -o <outputfile>'
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
      cmd = "curl https://ipapi.co/"+ i + "/country/ >> " + outputfile
      cmd1 = "echo \"\t\"" + i +" >> " + outputfile
      subprocess.call(cmd, shell=True) 
      subprocess.call(cmd1, shell=True) 
      time.sleep(0.5)

if __name__ == "__main__":
   main(sys.argv[1:])
