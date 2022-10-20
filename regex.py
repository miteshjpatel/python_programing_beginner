# RegEx in Python


import re

txt = "The rain in Spain"
x = re.search("^The.*Spain$", txt)

if x:
  print("YES! We have a match!")
else:
  print("No match")


# The regular expression looks for any words that starts with an upper case "S":
x = re.search(r"\bS\w+", txt)
print(x.group())

# Print the string passed into the function:
x = re.search(r"\bS\w+", txt)
print(x.string)
