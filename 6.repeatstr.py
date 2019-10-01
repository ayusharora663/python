a=input("enter the str: ")
l=list(a)
nstr=''
for i in range(0,len(l)):
    for j in range(i+1,len(l)):
        if(l[j]==l[i]):
            l[j]='*'
    nstr+=l[i]
print(nstr)
