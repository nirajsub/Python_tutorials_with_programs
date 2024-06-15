import random
print("Can you guess a secret number. Let's start the game")
print("Select the range of number you want to play.")

first_range = int(input("Enter the Lower range of number: "))
second_range = int(input("Enter the Upper range of number: "))

sectret_number = random.randint(first_range, second_range)

guess = 0
guessed_numbers = []
turn = 0

print(f"Guess your number between {first_range} and {second_range}.")
while guess != sectret_number:
    guess = int(input("Enter your guess: "))
    guessed_numbers.append(guess)
    if guess < 1 and guess > 100:
        print("Invalid Number. Enter a number between 1 and 100.")
    turn += 1
    if guess == sectret_number:
        print(f"Congratulations! {guess} is the correct number. You have guessed this in {turn} step.")
        print(f"Your guesses were {guessed_numbers}")
    else:
        if guess > sectret_number:
            print(f"Wrong guess! You guessed higher then the actual number. Try a smaller number then this.")
            print(f"Your last guess were {guessed_numbers}")
        else:
            print(f"Wrong guess! You guessed lower then the actual number. Try a higher number then this.")
            print(f"Your last guess were {guessed_numbers}")

# More advance version of number guessing game

def check_number_input(number):
    while True:
        try:
            return int(input(number))
        except ValueError:
            print("Invalid input. Enter a valid number.")

def get_secret_number(lower_range, upper_range):
    return random.randint(lower_range, upper_range)

def play_page(lower_range, upper_range):
    secret_number = get_secret_number(lower_range, upper_range)
    guessed_numbers = []
    guess = 0
    turn = 0
    max_attempt = (upper_range - lower_range) // 2

    print(f"Guess the number between {lower_range} and {upper_range}. You have maximum of {max_attempt} attempts.")

    while turn < max_attempt:
        guess = check_number_input("Guess the number: ")
        if guess < lower_range or guess > upper_range:
            print(f"Invalid guess! Enter a number butween {lower_range} and {upper_range}")
        guessed_numbers.append(guess)
        turn += 1

        if guess == secret_number:
            print(f"Congratulations! {guess} is the correct number. You have guessed this in {turn} step.")
            print(f"Your guessed were: {guessed_numbers}")
            break
        else:

            if guess > secret_number:
                if guess > secret_number + 10:
                    hint = "much higher"
                else:
                    hint = "higher"
            else:
                if guess < secret_number - 10:
                    hint = "much lower"

            print(f"Wrong guess! You guessed {hint} then the actual number.")
            last_guess = guessed_numbers[-2] if len(guessed_numbers) >= 2 else guessed_numbers[-1]
            print(f"Your last guess was: {last_guess}")
    else:
        print(f"Sorry, you've reached the maximum number of attempts. The secret number was {secret_number}. Better luck next time!")

def main():
    print("Start a number Guessing Game!")

    while True:
        lower_range = check_number_input("Enter a lower range of number: ")
        upper_range = check_number_input("Enter a upper range of number: ")

        if lower_range >= upper_range:
            print("Invalid input! Lower range number must be lower than the upper range number. Try again.")
            continue

        play_page(lower_range, upper_range)
        
        play_again = input("Do you want to play again? (Y/N): ").strip().lower()
        if play_again != 'y':
            print("Thank you for playing. Goodbye!")
            break

if __name__ == "__main__":
    main()
