#The Range Riddle

#Task 1: Every Other Day Write a program that prints each day of the week, but only if that day is on an even index.

days_of_week = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]

for index in range(len(days_of_week)):
    if index % 2 == 0:
        print("the day of the month that is even is:", days_of_week[index])


#  2. Loop Condition Logic
#  Task 1: Loop Condition Exploration Write a while loop with a condition that will never be true (an infinite loop). Ask the user a question until their answer triggers a break statement (hint: use an if statement to evaluate their answer).


while False:
    pass

while not False:

    answer = input("What is my name?")
    if answer == "vincent":
        print("You are correct")
        break
    else:
        print("That's not correct.Try again.")

        # I do not understand how to use the randomness with loops 
