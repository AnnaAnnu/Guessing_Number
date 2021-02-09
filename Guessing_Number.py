number_of_guesses = 1
print(" Number of guesses is limited to 9 times:")

while (number_of_guesses<=9):
    guess_number = int(input("Guess the number:\n"))

    if guess_number<55:
        print("The number is less than the guessing number")
    elif guess_number>55:
        print("The number is greater than the guessing number")

    else:
        print("You Won")
        print(number_of_guesses, "no. of guesses taken to finish the game")
        break
    print(9-number_of_guesses,"No. of guesses left")
    number_of_guesses = number_of_guesses + 1

if (number_of_guesses > 9):
    print("Game Over")
    
        
