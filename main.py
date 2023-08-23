from transpiler import *
from sys import argv

if len(argv) < 2:
    tp = FreeLangPyTranspiler()
else:
    tp = FreeLangPyTranspiler(argv[1])
with open("translated.py", "w+") as f:
    code = tp.translate_code()
    f.write(code)
tp.run_code()