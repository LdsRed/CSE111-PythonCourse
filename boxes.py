import math 

number_of_items = int(input("Enter the number of items: "))
number_of_items_per_box = int(input("Enter the number of items per box: "))

number_of_boxes = math.ceil(number_of_items / number_of_items_per_box)

print()

print(f"For {number_of_items} items, packing {number_of_items_per_box}"
    f" items in each box, you will need {number_of_boxes} boxes.")
