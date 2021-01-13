with open("input.txt", "r") as f:
    c =  int(f.read())
d = (c-2, c-1, c, c+1, c+2)
with open("output.txt", "w") as f:
    f.write(str(d))
