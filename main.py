from game import play_game
from information import print_hello

def main():
  print_hello()
  human_name = input("Hello! What's your name? ")
  play_game(human_name)
  print("Thanks for playing!")
  
if __name__ == "__main__":
  main()