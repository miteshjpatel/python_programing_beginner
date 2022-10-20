
import this


thisdict = {
    "brand":        "Ford",
    "model":        "Mustang",
    "year":         1064
}


#Print Key value
for x in thisdict:
    print(x)
#Print value
for x in thisdict:
    print(thisdict[x])    

# Print with loop in keys
for x in thisdict.keys():
    print(x)

# Loop throught both keys and values
for x, y in thisdict.items():
    print(x, y)   

# Make a copy with the copy

mydict = thisdict.copy()
print(mydict)