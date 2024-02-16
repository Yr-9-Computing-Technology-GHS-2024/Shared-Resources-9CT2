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