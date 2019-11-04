# Guessing a number game. The computer randomly picks a number
# and the user has to guess it in 6 tries.

import random  # Imports the random module to allow use of methods from it.

guesses_taken = 0  # Assigns 0 to the guesses_taken variable, for use
                   # in the while loop.

print('Hello! What is your name?')  # Displays the text on the screen.
myName = input()  # Initializes the myName variable and waits for user input.

number = random.randint(1, 20)  # Initializes the number variable, with the
                                # random randint method from the random module.
                                # The range will go to 19 though.
print('Well, ' + myName + ', I am thinking of a number between 1 and 20.')
        # Concatenates the strings and myName variable (also a string) and
        # displays it on the screen.

while guesses_taken < 6:  # Main loop, guesses_taken from 0 to 5 (6 times).
    print('Take a guess.')  # Displays the string on the screen.
    guess = input()  # Initializes the guess variable and waits for user input
    guess = int(guess)  # Converts the value of guess to int, as input is str

    guesses_taken += 1  # Increments the guesses_taken variable by 1 to move
                        # forward in the loop

    if guess < number:  # If statement that compares the values of the 2
                        # variables to determine if the user input guess was
                        # lower than the number value
        print('Your guess is too low.')  # Displays the string on the screen

    if guess > number:  # If statement that compares the values of the 2
                        # variables to determine if the user input guess was
                        # higher than the number value
        print('Your guess is too high.')  # Displays the string on the screen

    if guess == number:  # If statement that compares the values of the 2
                         # variables to determine if the user input guess was
                         # equal to the number value
        break  # As a result of the True value of the previous statement,
               # it stops the while loop and the execution can proceed to the
               # next part of the program

if guess == number:  # If statement that compares the values of the 2
                     # variables to determine if the user input guess was
                     # equal to the number value
    guesses_taken = str(guesses_taken)  # Converts the value of guesses_taken
                                        # to str, as it was previously an int
    print('Good job, ' + myName + '! You guessed my number in ' + guesses_taken + ' guesses!')
                    # Concatenates the strings and variable values and then
                    # displays them on the screen.
if guess != number:  # If statement that compares the values of the 2
                     # variables to determine if the user input guess was
                     # not equal to the number value
    number = str(number)  # Converts the value of guesses_taken
                          # to str, as it was previously an int
    print('Nope. The number I was thinking of was ' + number)
                    # Concatenates the strings and variable values and then
                    # displays them on the screen.
