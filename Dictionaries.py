# Python Dictionaries
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict)
print(thisdict["brand"])

# Duplicate values will overwrite existing values:
thisdict = {
  "brand":      "Ford",
  "model":      "Mustang",
  "eletric":    False,
  "year":       1964,
  "year":       2020
}
print(thisdict)

# Print Dictionary Length
print(len(thisdict))

# Print Dictionary type

print(type(thisdict))

### Dictionary access

x = thisdict["model"]
print(x)

x = thisdict.keys()
print(x)


thisdict["color"] = 'white'

print(x)

y = thisdict.values()

print(y)

if "model" in thisdict:
  print("Yes, 'model' is one of the keys in the thisdict dictionary")


car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}

x = car.values()

print(x) #before the change

car["color"] = "red"

car["year"] = '2020'
print(x) #after the change