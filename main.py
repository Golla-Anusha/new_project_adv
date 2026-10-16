def start_adventure():
    print("you are starting at the edge of a forest.")
    print("There are two paths ahead to you: 'left' or 'right'.")

choice = input("which path could you choose?").lower().strip()

if choice == "left":
    print("\n you walk down the left path and find a chest full of gold!")
    print("congratulations, you win!")

elif choice == "right":
    print("\n you walk down the right path and run directly into a sleeping lion!")
    print("you quickly tiptoe back safety. Game over!")

else:
    print("\n  that wasn't an optio. you stand there frozon and nothing happens.")
    
print("hello is adventure is good")