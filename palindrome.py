name=['n','i','t','i','n']
length = len(name)
i= 0
a= length -1 
while(i<a):
    if(name[i]==name[a]):
        i=i+1
        a=a-1
        print("its a palindrome")
    else:
        print("its not an palindrome")