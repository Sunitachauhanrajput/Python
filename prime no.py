m=1
while m<=100:
    p=0
    i=1
    while i<=m:
        if m%i==0:
            p=p+1
        i=i+1
    if p==2:
        print(m)
    m=m+1