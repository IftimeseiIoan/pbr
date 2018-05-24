import os.path
from FileReader import FileReader
from RuleProcessor import RuleProcessor
from pyknow import *
reader = None
print("Choose one option:")
print("1.Read CLIPS instructions from file")
print("2.Read Clips instructions from STDIN")


option = input('Choose a number: ')
try:
    option=int(option)
except:
    print("You must enter a valid option")
    exit(0)

rule_processor = RuleProcessor()

if option == 1:
   filename = input('Enter the full path of file: ')
   if not os.path.isfile(filename):
       print("The file you specified doesn't exist")
       exit(0)
   else:
        reader = FileReader(filename,rule_processor)
        reader.read_clips_command()
