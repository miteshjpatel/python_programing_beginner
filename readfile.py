import os

print(os.pardir)

if os.path.exists("demofile.txt"):
    print("Files exists")
    f = open("demofile.txt", "a")
    f.write("Now the file has more content!")
    f.close()
else:
    print("The file does not exist") 



#open and read the file after the appending:
f = open("demofile.txt", "r")
print(f.read())


