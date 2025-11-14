activity-cyoa-Yik Man Zhang.py
inventory = []
health = 100

name = input("What is your name, skibidiskibidi? ")
print(f"Welcome, {name}, to the Forest of Whispers.")

print("\nYou come to a fork in the forest path.")
choice1 = input("Do you go LEFT toward the river, or RIGHT into the darker woods? (left/right): ").lower()

if choice1 == "left":
    print("\nYou walk toward the sound of running water and find a peaceful river.")
    print("You notice a shiny object near the bank.")
    choice2 = input("Do you PICK it up or IGNORE it? (pick/ignore): ").lower()

    if choice2 == "pick":
        print("You picked up a glowing STONE. It hums with power.")
        inventory.append("glowing stone")
    else:
        print("You ignore the object and continue walking.")

    print("You follow the river and soon encounter a bridge guarded by a troll.")
    choice3 = input("Do you FIGHT the troll or try to TALK to it? (fight/talk): ").lower()

    if choice3 == "fight":
        if "glowing stone" in inventory:
            print("The stone glows brightly and weakens the troll! You defeat it easily.")
            print("You cross the bridge safely and find a hidden village. You are welcomed as a hero.")
            print("🏆 Ending: Hero of the Riverlands")
        else:
            health -= 50
            if health <= 0:
                print("The troll is too strong. You are defeated.")
                print("💀 Ending: Fallen at the Bridge")
            else:
                print(f"You survive the battle. Health: {health}")
                print("You limp across the bridge but are too weak to go on.")
                print("😢 Ending: Wounded Wanderer")

    elif choice3 == "talk":
        print("The troll is surprisingly friendly and lets you pass after a riddle.")
        print("You cross the bridge and find a peaceful meadow where you rest.")
        print("🌼 Ending: Peaceful Resolution")
    else:
        print("Invalid choice. Lost in indecision, you wander endlessly.")
        print("🌀 Ending: Lost in the Forest")

elif choice1 == "right":
    print("You enter the dark woods. The trees seem to whisper.")
    choice2 = input("You see a torch on the ground. Do you TAKE it or LEAVE it? (take/leave): ").lower()

    if choice2 == "take":
        print("You now have a torch. It lights your way.")
        inventory.append("torch")
    else:
        print("You leave the torch and proceed in darkness.")

    print("You hear growling ahead — a wild beast blocks your path!")
    choice3 = input("Do you RUN or STAND your ground? (run/stand): ").lower()

    if choice3 == "run":
        if "torch" in inventory:
            print("You use the torch to scare off the beast as you flee.")
            print("You escape safely and find your way out of the forest.")
            print("🌟 Ending: Survivor of the Shadows")
        else:
            health -= 60
            if health <= 0:
                print("The beast catches you in the dark.")
                print("💀 Ending: Hunted in the Woods")
            else:
                print(f"You escape but are badly wounded. Health: {health}")
                print("You make it out, barely alive.")
                print("😖 Ending: Scarred but Alive")

    elif choice3 == "stand":
        if "torch" in inventory:
            print("You wave the torch and scare the beast away.")
            print("You continue on and find an ancient ruin filled with treasures.")
            print("💰 Ending: Treasure Hunter")
        else:
            print("You stand your ground, but the beast overpowers you.")
            print("💀 Ending: Brave but Doomed")
    else:
        print("Frozen with fear, you can't decide. The beast takes advantage.")
        print("💀 Ending: Indecisive End")

else:
    print("You hesitate too long at the fork. Night falls, and the forest claims another.")
    print("🌑 Ending: Lost Before the Journey Began")
