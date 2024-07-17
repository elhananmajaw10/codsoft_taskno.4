import random

def get_computer_choice():
    return random.choice(['rock', 'paper', 'scissors'])

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == 'rock' and computer_choice == 'scissors') or \
         (user_choice == 'scissors' and computer_choice == 'paper') or \
         (user_choice == 'paper' and computer_choice == 'rock'):
        return "You win!"
    else:
        return "You lose!"

def main():
    user_score = 0
    computer_score = 0

    print("Welcome to Rock, Paper, Scissors!")

    while True:
        user_choice = input("Enter your choice (rock, paper, or scissors): ").lower()
        while user_choice not in ['rock', 'paper', 'scissors']:
            print("Invalid choice. Please try again.")
            user_choice = input("Enter your choice (rock, paper, or scissors): ").lower()

        computer_choice = get_computer_choice()
        result = determine_winner(user_choice, computer_choice)
        
        print(f"\nYou chose: {user_choice}")
        print(f"Computer chose: {computer_choice}")
        print(result)

        if result == "You win!":
            user_score += 1
        elif result == "You lose!":
            computer_score += 1

        print(f"\nScore: You {user_score} - Computer {computer_score}")

        play_again = input("Do you want to play again? (yes or no): ").lower()
        if play_again != 'yes':
            break

    print("Thanks for playing! Goodbye!")

if __name__ == "__main__":
    main()
