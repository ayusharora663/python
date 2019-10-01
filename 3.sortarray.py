a=[1,100,99,3,5,7,55]
b=[2,4,6,8,10]
c=a+b
print(c)
for i in range(0,len(c)):
    temp=0
    for j in range(i,len(c)):
        if(c[i]>c[j]):
            temp=c[i]
            c[i]=c[j]
            c[j]=temp
print(c)
