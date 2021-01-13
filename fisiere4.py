with open("globulet.txt", "r") as f:
    a=int(f.readline())
    r = a + 3
    b = (a+r) - 2
    c=a+b+r
    with open("bradut.txt", "w") as f:
        f.write(str(c))