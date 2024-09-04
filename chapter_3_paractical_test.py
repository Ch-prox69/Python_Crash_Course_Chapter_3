# The list and printing list
candy_list = ['Seth = Gummy Bears', 'Trace = Candy Corn', 'Josue = Twix', 'Julian = Sour Patch Kids', 'Yaseen = Snickers']
print("This is our list:",candy_list)

# Printing each item in the list individually
print(candy_list[0].title())
print(candy_list[1].title())
print(candy_list[2].title())
print(candy_list[3].title())
print(candy_list[4].title())

# Sorting the list by name
sortedCandy_list = sorted(candy_list)
print(sortedCandy_list)

# Printing the list and skipping a line
print("\n",candy_list[0].title())
print("\n",candy_list[1].title())
print("\n",candy_list[2].title())
print("\n",candy_list[3].title())
print("\n",candy_list[4].title())

# Adding Mr. McKinstry's Favorite item
candy_list.append('McKinstry = Almond Joy')

# Printing in reverse order
candy_list.reverse()
print(candy_list)

# Finding the Length of the list
print("The length of the candy list is:",len(candy_list))