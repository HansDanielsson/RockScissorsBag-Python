def play_game(human_name):
    print("Playing the game!")
    print(f"Hello, {human_name}!")
    play_more = True
    while play_more:
        print("Playing a round!")
        play_rsb()
        play_more = input("Do you want to play another round? (y/n) ") == "y"
        
def play_rsb():
  play_one = True
  while play_one:
    human_choice = input("Please choose <r>ock, <s>cissors, or <b>ag: ")
    if (human_choice == "r") or (human_choice == "s") or (human_choice == "b"):
      computer_choice = random_choice()
      print(f"The computer chose {computer_choice}.")
      if human_choice == computer_choice:
        print("It's a draw!")
      else:
        play_one = False
        determine_winner(human_choice, computer_choice)
  
def random_choice():
  import random
  return random.choice(["r", "s", "b"])

def determine_winner(human_choice, computer_choice):
  if ((human_choice == "r") and (computer_choice == "s")) or ((human_choice == "s") and (computer_choice == "b")) or ((human_choice == "b") and (computer_choice == "r")):
    print("You win!")
  else:
    print("The computer wins!")