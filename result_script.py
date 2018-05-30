from graphviz import Digraph
from pyknow import *
import os

class color(Fact):
	 pass
class duck(Fact):
	 pass
class uaic(Fact):
	 pass
class refrigerator(Fact):
	 pass
class Engine(KnowledgeEngine):
	@Rule(refrigerator(refrigerator='light on')&refrigerator(refrigerator='door open'))
	def refrigerator_light_on_refrigerator_door_open(self):
		engine.declare(Fact(refrigerator='food spoiled'))
		print("action activate-sprinkler-system ")
engine=Engine()
engine.reset()
engine.declare(color(color='green'))
engine.declare(duck(duck='None'))
engine.declare(uaic(uaic='lame'))
graph=engine.matcher.print_network()
fd=open("graph.vd","w")
fd.write(graph)
dirpath = os.getcwd()
graph_path = dirpath +"\graph.vd"
output_path = dirpath +"\graph.png"
command_to_execute="dot -T png "+graph_path +" -o "+output_path
os.popen(command_to_execute)
