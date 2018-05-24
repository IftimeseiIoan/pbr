import re
from RuleProcessor import RuleProcessor
class FileReader:
    def __init__(self,filename,rule_processor):
        self.filename=filename
        self.file_object = open(self.filename,"r")
        self.rule_processor=rule_processor

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
                            #print ("Found clips rule :" + buffer)
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


    def process_clips_command(self,command):
        print("Found clips rule:" + command)
        print("Start proccesing it")
        command.replace("  "," ")
        rule = self.find_instruction(command)

        if rule == "assert":
            arguments = re.search(r"\((\w+ \((\w+) (\w+)\))\)",command)
            if(str(type(arguments)) == "<class '_sre.SRE_Match'>"):
                first_argument = arguments.group(2)
                second_argument = arguments.group(3)
                self.rule_processor.assert_process(first_argument,second_argument)
            else:
                return

    def find_instruction(self,command):
        instruction = str()
        command = command[1:]
        instruction += command.split()[0]
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
