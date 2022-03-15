import random

CHOICES = ["rock", "paper", "scissors"]

while True:
    print("Make your throw")

    user_choice = input("   Type rock, paper or scissors: ")

    if user_choice in CHOICES:
        computer_choice = random.choice(CHOICES)
        print(f"\nYou threw '{user_choice}, the computer threw '{computer_choice}'.")
    else:
        print(f"\nYou typed '{user_choice}', which isn't a valid throw.")
    
    
    
    if user_choice == computer_choice:
        print(f"Both players selected {user_choice}, It's a tie!")
    elif user_choice == "rock":
        if computer_choice == "scissors":
            print("Rock smashes scissors! You win!")
        else:
            print("Paper covers rock! You lose.")
    elif user_choice == "paper":
        if computer_choice == "rock":
            print("Paper covers rock! You win!")
        else:
            print("Scissors cuts paper! You lose.")
    elif user_choice == "scissors":
        if computer_choice == "paper":
            print("Scissors cuts paper! You win!")
        else:
            print("Rock smashes scissors! You lose.")
           
            
    again = input("\nWant some more? (y/n): ")
    if again.lower() == 'n':
        break
    
    print()          
        
    
print("\nGoodbye")
