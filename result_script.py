from graphviz import Digraph
from pyknow import *
import os

class PrinterDoesNotPrint(Fact):
	 pass
class ARedLightIsFlashing(Fact):
	 pass
class PrinterIsNotRecognised(Fact):
	 pass
class Engine(KnowledgeEngine):
	@Rule(PrinterDoesNotPrint(PrinterDoesNotPrint='yes')&ARedLightIsFlashing(ARedLightIsFlashing='yes')&PrinterIsNotRecognised(PrinterIsNotRecognised='yes'))
	def PrinterDoesNotPrint_yes_ARedLightIsFlashing_yes_PrinterIsNotRecognised_yes(self):
		print("Check the printer-computer cable  ")
		print("Ensure printer software is installed  ")
		print("Check/replace ink  ")
	@Rule(PrinterDoesNotPrint(PrinterDoesNotPrint='yes')&ARedLightIsFlashing(ARedLightIsFlashing='yes')&PrinterIsNotRecognised(PrinterIsNotRecognised='no'))
	def PrinterDoesNotPrint_yes_ARedLightIsFlashing_yes_PrinterIsNotRecognised_no(self):
		print("Check/replace ink  ")
		print("Check for paper jam  ")
engine=Engine()
engine.reset()
graph=engine.matcher.print_network()
fd=open("graph.vd","w")
fd.write(graph)
dirpath = os.getcwd()
graph_path = dirpath +"\graph.vd"
output_path = dirpath +"\graph.png"
command_to_execute="dot -T png "+graph_path +" -o "+output_path
os.popen(command_to_execute)
