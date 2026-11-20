import random
# Rock Paper Scissors Game
# Steps
    ## Take the input from the user
    ## Assign a random choice to computer
    ## Compare the user input and computer choice and declare the winner

# Rules
    ## Rock beats Scissors
    ## Scissors beats Paper
    ## Paper beats Rock

def userInput():
    userChoice = input("Enter your choice: Rock, Paper, Scissors: ").lower();
    if userChoice not in ["rock", "paper", "scissors"]:
        print("Invalid choice. Please choose Rock, Paper, or Scissors.")
        return userInput()
    return userChoice;

def gameLogic(userChoice, computerChoice):
    if userChoice == computerChoice:
        print("It's a tie!")
    elif (userChoice == "rock" and computerChoice == "scissors") or \
         (userChoice == "paper" and computerChoice == "rock") or \
         (userChoice == "scissors" and computerChoice == "paper"):
        print("You win!")
    else:
        print("Computer wins!")

def main():
    while True:
        computerChoice = random.choice(["rock", "paper", "scissors"])
        input = userInput();
        print(f"You chose: {input}")
        print(f"Computer chose: {computerChoice}")
        gameLogic(input, computerChoice);

main();