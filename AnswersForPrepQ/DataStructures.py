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