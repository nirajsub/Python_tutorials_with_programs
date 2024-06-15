import random
print("Can you guess a secret number. Let's start the game")
print("Select the range of number you want to play.")

first_range = int(input("Enter the Lower range of number: "))
second_range = int(input("Enter the Upper range of number: "))

sectretnumber = random.randint(first_range, second_range)

guess = 0
guessed_numbers = []
turn = 0

while guess != sectretnumber:
    print("Guess Your Number between 1 and 100.")
    guess = int(input("Enter your guess: "))
    guessed_numbers.append(guess)
    if guess < 1 and guess > 100:
        print("Invalid Number. Enter a number between 1 and 100.")
    turn = turn + 1
    if guess == sectretnumber:
        print(f"Congratulations! {guess} is the correct number. You have guessed this in {turn} step.")
    else:
        if guess > sectretnumber:
            print(f"Wrong guess! You guessed higher then the actual number. Try a smaller number then this.")
            print(f"Your last guess was {guessed_numbers[-1]}")
        else:
            print(f"Wrong guess! You guessed lower then the actual number. Try a higher number then this.")
            print(f"Your last guess was {guessed_numbers[-1]}")

