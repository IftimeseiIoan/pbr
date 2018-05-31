import os.path
import os

from kivy.uix.label import Label

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

    ################  create examples ##############
    #buffer += '"\\example1.png"\n'
    #buffer += '"\\example2.png"\n'

    buffer += "command_to_execute=\"dot -T png \"+graph_path +\" -o \"+output_path\n"
    buffer += "os.popen(command_to_execute)\n"
    fd = open("result_script.py", "w")
    fd.write(buffer)
    dirpath = os.getcwd()
    command_to_execute = "py " + dirpath + "\\result_script.py"
    os.popen(command_to_execute)

class MainApp(App):
    dirpath = os.getcwd()
    image = Image(pos_hint={'top': 0.9})
    label = Label(text='Enter path to .clp file.',size_hint=(1, 0.07))
    textinput = TextInput(size_hint=(1, 0.07))
    window = BoxLayout(orientation='vertical')
    buttons = BoxLayout(orientation='horizontal',size_hint=(1, 0.07))


    def build(self):
        self.image.keep_ratio = False
        self.image.allow_stretch = True
        button1 = Button(text="Generate Rete",
                         background_normal= '',background_color=(.1, .3, .3, .9))
        button1.bind(on_press=self.show_rete)

        button2 = Button(text="Show example 1",
                         background_normal='', background_color=(.2, .5, .5, .8))
        button2.bind(on_press=self.show_example1)

        button3 = Button(text="Show example 2",
                         background_normal='', background_color=(.1, .6, .5, .9))
        button3.bind(on_press=self.show_example2)

        self.window.add_widget(self.label)
        self.window.add_widget(self.textinput)
        self.window.add_widget(self.image)
        self.buttons.add_widget(button1)
        self.buttons.add_widget(button2)
        self.buttons.add_widget(button3)
        self.window.add_widget(self.buttons)
        return self.window

    def show_rete(self, value):
        filename=self.textinput.text
        if not os.path.isfile(filename):
            self.label.text="The file does not exist. Enter another path."
        else:
            generate_rete(filename)
            self.image.source = self.dirpath + "\\graph.png"
            self.image.reload()

    def show_example1(self, value):
        self.image.source = self.dirpath + "\\example1.png"
        self.image.reload()

    def show_example2(self, value):
        self.image.source = self.dirpath + "\\example2.png"
        self.image.reload()


if __name__ == '__main__':
    MainApp().run()
