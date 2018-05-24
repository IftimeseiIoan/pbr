from pyknow import *

class Light(Fact):
   pass

class RuleClass(KnowledgeEngine):
    @Rule(Light(color='green'))
    def green_light(self):
           print("Walk")



class RuleProcessor:
    def __init__(self):
        self.facts=Fact()
        self.classes = list()

    def assert_process(self,argument1,argument2):
        if argument1 in self.facts:
            self.facts[argument1]=argument2
        else:
            self.facts[argument1]=argument2
            new_class = type(argument1,(Fact,),{})
            self.classes.append(new_class)
            print(new_class)

'''
        new_class = type("NewClass", (object,), {
        "string_val": "this is val1",
        "int_val": 10,
        "__init__": constructor,
        "func_val": some_func,
        "class_func": some_class_method
    })
'''
