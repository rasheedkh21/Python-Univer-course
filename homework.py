# # a=1
# # b=2
# # print(a+b)

# # a= "Python"
# # print(a)

# from random import shuffle, sample

# # List of participant IDs
# participants = list(range(1, 21))

# # Shuffle the participant IDs
# shuffle(participants)

# # Select winners
# chicken_winner = participants[0]
# coffee_winners = sample(participants[1:], 3)

# # Print the winner announcement
# print("---Winner Announcement---")
# print("Chicken winner:", chicken_winner)
# print("Coffee winners:", coffee_winners)
# print("---Congratulations---")
# Calculate average score using "for" statement

#Question 1
scores = [70, 60, 55, 75, 95, 90, 80, 80, 85, 100]
total_score = 0

for score in scores:
    total_score += score

average_score = total_score / len(scores)
print("Average score of class A:", average_score)

#Question 2
import random

# Initialize variables
total_passengers = 0

# Loop to simulate passengers and check conditions
for passenger_number in range(1, 51):
    travel_time = random.randint(5, 50)
    
    if 5 <= travel_time <= 15:
        print(f"[0] Passenger {passenger_number} (time to take: {travel_time} minutes)")
        total_passengers += 1

print("Total passengers:", total_passengers, "teams")

#Question 3
def std_weight(height, gender):
    if gender.lower() == 'man':
        return round(height * height * 22, 2)
    elif gender.lower() == 'woman':
        return round(height * height * 22, 2)
    else:
        return None

# Example usage:
height = 1.75  # in meters
gender = 'man'
result = std_weight(height, gender)
print(f"The standard weight of a {int(height * 100)}cm tall {gender} is {result}kg.")

#Question 4
# Create report files for weeks 1 to 50
for week_number in range(1, 51):
    file_name = f"Week{week_number}.txt"
    
    with open(file_name, 'w') as report_file:
        report_file.write(f"- Weekly reporting for {week_number} weeks -\n")
        report_file.write("Department :\n")
        report_file.write("Name :\n")
        report_file.write("Summary your work :\n")

#Question 5
# Output sentence using variable
station = ["Gwangju airport", "Songjeong", "Geumnam-ro"]
print(f"The train bound for {', '.join(station)} is coming in.")
