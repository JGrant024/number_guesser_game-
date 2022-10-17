import level_1
import level_3

print("Ready to For a Game?")
choice = input(
    "Hit '1' for me to choose a number for you to guess, hit '2' to choose a number for me to guess! "
)

if choice.lower() == "1":
    level_1()
elif choice.lower() == "2":
    level_3()
