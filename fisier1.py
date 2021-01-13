with open("numere.txt", "r") as f:
    a=int(f.readline())
    b=int(f.readline())
if a > b:
    c = str(a)
if b > a:
    c = str(b)
if a==b:
    c="Nr sunt egale"
with open("minim.txt", "w") as f:
    f.write(c)