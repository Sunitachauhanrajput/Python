# list=[0.4,3,"sunita",6,"rani"]
# list1=[]
# list2=[]
# list3=[]
# i=0
# while i<len(list):
#     if i==str:
#         list1.append(str)
#     j=0
#     while j<len(list):
#         if j==float:
#             list2.append(float)
#         k=0
#         while k<len(list):
#             if k==int:
#                 list3.append(int)
#             k=k+1
#         j=j+1
#     i=i+1
# print(list1)
# print(list2)
# print(list3)

# dic={1:"x",2:"y",3:{"a":"xxxx","b":"yyyyyy"}}
# for i in dic:
#     if type(dic[i])==dict:
#         for j in dic[i]:
#             if j=='a':
#                 dic[i].pop(j)
# print(dic)


# a="himani"
# b=1.2
# c=1
# d=str(b)
# e=str(c)
# f=int(b)
# print(d+a+e)
# g=f+c
# print(a+str(g))


# i=0
# while i<10:
#     i=i+2
#     print(i)
#     if i==10:
#         i=-1


# x=(2,5,8,3)
# print(x)

# i=0
# while (i<=10):
#     # if i==2:
#     #     continue
#     if i==6:
#         pass
#     # if i==7:
#     #     break
#     i=i+1
#     print(i)

# list="this is navgurkul"
# k=list.split(" ")
# #print(k)
# x="iteams"
# y="space"
# dict={"a":1}
# i=0
# c=0
# dic={}
# while i<len(k):
#      c=c+1
#      dict.update({"iteams":k[i]})
#      dict.update({"space":c})
#      i=i+1
# print(dict)



# a="3333"

# if a.isalpha():
#     print("yes")
# else:
#     print("digit is not found")
        

# pattern     +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# r=1
# while r<=3:
#     c=1
#     while c<=3:
#         if ((r==1 and c==2) or (r==2 and (c==1 or c==3)) or (r==3 and (c==2))):
#             print("*",end=" ")
#         else:
#             print(" ",end=" ")
#         c=c+1
#     print()
#     r=r+1



# def FindSumOfRemainders(n, div):
#       #write your code here
#     rem=0
#     for i in range(1,n+1,1):
#         if (i<div):
#             rem=rem+i
#         else:
#             x=i%div
#             rem=rem+x
# result = FindSumOfRemainders(12,4)
# print(result)


# k = int(input("enetr"))
# n = int(input("enter how many element"))
# l = []

# for i in range(0, n):
#     p = int(input("enter p"))
#     l.append(p)
    
# def SumOfNumbers(l,n,k):
#   #write your code here
#     for i in range(len(l)):
#         print(i)
    
    
# result = SumOfNumbers(l,n,k)
# print(result)


# def kthSmallest(arr, n, k):

# if __name__=='__main__':
#     n = len(arr)
#     k = 3
#     print("K'th smallest element is",
#     kthSmallest(arr, n, k))

# arr = [4,7,9,2,6,1]
# arr.sort()
# k=2
# print(arr[k-1])
# print(arr[-(k)])



# a=11
# b=1
# c=3
# if (1%3 and 3%11):
#     a=a+19
# print(a+c-b)


# s="sunita"
# for i in s:
#     print(i)

# input1=input("enter your first word ")
# input2=input("enter your second word ")
# result=0
# if len(input1)==len(input2):
#     for i in input1:
#         if i in input2:
#             result=result+1
#     if len(input1)==result:
#         print("YES")
#     else:
#         print("NO")
# else:
#     print("NO")

# n=int(input("enter your number"))
# m=int(input("enter your  range number"))
# divisible=0
# notDivisible=0
# for i in range(m+1):
#     if i%n==0:
#         divisible=divisible+i
#     else:
#         notDivisible=notDivisible+i
# differance=notDivisible-divisible
# print(differance)
                                    # r: 7
                                    # unit: 2
                                   # n: 8
                                    # arr: 2 8 3 5 7 4 1 2

# def func():
#     arr=[]
#     for i in range(n):
#         item=int(input())
#         arr.append(item)
#     amount=r*unit
#     sum=0
#     if len(arr)==0:
#         return -1
#     else:
#         for i in range(len(arr)):
#             sum=sum+arr[i]
#             if sum>=amount:
#                 return i+1
#             break
#         if sum<amount:
#             return 0
            
# r=int(input())
# unit=int(input())
# n=int(input())
# print(func())


# quastionn+++++++++++++++++++++++++++++++
# 'A' denotes AND operation 
# 'B' denotes OR operation 
# 'C' denotes XOR operation
# 'I' denotes 1 operation 
# 'O' denotes 0 operation  
# str="ICOCICIAOBI "
# output=1
        
        
# At least 4 characters 
# At least one numeric digit 
# At least one Capital letter 
# Must not have space or slash (/) 
# Starting character must not be a number 

# 
# students = [['Harry', 37.21], ['Berry', 37.21],
#                    ['Tina', 37.2], ['Akriti', 41], ['Harsh', 39]] 
# for i in students:
#     for j in i:
        
# # a=list[0]
# # for i in list:
# #     for j in list:
# #         if 

# for i in range (len(Number)):
#     for j in range(i + 1, len(Number)):
#         if(Number[i] > Number[j]):
#             Number[i],Number[j]=Number[j], Number[i]

# print("Element After Sorting List in Ascending Order is : ", Number)
# list=[]
# for i in Number:
#     if i  not in list:
#         list.append(i)
# print(list[-2])



# str="sunita chauhan"
# x=str.split()
# list=[]
# for i in x:
#     y=i[0].upper()
#     a=i.replace(i[0],y)
#     list.append(a)
# print(list)
    
    
    
# def solve(s):
#     x=s.split()
#     list=[]
#     for i in x:
#         y=i[0].upper()
#         a=i.replace(i[0],y)
#         print(a,end=" ")
# str=input()
# solve(str)
    

    
# for i in range(1,int(input())+1): #More than 2 lines will result in 0 score. Do not leave a blank line also
#     print(str(i)*i)

# b 3
# a 2
# c 2


# s="aabbbccde"
# dic={}
# for i in s:
#     c=0
#     max=0
#     for j in s:
#         if i==j:
#             c=c+1
#     if c>1:
#         dic[i]=c

# T=int(input())
# array=[]
# for i in range(T):
#     arr=[]
#     c=input()
#     d=input()
#     l=input()
#     arr.append(c)
#     arr.append(d)
#     arr.append(l)
#     array.append(arr)
# for i in array:
#     if int(i[2])>=int(i[0])*4:
#         if int(i[2])%4==0:
#             print(True)
#     else:
#         print(False)
    


# T=int(input())
# for i in range(T):
#     c,d,l=map(int,input().split())
#     leg=d*4
#     if l>=leg and l%4==0:
#             print(True)
#     else:
#         print(False)

# s = input("enter")
# if chr in s:
#     print("yes")
# else:
#     print("no")

# T=int(input())
# for i in range(T):
#     N=int(input())
#     A=map(int,input().split())
#     arr=list(A)
#     arr.sort()
#     c=0
#     uniqe_list=[]
#     for j in range(len(arr)):
#         if arr[j]!=0 and (arr[j] not in uniqe_list):
#             uniqe_list.append(arr[j])
#             c=c+1
#     print(c)
        
# T=int(input())
# for i in range(T):
#     N=int(input())
#     A=list(map(int,input().split()))
#     x=set(A)
#     print(x)

# if __name__ == '__main__':
#     list=[]
#     for i in range(int(input())):
#         l=[]
#         name = input()
#         score = float(input())
#         l.append(name)
#         l.append(score)
#         list.append(l)
# list=[["r",3],["s",4],["m",2]]
# for i in list:
   
   
# t=int(input())
# for i in t:
#     n=int(input())
#     a=list(map(int,input().split()))
#     sum=0
#     for j in a:
#         sum=sum+j
#     if sum%2==0:
#         print("0")
#     elif sum%2!=0:
#         for x in a:
#             p=max(0,⌈a[i]/2⌉−1)
#             a[i]=p
#             sum=0
#             for  y in a:
#                 sum=sum+y
#             if sum%2==0:
#                 print("1")
#                 break
#             else:
#                 print("-1")
    
    
# T=int(input())
# for i in range(T):
#     N,K,X,Y=map(int,input().split())
#     current_covid_city=X
#     while(True):
#         if current_covid_city==Y:
#             print("yes")
#             break
#         current_covid_city=(current_covid_city+K)%N
#         if current_covid_city==X:
#             print("no")
#             break


# l=[3,6,9,2,3,4]
# print(max(l))

# str is a valid password if it satisfies the below conditions. – At least 4 
# characters – At least one numeric digit – At Least one Capital Letter – 
# Must not have space or slash (/) – Starting character must not be a nu

def CheckPassword(str1):
    digit=0
    length=0
    upper=0
    lower=0
    special=0
    result=0
    if len(str1)>=4 :
        if "1"<=str1[0]<="9" or str1[0]=="0":
            return 0
        if " " in str1 or "/" in str1:
            return 0
        else:
            for i in str1:
                if "A"<=i<="Z" :
                    upper+=1
                if "1"<=i<="9" or i=="0":
                    digit+=1
                if(i=='@'or i=='$' or i=='_' or i=='#'):
                    special+=1
            if upper>=1 and digit>=1 and special>=1:
                return 1
    else:
        return 0
s=input()
print(CheckPassword(s))