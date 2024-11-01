import random

choices = ['rock', 'paper', 'scissors']

def determine_winner(user_choice, comp_choice):
    if user_choice == comp_choice:
        return "It's a tie!"
    elif (user_choice == 'rock' and comp_choice == 'scissors') or \
         (user_choice == 'scissors' and comp_choice == 'paper') or \
         (user_choice == 'paper' and comp_choice == 'rock'):
        return "You win!"
    else:
        return "You lose!"
    
def play_game():
    user_score = 0
    comp_score = 0
    print("Welcome to Rock-Paper-Scissors!")
    while True:
        print("\nChoose rock, paper, or scissors:")
        user_choice = input("Your choice: ").lower()

        if user_choice not in choices:
            print("Invalid choice! Please choose rock, paper, or scissors.")
            continue
        
        comp_choice = random.choice(choices)
        
        print(f"You chose: {user_choice}")
        print(f"Computer chose: {comp_choice}")

        result = determine_winner(user_choice, comp_choice)
        print(result)

        if result == "You win!":
            user_score += 1
        elif result == "You lose!":
            comp_score += 1
        
        print(f"Score -> You: {user_score}, Computer: {comp_score}")
        
        play_again = input("Do you want to play another round? (yes/no): ").lower()
        if play_again != 'yes':
            break

    print(f"final_Score -> You: {user_score}, Computer: {comp_score}")
    print("Thanks for playing!")

if __name__ == '__main__':
    play_game()
