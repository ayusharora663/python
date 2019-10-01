a=input("enter string")
lista=a.split(" ")
nstr=""
for i in range(len(lista)-1,-1,-1):
    nstr+=(lista[i]+" ")
print(nstr.rstrip())
