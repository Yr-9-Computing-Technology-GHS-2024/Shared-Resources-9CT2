#Activity 1
import numpy as np
myarray = np.array([21,23,24,21,26,27,19])
avg = np.mean(myarray)
high = np.max(myarray)
low = np.min(myarray)
print(f"""Weather Summary:
      Highest temp was {high}
      Lowest temp was {low}
      Averager temp was {avg}""")
#Activity 2
myarray2 = np.array([[" ","O"," "], ["X"," "," "],[" ","X"," "]])
print(myarray2)
#Activity 3
mylist = ["milk", "bread", "eggs"]
def add_item(list, item):
    try:
        list.append(item)
        print(f"{item} added to list")
        print(list)
    except:
        print(f"Invalid Input")

def remove_item(list, item):
    try:
        list.remove(item)
        print(f"{item} was removed from list")
        print(list)
    except:
        print(f"Invalid Input")

inp = int(input("""Please Choose 1:
1. Add Item
2. Remove Item
3. Quit
"""))
if inp == 1:
    item = input("Please input item: ")
    add_item(mylist, item)
elif inp == 2:
    item = input("Please input item: ")
    remove_item(mylist, item)
elif inp == 3:
    print("Goodbye")
else:
    print("Invalid input")
#Activity 4
class TreeNode:
  def __init__(self, data):
    self.data = data
    self.left = None
    self.right = None

root = TreeNode(50)
NodeA = TreeNode(30)
NodeB = TreeNode(70)
NodeC = TreeNode(20)
NodeD = TreeNode(40)
NodeE = TreeNode(60)
NodeF = TreeNode(80)

root.left = NodeA
root.right = NodeB

NodeA.left = NodeC
NodeA.right = NodeD

NodeB.left = NodeE
NodeB.right = NodeF
print("Binary Tree", root.right.left.data, root.right.right.data)
#Activity 5
stack = []
ans = input()
if ans != "undo" or "quit":
    stack.append(ans)
while ans != "quit":
    ans = input()
    if ans == "undo":
        print("Undone")
        stack.pop()
    elif ans == "stack":
        print(stack)
    else:
        stack.append(ans)
#Activity 6
phonebook = {
    "John Doe": 245263678,
    "Bob Bob": 123456789,
    "Saul Goodman": 911
}

choice = input("Would you like to add, remove, search or sort")
choice = choice.lower()
if choice == "add":
    added = input("Please type the name of the person")
    add = input("Please type their number")
    phonebook[added] = add
elif choice == "remove":
    remove = input("Please type the name of the person")
    try:
        phonebook.pop(remove)
    except:
        print("Invalid choice")
elif choice == "search":
    name = input("Please type the name of the person")
    try:
        x = phonebook.get(name)
        print(x)
    except:
        print("Name not found")
elif choice == "sort":
    y = dict(sorted(phonebook.items()))
    print(y)