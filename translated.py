import sys, math
TEST = int(8)
W = str('WORLD! ')
LI = [1,2,3,4,5]
LI.append(6 )
LI[5] = 7 
TEST **= 2
print('POW(TEST,','2)','=',TEST,)
TEST = math.sqrt(TEST)
print('SQRT(TEST)','=',TEST,)
print(LI,)
while TEST <= 10:
    print('TEST','=',TEST,)
    TEST += 1
