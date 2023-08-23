import sys
translated_code = """import sys, math\n"""

class FreeLangPyTranspiler:
    def __init__(self, filename="main.free"):
        global translated_code
        self.filename = filename
        self.tabs = ""
        f = open(self.filename)
        c = f.readlines()
        self.code = []
        for i in c:
            if i != "":
                self.code.append(i.removesuffix("\n"))
        self.PC = 0
    
    def run_code(self):
        global translated_code
        exec(translated_code)
    
    def translate_code(self):
        global translated_code
        for self.PC in range(len(self.code)):
            self.execute_command(self.code[self.PC])
        return translated_code
    
    def execute_command(self, line):
        global translated_code
        args = line.split(" ")
        cmd = args.pop(0)
        if cmd.startswith("#") or cmd.startswith("//") or cmd.startswith("--"): return
        if line.replace(" ", "") == "": return
        if cmd == "PRINT":
            text = ""
            for i in args: 
                if i.startswith("VAR:"):
                    i = i.removeprefix("VAR:")
                    if "::" in i:
                        x = i.split("::")
                        text += f"{x[0]}[{x[1]}]"+","
                    else:
                        text += f"{i}"+","
                else:
                    text += f"'{i}'"+","
            translated_code += self.tabs+f"print({text})"+"\n"
        elif cmd == "VAR":
            if args[0] == "INT":
                var = args[2].removesuffix("-FREE")
                translated_code += self.tabs+f"{args[1]} = int({var})"+"\n"
            elif args[0] == "STR":
                var = ""
                for i in args[2:]: var += i+" "
                translated_code += self.tabs+f"{args[1]} = str('{var}')"+"\n"
            elif args[0] == "LIST":
                var = "["
                for i in args[2:]: var += i+","
                else:
                    var = var.removesuffix(",")
                    var += "]"
                translated_code += self.tabs+f"{args[1]} = {var}"+"\n"
            elif args[0] == "LIST_OBJECT":
                var = ""
                x = args[1].split("::")
                for i in args[2:]: var += i+" "
                translated_code += self.tabs+f"{x[0]}.append({var})"+"\n"
        elif cmd == "ADD":
            args[0] = args[0].removeprefix("VAR:")
            if args[1].endswith("-FREE"):
                args[1] = args[1].removesuffix("-FREE")
                translated_code += self.tabs+f"{args[0]} += {args[1]}"+"\n"
            else:
                translated_code += self.tabs+f"{args[0]} += '{args[1]}'"+"\n"
        elif cmd == "SUB":
            args[0] = args[0].removeprefix("VAR:")
            args[1] = args[1].removesuffix("-FREE")
            translated_code += self.tabs+f"{args[0]} -= {args[1]}"+"\n"
        elif cmd == "MUL":
            args[0] = args[0].removeprefix("VAR:")
            args[1] = args[1].removesuffix("-FREE")
            translated_code += self.tabs+f"{args[0]} *= {args[1]}"+"\n"
        elif cmd == "DIV":
            args[0] = args[0].removeprefix("VAR:")
            args[1] = args[1].removesuffix("-FREE")
            translated_code += self.tabs+f"{args[0]} /= {args[1]}"+"\n"
        elif cmd == "POW":
            args[0] = args[0].removeprefix("VAR:")
            args[1] = args[1].removesuffix("-FREE")
            translated_code += self.tabs+f"{args[0]} **= {args[1]}"+"\n"
        elif cmd == "SQRT":
            args[0] = args[0].removeprefix("VAR:")
            translated_code += self.tabs+f"{args[0]} = math.sqrt({args[0]})"+"\n"
        elif cmd == "IF":
            if args[0].startswith("VAR:"): args[0] = args[0].removeprefix("VAR:")
            if args[0].endswith("-FREE"): args[0] = args[0].removesuffix("-FREE")
            if args[2].startswith("VAR:"):
                args[2] = args[2].removeprefix('VAR:')
                translated_code += self.tabs+f"if {args[0]} {args[1]} {args[2]}:"+"\n"
            else:
                if args[2].endswith("-FREE"):
                    args[2] = args[2].removesuffix('-FREE')
                    translated_code += self.tabs+f"if {args[0]} {args[1]} {args[2]}:"+"\n"
                else:
                    translated_code += self.tabs+f"if {args[0]} {args[1]} '{args[2]}':"+"\n"
            self.tabs += "    "
        elif cmd == "WHILE":
            if args[0].startswith("VAR:"): args[0] = args[0].removeprefix("VAR:")
            if args[0].endswith("-FREE"): args[0] = args[0].removesuffix("-FREE")
            if args[2].startswith("VAR:"):
                args[2] = args[2].removeprefix('VAR:')
                translated_code += self.tabs+f"while {args[0]} {args[1]} {args[2]}:"+"\n"
            else:
                if args[2].endswith("-FREE"):
                    args[2] = args[2].removesuffix('-FREE')
                    translated_code += self.tabs+f"while {args[0]} {args[1]} {args[2]}:"+"\n"
                else:
                    translated_code += self.tabs+f"while {args[0]} {args[1]} '{args[2]}':"+"\n"
            self.tabs += "    "
        elif cmd == "LOOP":
            translated_code += self.tabs+f"while True:"+"\n"
            self.tabs += "    "
        elif cmd == "END":
            try:
                s_obj = slice(0, 4)
                #print(self.tabs[s_obj])
            except:
                pass
        elif cmd == "SET":
            var = ""
            x = args[0].split("::")
            for i in args[1:]: var += i+" "
            translated_code += self.tabs+f"{x[0]}[{x[1]}] = {var}"+"\n"
        elif cmd == "QUIT":
            translated_code += self.tabs+f"sys.exit()"+"\n"
        else:
            raise SyntaxError("Command not found")