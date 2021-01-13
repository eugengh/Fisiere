with open("numere.txt", "r") as f:
    a=int(f.readline())
    b=int(f.readline())
if a > b:
    c = str(a*2)
    d= str(b*3)
if b > a:
    c = str(b*2)
    d= str(a*3)
if a==b:
    c="Nr sunt egale"
with open("produs.txt", "w") as f:
    f.write(c)
    f.write("\n")
    f.write(d)