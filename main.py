import os.path
import os
from Reader import Reader
from RuleProcessor import RuleProcessor
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
        reader = Reader(filename,rule_processor,option)
        rule_processor.reader=reader
        reader.read_clips_command()
        buffer = \
        "from graphviz import Digraph\n" + \
        "from pyknow import *\n" +\
        "import os\n\n"
        buffer+=rule_processor.facts_classes
        buffer+="class Engine(KnowledgeEngine):\n"
        buffer+=rule_processor.rules
        buffer+="engine=Engine()\n"
        buffer+="engine.reset()\n"
        buffer+=rule_processor.facts
        buffer+="graph=engine.matcher.print_network()\n"
        buffer+="fd=open(\"graph.vd\",\"w\")\n"
        buffer+="fd.write(graph)\n"
        buffer+="dirpath = os.getcwd()\n"
        buffer+="graph_path = dirpath +"
        buffer+='"\\graph.vd"\n'
        buffer+="output_path = dirpath +"
        buffer+='"\\graph.png"\n'
        buffer+="command_to_execute=\"dot -T png \"+graph_path +\" -o \"+output_path\n"
        buffer+="os.popen(command_to_execute)\n"
        fd = open("result_script.py","w")
        fd.write(buffer)
        dirpath = os.getcwd()
        command_to_execute="py "+dirpath+"\\result_script.py"
        os.popen(command_to_execute)
