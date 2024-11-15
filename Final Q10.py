#Christopher Kenny
#CS 175
#Final Exam Q10
#Create a program to track the stock of items in a store and updates the inventory when items are sold.


inventory = {
    "apple": 10,
    "banana": 5,
    "orange": 8,
    "grape": 1
}
sold_items = ["apple", "banana", "grape", "apple", "orange", "banana"]

for item in sold_items:
  if item in inventory:
    inventory[item] -= 1

print(inventory)
