from transpiler import *
from sys import argv

if len(argv) < 2:
    tp = FreeLangTranspiler()
else:
    tp = FreeLangTranspiler(argv[2])
code = tp.translate_code()
tp.run_code()