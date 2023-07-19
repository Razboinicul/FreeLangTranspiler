import sys
translated_code = """"""

class FreeLangTranspiler:
    def __init__(self, filename="main.free"):
        global translated_code
        self.filename = filename
        self.tabs = ""
        f = open(self.filename)
        c = f.readlines()
        self.code = []
        for i in c: self.code.append(i.removesuffix("\n"))
        self.PC = 0
    
    def run(self):
        global translated_code
        for self.PC in range(len(self.code)):
            self.execute_command(self.code[self.PC])
        c = compile(translated_code, 'sumstring', 'exec')
        print("code:\n", translated_code)
        print("\nOutput:\n")
        exec(translated_code)
    
    def execute_command(self, line):
        global translated_code
        args = line.split(" ")
        cmd = args[0]
        args.pop(0)
        if cmd == "PRINT":
            text = ""
            for i in args: 
                if i.startswith("VAR:"):
                    i = i.removeprefix("VAR:")
                    text += f"{i}"+","
                else:
                    text += f"'{i}'"+","
            translated_code += self.tabs+f"print({text})"+"\n"
        elif cmd == "VAR":
            if args[0] == "INT":
                var = args[2].removesuffix("-FREE")
                translated_code += self.tabs+f"{args[1]} = {var}"+"\n"
            elif args[0] == "STR":
                var = ""
                for i in args[2:]: var += i+" "
                translated_code += self.tabs+f"{args[1]} = '{args[2]}'"+"\n"
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
        elif cmd == "END":
            s_obj = slice(0, 4)
            print(self.tabs[s_obj])