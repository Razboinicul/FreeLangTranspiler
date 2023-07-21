from transpiler import *
from sys import argv

if len(argv) < 2:
    tp = FreeLangPyTranspiler()
else:
    tp = FreeLangPyTranspiler(argv[1])
code = tp.translate_code()
tp.run_code()