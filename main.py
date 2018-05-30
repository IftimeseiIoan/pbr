import os.path
import os

from Reader import Reader
from RuleProcessor import RuleProcessor

from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.image import Image
from kivy.uix.textinput import TextInput


def generate_rete(filename):
    rule_processor = RuleProcessor()
    reader = Reader(filename, rule_processor, 1)
    rule_processor.reader = reader
    reader.read_clips_command()
    buffer = \
        "from graphviz import Digraph\n" + \
        "from pyknow import *\n" + \
        "import os\n\n"
    buffer += rule_processor.facts_classes
    buffer += "class Engine(KnowledgeEngine):\n"
    buffer += rule_processor.rules
    buffer += "engine=Engine()\n"
    buffer += "engine.reset()\n"
    buffer += rule_processor.facts
    buffer += "graph=engine.matcher.print_network()\n"
    buffer += "fd=open(\"graph.vd\",\"w\")\n"
    buffer += "fd.write(graph)\n"
    buffer += "dirpath = os.getcwd()\n"
    buffer += "graph_path = dirpath +"
    buffer += '"\\graph.vd"\n'
    buffer += "output_path = dirpath +"
    buffer += '"\\graph.png"\n'
    buffer += "command_to_execute=\"dot -T png \"+graph_path +\" -o \"+output_path\n"
    buffer += "os.popen(command_to_execute)\n"
    fd = open("result_script.py", "w")
    fd.write(buffer)
    dirpath = os.getcwd()
    command_to_execute = "py " + dirpath + "\\result_script.py"
    os.popen(command_to_execute)

class MainApp(App):
    image = Image(pos_hint={'top': 0.9})
    textinput = TextInput(text='Enter path', size_hint=(1, 0.08))
    window = BoxLayout(orientation='vertical')


    def build(self):
        self.window.add_widget(self.textinput)
        self.image.keep_ratio = False
        self.image.allow_stretch = True
        button1 = Button(text="Generate Rete", size_hint=(0.2, 0.1))
        button1.bind(on_press=self.show_rete)
        self.window.add_widget(self.image)
        self.window.add_widget(button1)
        return self.window

    def show_rete(self, value):
        filename=self.textinput.text
        generate_rete(filename)
        dirpath = os.getcwd()
        self.image.source = dirpath + "\\graph.png"
        self.image.reload()

if __name__ == '__main__':
    MainApp().run()
