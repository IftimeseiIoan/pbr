from pyknow import *
import re
new_class= None

class Engine(KnowledgeEngine):
    def execute(self,buffer,function_name):
        exec(buffer,globals())
        function = self[function_name]
        print(function)


class RuleProcessor:
    def __init__(self):
        self.facts=Fact()
        self.classes = list()
        self.engine = Engine()
        self.engine.reset()
        self.reader = None
        self.rules=str()
        self.facts=str()
        self.facts_classes=str()

    def assert_process(self,argument1,argument2):
        print("in assert "+argument1+" " +str(argument2))
        declare_class = "class " + str(argument1).replace('-',"_") +"(Fact):\n\t pass\n"
        self.facts_classes+=declare_class

        declare_string = str()
        declare_string = "engine.declare(" + str(argument1).replace('-',"_") + '(' +  str(argument1).replace('-',"_") + "='" + str(argument2) + "'))\n"
        self.facts+=declare_string

    def defrule_process(self,condition_arguments,rules_arguments):
        buffer = str()
        buffer += "\t@Rule("
        for condition in condition_arguments:
            condition = condition[1:len(condition)-1]
            arguments = condition.split(" ",1)
            argument1=arguments[0]
            argument2=arguments[1]
            buffer += str(argument1).replace('-',"_")+"("+str(argument1).replace('-',"_") + '=' +"'"+str(argument2)+"')&"
        buffer=buffer[:len(buffer)-1]
        buffer += ')\n'
        #for argument in arguments:
        buffer+="\tdef "
        for condition in condition_arguments:
            condition=condition[1:len(condition)-1]
            aux_conditions=condition.split()
            if self.facts_classes.find("class "+aux_conditions[0])==-1:
                self.facts_classes+= "class " + str(aux_conditions[0]).replace('-',"_") +"(Fact):\n\t pass\n"
            condition=str(condition).replace(" ","_")
            buffer+=str(condition).replace('-',"_")+"_"
        buffer=buffer[:len(buffer)-1]
        buffer+="(self):\n"
        counter=0
        for rule in rules_arguments:
            parse_result = self.reader.process_clips_command(rule,False)
            if len(parse_result)>=2:
                command=parse_result[0]
                if command=="assert":
                    arguments=parse_result[1:]
                    if len(arguments)==2:
                        buffer+="\t\tengine.declare(Fact("
                        ok=0
                        for aux in str(arguments[0]).split():
                            if ok==0:
                                buffer=buffer+aux+"="+"'"
                                ok=1
                            else:
                                buffer+=aux
                                buffer+=" "

                        buffer=buffer+str(arguments[1])+"'"+"))\n"
                    else:
                        buffer=buffer+"\t\tengine.declare(Fact("+"'"+str(arguments[0])+"'"+"))\n"
                elif command=="printout":
                    arguments=parse_result[1:]

                    buffer+="\t\tprint("
                    local_buffer=str()
                    for argument in arguments:
                        if argument=="crlf":
                            pass
                        elif argument=="t":
                            pass
                        else:
                            new_argument=argument
                            local_buffer+=new_argument.replace('"','')
                            local_buffer+=" "
                    buffer=buffer+'"'+local_buffer+'"'+")\n"
        self.rules+=buffer
