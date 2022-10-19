# Python - Sort Lists

thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort()     #Sort the list
print(thislist)
thislist.sort(reverse=True) #Sort the list in reverse
print(thislist)

thislistnum = [100, 50, 65, 82, 23]
thislistnum.sort()
print(thislistnum)
thislistnum.sort(reverse=True)
print(thislistnum)


def myfunc(n):
    return abs(n - 50)

thislistnum.sort(key = myfunc)

print(thislistnum)