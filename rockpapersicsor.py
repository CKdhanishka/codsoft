import random

def display_instructions():
    print("🎮 Welcome to the Rock-Paper-Scissors Game!")
    print("Instructions:")
    print("- Type 'rock', 'paper', or 'scissors' to play.")
    print("- Rock beats Scissors, Scissors beats Paper, Paper beats Rock.")
    print("- Try to beat the computer! 💻")
    print("- Type 'exit' at any time to quit the game.")

def get_user_choice():
    choice = input("\nYour choice (rock/paper/scissors): ").lower()
    if choice in ['rock', 'paper', 'scissors']:
        return choice
    elif choice == 'exit':
        return 'exit'
    else:
        print("Invalid input. Please enter rock, paper, or scissors.")
        return get_user_choice()

def get_computer_choice():
    return random.choice(['rock', 'paper', 'scissors'])

def determine_winner(user, computer):
    if user == computer:
        return 'tie'
    elif (user == 'rock' and computer == 'scissors') or \
         (user == 'scissors' and computer == 'paper') or \
         (user == 'paper' and computer == 'rock'):
        return 'user'
    else:
        return 'computer'

def display_result(user, computer, winner):
    print(f"\n🧑 You chose:     {user}")
    print(f"💻 Computer chose: {computer}")
    
    if winner == 'tie':
        print("🔁 It's a tie!")
    elif winner == 'user':
        print("✅ You win this round!")
    else:
        print("❌ Computer wins this round!")

def play_game():
    user_score = 0
    computer_score = 0
    round_number = 1

    display_instructions()

    while True:
        print(f"\n===== Round {round_number} =====")
        user_choice = get_user_choice()
        if user_choice == 'exit':
            break
        computer_choice = get_computer_choice()
        winner = determine_winner(user_choice, computer_choice)
        
        display_result(user_choice, computer_choice, winner)

        if winner == 'user':
            user_score += 1
        elif winner == 'computer':
            computer_score += 1

        print(f"📊 Score => You: {user_score} | Computer: {computer_score}")

        play_again = input("\nDo you want to play another round? (yes/no): ").lower()
        if play_again not in ['yes', 'y']:
            break
        round_number += 1

    print("\n🏁 Game Over! Final Score:")
    print(f"👤 You: {user_score} | 💻 Computer: {computer_score}")
    print("Thanks for playing! 👋")

if __name__ == "__main__":
    play_game()