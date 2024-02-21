x = "this is a variable"

print("this with send a message")

x = input("this is where you can get the user to type stuff: ")

if x == "this is a variable":
    print("try changing the variable and see the result")
elif x == "something":
    print("this will only happen when both the if is false and the elif is true")
else:
    print("this will happen when both the if and elif are false")

def define():
    print("defining something will shorten code and make things easier by making a section of code one line")
define()

dictionary = {
    "a dictionary":1,
    "assigns a key": "and a value",
    "and act": "as extended variables"
}
print(dictionary["a dictionary"])

while x == "while":
    print("while loops will continue to loop until the condition is false")
    x = input("this is where you can get the user to type stuff: ")

for n in range(6):
    print(n)

list = ["this","is","a","list"]
print(list[0])
list.append(1)
print(list)

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
p1 = Person("John", 36)
print(p1.name)
print(p1.age)

try:
    print(error_maker)
except:
    print("error!")
else:
    print("nothing's wrong")

mytuple = ("apple", "banana", "cherry")
for i in mytuple:
  print(i)

x = "this will output the number of items in a string or list"
print(len(x))

inp = input("this will become a list ")
inp.split()
print(inp)

inp = input("your input will be changed ")
inp = inp.replace(inp[0:],"this has replaced your input")
print(inp)

mylist = ["this", "will", "be", "sorted"]
mylist.sort()
print(mylist)

inp = int(input("Number? "))
if inp == 3:
    print("that is equals to")
elif inp != 5:
    print("that is not equal to")

data = input("input in any data type: ")
print(type(data))