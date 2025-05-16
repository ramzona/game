import random
import time

def print_slow(text):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(0.02)
    print()

def get_user_choice():
    while True:
        choice = input("Choose [rock], [paper], [scissors] or [q] to quit: ").lower()
        if choice in ["rock", "paper", "scissors", "q"]:
            return choice
        else:
            print("❌ Invalid input. Try again.")

def decide_winner(player, computer):
    if player == computer:
        return "tie"
    elif (player == "rock" and computer == "scissors") or \
         (player == "paper" and computer == "rock") or \
         (player == "scissors" and computer == "paper"):
        return "player"
    else:
        return "computer"

print("🎮 Welcome to Rock, Paper, Scissors!")
player_score = 0
computer_score = 0
rounds_to_win = 3

while player_score < rounds_to_win and computer_score < rounds_to_win:
    player = get_user_choice()
    if player == "q":
        print("👋 Exiting the game.")
        break

    computer = random.choice(["rock", "paper", "scissors"])
    print_slow(f"🤖 Computer chose: {computer}")
    
    winner = decide_winner(player, computer)
    if winner == "tie":
        print("🤝 It's a tie!")
    elif winner == "player":
        player_score += 1
        print("✅ You win this round!")
    else:
        computer_score += 1
        print("❌ You lose this round.")

    print(f"📊 Score: You {player_score} - {computer_score} Computer\n")

if player_score == rounds_to_win:
    print("🏆 Congratulations! You won the game!")
elif computer_score == rounds_to_win:
    print("💀 The computer won the game. Better luck next time!")
