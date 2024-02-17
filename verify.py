files = input().split()

inp = open(files[0],"r")
out = open(files[1],"r")

for line in inp:
    try:
        a,b,c = map(float,line.split())
        x = float(out.readline())
    except:
        continue
    if :
        print("\tCorrect")
    else:
        print("\tWrong")
        print("\t\t",a*(x**2) + b*(x**0.5), c)
inp.close()
out.close()
