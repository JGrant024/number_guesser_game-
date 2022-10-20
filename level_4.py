from level_1 import play_computer
from level_3 import play_user

print("Ready to For a Game?")
choice = input(
    "Hit '1' for me to choose a number for you to guess, hit '2' to choose a number for me to guess! "
)

if choice.lower() == "1":
    play_computer()
elif choice.lower() == "2":
    play_user()
