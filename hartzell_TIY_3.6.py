# The guests 
guests = ['Heisenburg', 'Homelander', 'Patrick Bateman']

# Accounce the guest who can't make it
print("Unfortunatly, Heisenburg can't make it to the dinner party, therefore John Cena will be taking his place")

# New guest 
guests[0] = 'John Cean'

# Second line of new invitations
the_invintation = [
    f"Dear {guests[0].title()}, you are invited to the utmost luxurious dinner party.",
    f"Dear {guests[1].title()}, you were selected to attend a dinner party.",
    f"Dear {guests[2].title()}, I'm pleased to announce that you are hereby selected to attend the most exclusive dinner party in Fort Wayne.",
]
 # Printing
print(the_invintation)

# Print stating three more spots opened up
print("\nAttention all guests, we have now found a bigger dinner table so therefore more space is avaliable! Think of people you want coming. Maximum is three")

# Guest beginning
guests.insert(0, 'Triple H')

# Guest Middle
middle_list = len(guests) // 2
guests.insert(middle_list, 'Batista')

# End of List
guests.append('Chris Jericho')

# Print updated invitations
print(f"Dear {guests[0].title()}, you are invited to the utmost luxurious dinner party.")
print(f"Dear {guests[1].title()}, you are invited to the utmost luxurious dinner party.")
print(f"Dear {guests[2].title()}, you are invited to the utmost luxurious dinner party.")
print(f"Dear {guests[3].title()}, you are invited to the utmost luxurious dinner party.")
print(f"Dear {guests[4].title()}, you are invited to the utmost luxurious dinner party.")
print(f"Dear {guests[5].title()}, you are invited to the utmost luxurious dinner party.")



