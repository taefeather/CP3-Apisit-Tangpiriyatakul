OE = int(input("Number For Floor: "))
for x in range(OE):
    space = " " * (OE - x)
    Dok = "*" * (x*2+1)
    print(space,Dok)