def delstr(inputstr,delimiter):
    nstr=inputstr.split(delimiter)
    return nstr
inputstr=input("enter the input: ")
delimiter=input("enter the delimiter: ")
print(delstr(inputstr,delimiter))
