""" This program makes use of the random library and generates a random integer number
    by taking the start an end value from the user. Once the number is generated, it asks 
    the user to guess the number and depending upon the input given by the user it prints
    the desired statments. If the user is able to guess the number correctly, it quits the 
    program otherwise at the end it displays the number generated."""

import random

key = 0
start = int(input("Enter the first number in the range: "))
end = int(input("Enter the second number in the range: "))
num_gen = random.randint(start, end)
print("Number has been generated")
usr_guess = int(input("Enter your guess: "))

if usr_guess > num_gen:
    print("Guess is too high") 
elif usr_guess < num_gen:
    print("Guess is too low")
elif usr_guess == num_gen:
    print("Congratulations, You hit the bull's eye")
    quit()  
else:
    print("Invalid input entered")

key = input("Press 1 to know the number generated: ")

if key == '1':
    print("The random number generated is {}:".format(num_gen))
else:
    print("Wrong key entered")

 

