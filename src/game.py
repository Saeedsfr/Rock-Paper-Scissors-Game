import random


def main():
    print("Welcome to Rock, Paper, Scissors!")
    play_game()


def get_user_choice():
    choice = input("Enter rock, paper, or scissors: ").lower()
    while choice not in ['rock', 'paper', 'scissors']:
        choice = input("Invalid choice. Please enter rock, paper, or scissors: ").lower()
    return choice


def get_computer_choice():
    return random.choice(['rock', 'paper', 'scissors'])


def determine_winner(user, computer):
    if user == computer:
        return "It's a tie!"
    elif (user == 'rock' and computer == 'scissors') or \
         (user == 'paper' and computer == 'rock') or \
         (user == 'scissors' and computer == 'paper'):
        return "You win!"
    else:
        return "You lose!"
    

def play_game():
    user_choice = get_user_choice()
    computer_choice = get_computer_choice()
    print(f"You chose: {user_choice}")
    print(f"Computer chose: {computer_choice}")
    result = determine_winner(user_choice, computer_choice)
    print(result)
    print("Thanks for playing!")


if __name__ == "__main__":
    main()


while True:
    replay = input("Do you want to play again? (yes/no): ").lower()
    if replay == 'yes':
        play_game()
    elif replay == 'no':
        print("Goodbye!")
        break
    else:
        print("Invalid input. Please enter yes or no.")