# a=1
# b=2
# print(a+b)

# a= "Python"
# print(a)

from random import shuffle, sample

# List of participant IDs
participants = list(range(1, 21))

# Shuffle the participant IDs
shuffle(participants)

# Select winners
chicken_winner = participants[0]
coffee_winners = sample(participants[1:], 3)

# Print the winner announcement
print("---Winner Announcement---")
print("Chicken winner:", chicken_winner)
print("Coffee winners:", coffee_winners)
print("---Congratulations---")