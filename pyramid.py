import time

symbol = input("What symbol to use ? ")
indent = " "
maxSymbol = int(input("How big do you wants the base to be? : "))
    
for i in range(int(maxSymbol/2)):
    print (indent*int((maxSymbol/2)-i) + symbol*(i*2) + indent*int((maxSymbol/2)-i))
    time.sleep(0.5)
#.