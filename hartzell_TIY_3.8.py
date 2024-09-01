# The Five Locations list
locations = ['Highlands of Scotland', 'Bavaria, Germany', 'Switzerland', 'The Shire, New Zealand', 'Saxony, Germany']

# Printing List: ORIGINAL ORDER
print("THIS IS ORIGINAL ORDER",locations)

# Printing List: ALPHABETICAL ORDER
print("THIS IS APLHABETICVAL ORDER",sorted(locations))

# Printing List: ORIGINAL ORDER AGAIN
print("THIS IS ORIGINAL ORDER",locations)

# Printing List: REVERSE-ALPHABETICAL ORDER
print("THIS IS REVERSE-APLHABETICAVAL",sorted(locations, reverse = True))

# Printing List: ORIGINAL ORDER AGAIN
print("THIS IS ORIGINAL ORDER AGAIN", locations)

# Printing List: REVERSE
locations.reverse()
print("THIS IS REVERSE",locations)

# Printing List: REVERSE AGAIN
locations.reverse()
print("THIS IS REVERSE AGAIN",locations)

# Printing List: ALPHABETICAL ORDER IN SORT
locations.sort()
print("THIS IS ALPHABET USING SORT",locations)

# Printing List: REVERSE-ALFHABETICAL ORDER 
locations.sort(reverse=True)
print("THIS IS REVERSE-ALPHABET USING SORT",locations)
