import re
from RuleProcessor import RuleProcessor
class Reader:
    def __init__(self,filename,rule_processor,option):
        if option == 1:
            self.filename=filename
            self.file_object = open(self.filename,"r")
        self.rule_processor=rule_processor
        if option == 2:
            self.found_command= False
            self.buffer = str()
            self.open_parenthesis = 0


    def read_clips_command(self):
        open_parenthesis = 0
        found_command = False
        buffer = str()
        try:
            character = self.file_object.read(1)
            while character:
                if found_command is True:
                    if character == '(':
                        open_parenthesis +=1
                        buffer += character

                    elif character == ')':
                        buffer+=character
                        open_parenthesis -= 1
                        if open_parenthesis < 0:
                            print("Parsing problem at line....")
                            print("Exit...")
                            exit(0)
                        elif open_parenthesis == 0:
                            found_command = False
                            open_parenthesis = 0
                            self.process_clips_command(buffer)
                            buffer = str()
                    else:
                        buffer+=character

                elif character == '(' and found_command is False:
                    open_parenthesis += 1
                    found_command = True
                    buffer+=character
                character = self.file_object.read(1)
        except Exception as e:
            print(e)

    def read_clips_command_from_stdin(self,string):
        for character in string:
            if self.found_command is True:
                        if character == '(':
                            self.open_parenthesis +=1
                            self.buffer += character

                        elif character == ')':
                            self.buffer+=character
                            self.open_parenthesis -= 1
                            if self.open_parenthesis < 0:
                                print("Parsing problem at line....")
                                print("Exit...")
                                exit(0)
                            elif self.open_parenthesis == 0:
                                self.found_command = False
                                self.open_parenthesis = 0
                                self.process_clips_command(self.buffer)
                                self.buffer = str()
                                return True
                        else:
                            self.buffer+=character

            elif character == '(' and self.found_command is False:
                self.open_parenthesis += 1
                self.found_command = True
                self.buffer+=character
        return False


    def process_clips_command(self,command,to_execute=True):
        if to_execute==False:
            pass
        else:
            print("Found clips rule:" + command)
            print("Start proccesing it")
        command=command.replace("  "," ")
        rule = self.find_instruction(command)
        result=list()

        if rule == "assert":
            first_argument=None
            second_argument=None
            arguments = re.search(r"\((.+ \((.+) (.+)\))\)",command)
            if(str(type(arguments)) == "<class '_sre.SRE_Match'>"):
                first_argument = arguments.group(2)
                second_argument = arguments.group(3)
                if to_execute==True:
                    self.rule_processor.assert_process(first_argument,second_argument)
                else:
                    result.append("assert")
                    result.append(first_argument)
                    result.append(second_argument)
                    return (result)
            else:
                arguments = re.search(r"\((.+ \((.+)\))\)",command)
                if(str(type(arguments)) == "<class '_sre.SRE_Match'>"):
                    first_argument = arguments.group(2)
                    second_argument = None
                    if to_execute==True:
                        self.rule_processor.assert_process(first_argument,second_argument)
                    else:
                        result.append(first_argument)
                        result.append(second_argument)
                        return ("assert",result)
        elif rule == "facts":
            print(self.rule_processor.engine.facts)
        elif rule == "exit":
            exit(0)
        elif rule == "clear":
            self.rule_processor.engine.reset()
        elif rule == "reset":
            self.rule_processor.engine.reset()
        elif rule == "run":
            self.rule_processor.engine.run()
        elif rule == "retract":
            arguments = re.search(r"\((\w+) (\d+)\)",command)
            if(str(type(arguments)) == "<class '_sre.SRE_Match'>"):
                id = int(arguments.group(2))
            else:
                return
            self.rule_processor.engine.retract(id+1)
        elif rule== "defrule":
            arrow_position = command.find("=>")
            command_for_arguments1 = command[1:arrow_position]
            command_for_arguments2 = command[arrow_position+2:len(command)-1]
            condition_arguments = re.findall(r"\(.+\)",command_for_arguments1)
            if len(condition_arguments) <= 0:
                return
            rules_arguments = re.findall(r"\(assert\s\(.+\)\)",command_for_arguments2)
            aux_rules_arguments = re.findall(r"\(printout.+\s*\)",command_for_arguments2)
            rules_arguments += aux_rules_arguments
            if to_execute==True:
                self.rule_processor.defrule_process(condition_arguments,rules_arguments)
        elif rule=="printout":
            command=command[:len(command)-1]
            arguments_list = command.split()
            arguments_list = arguments_list[1:]
            result=list()
            result.append("printout")
            for argument in arguments_list:
                result.append(argument)
            return(result)


    def find_instruction(self,command):
        instruction = str()
        command = command[1:]
        instruction += command.split()[0]
        instruction=instruction.replace(')','')
        return instruction


    def parse_nested_paren(self,string, level):
        if len(re.findall("\(", string)) == len(re.findall("\)", string)):
            LeftRightIndex = [x for x in zip(
            [Left.start()+1 for Left in re.finditer('\(', string)],
            reversed([Right.start() for Right in re.finditer('\)', string)]))]

        elif len(re.findall("\(", string)) > len(re.findall("\)", string)):
            return self.parse_nested_paren(string + ')', level)

        elif len(re.findall("\(", string)) < len(re.findall("\)", string)):
            return self.parse_nested_paren('(' + string, level)

        else:
            return 'fail'
        return [string[LeftRightIndex[level][0]:LeftRightIndex[level][1]]]
