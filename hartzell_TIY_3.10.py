# List about my favorite Ice Cream
icecream = ['mint', 'rocky road', 'vanilla', 'superman', 'coffee']

# Printing: NORMAL
print(icecream)

# Printing: INDEX
print("\nMy favorite icecream, in lowercase, is...", icecream[0])

# Lets print line 8, but in uppercase
print("\nMy favorite icecream, capitalized, is...", icecream[0].title())

# Alright, now lets print my most favored weird flaovors using index again and lets make sure to capitalize them using title again
print("\nMy most favorite weird flavors are...", icecream[3].title(),"and", icecream[4].title())

# Wow I'm having a hard time what my last favorite flavor was, lets use the index negative one, -1, to see what my last favorite flavor is
print("\nMy last favorite flavor is...", icecream[-1].title())

# Alright, now I need to use the f-string to create a message based on a value from my Icecream list
message = f"\nHey, I'd like you to know that the absolute OG of icecream flavors is {icecream[2].title()}."
print(message)

# Alrigtgt, now lets add an element to the list by using append
icecream.append('chocolate')
print("\nThe new flavor which is at the end of the list is...",icecream)

# Ok, Vanilla is kind of old, lets use the insert method to insert cocolate to vinallas position
icecream.insert(2, 'chocolate')
print("\nThe flavor that will replace vanilla is...",icecream)

# WHAT, now I have chocolate on in my list two times! Lets get rid of the last character in the list using the del statment
del icecream[6]
print("\nAlright, there should now be only only one chocolate",icecream)

# Alright, now lets remove the last flavor and use the pop method to use it for a specific message
popped_icecream = icecream.pop()
print(icecream)
print("\nThis is our popped value...",popped_icecream)

# Lets write a messege to see what the last flavor is now that we updated out list
last_flavor = icecream.pop()
print(f"\nThe my last flavor of Icecream was {last_flavor.title()}.")

# Alright, lets use the pop method with includiong the index
first_flavor = icecream.pop(0)
print(f"\nMy favorite flavor is... {first_flavor.title()}.")
icecream.insert(2, 'mint')
print("\nre-adding the popped value from above",icecream)

# Lets remove an item by value
icecream.remove('vanilla')
print("\nYou can now see vanilla is removed",icecream)
icecream.insert(3, 'vanilla')
print("\nRe-added Vanilla",icecream)

# Now lets remove vanilla, but provide a reason for doing so
boring_flavor = 'vanilla'
icecream.remove(boring_flavor)
print(icecream)
print(f"\nThe flavor {boring_flavor.title()} is removed because it's too boring now.")
icecream.insert(3, 'vanilla')
print("\nRe-added vanilla",icecream)

# Alright lets sort the list using the sort method
icecream.sort()
print("\nThe list should now be sorted...",icecream)

# Alright, lets sort the list in reverse alphgabetical just because :)
icecream.sort(reverse=True)
print("\nNow our list is in reverse",icecream)
icecream.sort()
print("\nLet's turn this back to it's original form :)",icecream)

# Alright, now its time to use sorted instead of sorted
print("\nHere is the original list of icecream:")
print(icecream)

print("\nThis is the sorted list:")
print(sorted(icecream))

print("\nHere is the original list again:")
print(icecream)


# Lets print the list in reverse
print("\nOur original list",icecream)
icecream.reverse()
print("\nOur list in reverse",icecream)

# Wow, that's a lot of code!!!! Let's see what the final length of our ice creame list is
print("The length of our final list is...",len(icecream))

# Wow, that took forever, but I'm glad I pushed through it, now it's time to do it two more times for the two lists below



# LIST TWO




# List of possible careers
possible_careers = ['System Administrator', 'Network Administrator', 'Information Technology Department Manager', 'Ethical Hacker', 'Director of Information Technology']

# Printing: NORMAL
print("\nInitial list of careers:", possible_careers)

# Printing: INDEX
print("\nMy desired career, in lowercase, is...", possible_careers[0].lower())

# Printing first career, but in uppercase
print("\nMy desired career, capitalized, is...", possible_careers[0].title())

# Most favored weird careers
print("\nMy most favorite weird careers are...", possible_careers[3].title(), "and", possible_careers[4].title())

# Last favorite career using negative index
print("\nMy last favorite career is...", possible_careers[-1].title())

# Using f-string for a message
message = f"\nHey, I'd like you to know that the absolute OG of careers is {possible_careers[2].title()}."
print(message)

# Adding an element to the list
possible_careers.append('Database Administrator')
print("\nThe new career which is at the end of the list is...", possible_careers)






# LIST THREE







# List of favorite movies
fav_movies = ['Lord of the Rings', 'Braveheart', 'Quest for the Holy Grail', 'Excalibur']

# Printing: NORMAL
print("\nInitial list of movies:", fav_movies)

# Printing: INDEX
print("\nMy favorite movie, in lowercase, is...", fav_movies[0].lower())

# Printing first movie, but in uppercase
print("\nMy favorite movie, capitalized, is...", fav_movies[0].title())

# Most favored weird movies
print("\nMy most favorite weird movies are...", fav_movies[2].title(), "and", fav_movies[3].title())

# Last favorite movie using negative index
print("\nMy last favorite movie is...", fav_movies[-1].title())

# Using f-string for a message
message = f"\nHey, I'd like you to know that the absolute OG of movies is {fav_movies[1].title()}."
print(message)

# Adding an element to the list
fav_movies.append('Inception')
print("\nThe new movie which is at the end of the list is...", fav_movies)



# THE TWO LISTS HAVE BEEN MANIPULATED, BUT NOT IN GREAT DEPTH LIKE THE FIRST LIST. I CUT THE SECOND AND THIRD LISTS INHALF TO MEET THE THREE LIST REQUIREMENTS WHILE ALSO STILL MANIPULATIONG THEM, BUT NOT TO THE FULL EXTENT AS SHOWN IN LIST ONE!




