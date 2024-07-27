import random

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == 'rock' and computer_choice == 'scissors') or \
         (user_choice == 'paper' and computer_choice == 'rock') or \
         (user_choice == 'scissors' and computer_choice == 'paper'):
        return "You win!"
    else:
        return "Computer wins!"

def main():
    print("Rock-Paper-Scissors Game")
    choices = ['rock', 'paper', 'scissors']

    while True:
        user_choice = input("Choose rock, paper, or scissors (or 'q' to quit): ").lower()
        
        if user_choice == 'q':
            print("Exiting the game...")
            break
        
        if user_choice not in choices:
            print("Invalid choice. Please choose rock, paper, or scissors.")
            continue

        computer_choice = random.choice(choices)
        print(f"Computer chooses: {computer_choice}")

        result = determine_winner(user_choice, computer_choice)
        print(result)

if __name__ == "__main__":
    main()
