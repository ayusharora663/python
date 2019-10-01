a=[1,21,53,84,50,66,7,38,9]
evenlist=[]
oddlist=[]
for i in a:
    if i%2==0:
        evenlist.append(i)
    else:
        oddlist.append(i)
print("even list",evenlist)
print("odd list",oddlist)
