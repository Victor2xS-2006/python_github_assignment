#this is a welcome message
print("Welcome to my Python program!")

#question asked to the user where they are supposed to input a numerical value
hours = input("About how many hours did you spend doing school work today?")

try:
    #makes the number able to be multiplied
    hours = float(hours)

    #this will multiply their answer by 7
    weekly_hours = hours * 7

    #shows how many hours a user is on track to do school work in a week in a sentence
    print(f"You are on track to spend {weekly_hours} hours doing school work this week.")
except ValueError:
    #makes a message pop up telling the user they did not input a numerical value and
    #that they need to input a number
    print("Please enter a valid number.")
    exit()