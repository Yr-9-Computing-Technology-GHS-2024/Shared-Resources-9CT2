#Open a file
f = open("demofile.txt")

#Read a file
f = open("demofile.txt", "r")
print(f.read())

#Read parts of a file
print(f.read(10))

#Read lines of a file
print(f.readline())
print(f.readline())

#Write to an existing file
f = open("demofile2.txt", "a")
f.write("Now the file has more content!")
f.close()

#Overwrite the original content
f = open("demofile3.txt", "w")
f.write("Woops! I have deleted the content!")
f.close()

#Create a file
f = open("myfile.txt", "x")

#Create a new file if it doesn't exist
f = open("myfile.txt", "w")