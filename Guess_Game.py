import random

def generate_random_number(start=1, end=100):
    return random.randint(start, end)

def get_user_guess():
    return int(input("Enter your guess: "))

def provide_feedback(guess, target):
    if guess < target:
        print("Too low! Try again.")
        return False
    elif guess > target:
        print("Too high! Try again.")
        return False
    else:
        print("Congratulations! You've guessed the correct number.")
        return True

def play_guessing_game():
    print("Welcome to the Guessing Game!")
    target_number = generate_random_number()
    attempts = 0
    guessed_correctly = False
    
    while not guessed_correctly:
        try:
            user_guess = get_user_guess()
            attempts += 1
            guessed_correctly = provide_feedback(user_guess, target_number)
        except ValueError:
            print("Invalid input. Please enter a valid integer.")
    
    print(f"You've guessed the number in {attempts} attempts.")

if __name__ == "__main__":
    play_guessing_game()
