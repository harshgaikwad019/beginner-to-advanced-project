name = input("hey type your name: ")
print("hello", name,"welcome to my game!")

should_we_play = input("do you want to play? ").lower()
 

if should_we_play == "yes":
    print("we are gonna play!")

    direction = input("do you want to go left or right? (left/right)").lower()
    if direction == "left":
        print("you went left and fell of a cliff, game over, try again. ")
    elif direction == "right":
        choice = input("okay now see a bridge, do you want to swim under or cross it? (swim/cross) ")
        if choice == "swim":
            print("you got eaten by an alligator you die , the end")
        else:
            print("you found the gold and won! ")

    else:
        print("sorry you not take any direction you die! ")
else:
    print(" ok we are not playing.....")
