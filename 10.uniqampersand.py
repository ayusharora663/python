a=['apple','orange','pear','apple','orange','peas','peas','melon', 'Peas']
s=list(set(a))
nstr=''
print(s)
print(len(s))
for i in range(0,len(s)):
    nstr+=s[i]
    if(i==len(s)-1):
            break
    if(i==len(s)-2):
       nstr+='&'
    else:
        nstr+=','
print(nstr)
