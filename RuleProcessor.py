from pyknow import *

new_class= None

class Engine(KnowledgeEngine):
    pass


class RuleProcessor:
    def __init__(self):
        self.facts=Fact()
        self.classes = list()
        self.engine = Engine()
        self.engine.reset()

    def assert_process(self,argument1,argument2):
        declare_class = "class " + str(argument1) +"(Fact):\n\t pass"
        if argument1 in self.facts:
            self.facts[argument1]=argument2
        else:
            self.facts[argument1]=argument2
            new_class = type(argument1,(Fact,),{})
            self.classes.append(new_class)

        exec(declare_class,globals())
        declare_string = str()
        declare_string = "self.engine.declare(" + str(argument1) + '(' +  str(argument1) + "='" + str(argument2) + "'))"
        print(declare_string)
        exec(declare_string)
        #print(self.engine.facts)



'''
        new_class = type("NewClass", (object,), {
        "string_val": "this is val1",
        "int_val": 10,
        "__init__": constructor,
        "func_val": some_func,
        "class_func": some_class_method
    })
'''
