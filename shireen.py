def upper(a):
    i=0
    c=0
    while i<len(a):
        if a[i]>="A "and a[i]<"Z":
            c=c+1
            print(c)
        elif a[i]>="a" and a[i]<="z":
            c=c+1
            print(c)
        i=i+1
upper("Today Is My Hacton")