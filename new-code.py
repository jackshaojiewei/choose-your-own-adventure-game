import time

def print_slow(text):
    """Prints text slowly for a dramatic effect."""
    for char in text:
        print(char, end='', flush=True)
        time.sleep(0.03)
    print()

def page_1():
    print_slow("You wake up in a dimly lit room. The air is cold, and the walls are covered in strange symbols.")
    print_slow("You see two doors: one red and one blue.")
    print_slow("1. Go through the red door.")
    print_slow("2. Go through the blue door.")
    choice = input("What do you do? (1 or 2): ")
    if choice == "1":
        page_2()
    elif choice == "2":
        page_3()
    else:
        print_slow("Invalid choice. Please try again.")
        page_1()

def page_2():
    print_slow("You open the red door and find yourself in a long, dark hallway.")
    print_slow("At the end of the hallway, you see a faint light.")
    print_slow("1. Walk toward the light.")
    print_slow("2. Turn back and go through the blue door instead.")
    print_slow("3. Investigate the walls for clues.")
    choice = input("What do you do? (1, 2, or 3): ")
    if choice == "1":
        page_4()
    elif choice == "2":
        page_3()
    elif choice == "3":
        page_22()
    else:
        print_slow("Invalid choice. Please try again.")
        page_2()

def page_3():
    print_slow("You open the blue door and step into a lush, green forest.")
    print_slow("The air is fresh, and you hear birds chirping.")
    print_slow("1. Explore the forest.")
    print_slow("2. Go back to the red door.")
    print_slow("3. Climb a tree to get a better view.")
    choice = input("What do you do? (1, 2, or 3): ")
    if choice == "1":
        page_5()
    elif choice == "2":
        page_2()
    elif choice == "3":
        page_23()
    else:
        print_slow("Invalid choice. Please try again.")
        page_3()

def page_4():
    print_slow("As you walk toward the light, you realize it's coming from a flickering lantern.")
    print_slow("Suddenly, the ground beneath you gives way, and you fall into a pit.")
    print_slow("You land in a dark cave, surrounded by glowing mushrooms.")
    print_slow("1. Climb out of the pit.")
    print_slow("2. Explore the cave.")
    print_slow("3. Call for help.")
    choice = input("What do you do? (1, 2, or 3): ")
    if choice == "1":
        page_6()
    elif choice == "2":
        page_7()
    elif choice == "3":
        page_24()
    else:
        print_slow("Invalid choice. Please try again.")
        page_4()

def page_5():
    print_slow("You venture deeper into the forest and come across a small cabin.")
    print_slow("Smoke rises from the chimney, and you hear faint music playing inside.")
    print_slow("1. Knock on the door.")
    print_slow("2. Ignore the cabin and keep exploring.")
    print_slow("3. Peek through the window.")
    choice = input("What do you do? (1, 2, or 3): ")
    if choice == "1":
        page_8()
    elif choice == "2":
        page_9()
    elif choice == "3":
        page_25()
    else:
        print_slow("Invalid choice. Please try again.")
        page_5()

def page_6():
    print_slow("You manage to climb out of the pit and find yourself back in the hallway.")
    print_slow("The red door is gone, replaced by a mirror.")
    print_slow("You see your reflection, but something is off...")
    print_slow("1. Touch the mirror.")
    print_slow("2. Turn back and explore the cave.")
    print_slow("3. Smash the mirror.")
    choice = input("What do you do? (1, 2, or 3): ")
    if choice == "1":
        page_10()
    elif choice == "2":
        page_7()
    elif choice == "3":
        page_26()
    else:
        print_slow("Invalid choice. Please try again.")
        page_6()

def page_7():
    print_slow("You explore the cave and find a hidden passage.")
    print_slow("The passage leads to a treasure chest filled with gold and jewels.")
    print_slow("1. Take the treasure.")
    print_slow("2. Leave the treasure and continue exploring.")
    print_slow("3. Investigate the chest for traps.")
    choice = input("What do you do? (1, 2, or 3): ")
    if choice == "1":
        page_11()
    elif choice == "2":
        page_12()
    elif choice == "3":
        page_27()
    else:
        print_slow("Invalid choice. Please try again.")
        page_7()

def page_8():
    print_slow("You knock on the door, and it creaks open.")
    print_slow("Inside, you see an old woman sitting by the fire.")
    print_slow("She smiles and beckons you to enter.")
    print_slow("1. Enter the cabin.")
    print_slow("2. Back away and leave.")
    print_slow("3. Ask her who she is.")
    choice = input("What do you do? (1, 2, or 3): ")
    if choice == "1":
        page_13()
    elif choice == "2":
        page_9()
    elif choice == "3":
        page_28()
    else:
        print_slow("Invalid choice. Please try again.")
        page_8()

def page_9():
    print_slow("You decide to ignore the cabin and continue exploring the forest.")
    print_slow("As you walk, you stumble upon a hidden path.")
    print_slow("1. Follow the path.")
    print_slow("2. Go back to the cabin.")
    print_slow("3. Rest under a tree.")
    choice = input("What do you do? (1, 2, or 3): ")
    if choice == "1":
        page_14()
    elif choice == "2":
        page_8()
    elif choice == "3":
        page_29()
    else:
        print_slow("Invalid choice. Please try again.")
        page_9()

def page_10():
    print_slow("You touch the mirror, and your reflection reaches out to grab you.")
    print_slow("You are pulled into the mirror and find yourself in an alternate reality.")
    print_slow("The world is twisted and dark, and you hear whispers all around you.")
    print_slow("1. Try to find a way back.")
    print_slow("2. Embrace the darkness.")
    print_slow("3. Scream for help.")
    choice = input("What do you do? (1, 2, or 3): ")
    if choice == "1":
        page_15()
    elif choice == "2":
        page_16()
    elif choice == "3":
        page_30()
    else:
        print_slow("Invalid choice. Please try again.")
        page_10()

def page_11():
    print_slow("You take the treasure, but as soon as you do, the cave begins to collapse.")
    print_slow("You run for the exit, but it's too late. The cave buries you alive.")
    print_slow("GAME OVER.")
    play_again()

def page_12():
    print_slow("You leave the treasure and continue exploring the cave.")
    print_slow("You find a hidden exit that leads you back to the forest.")
    print_slow("You feel a sense of accomplishment, knowing you made the right choice.")
    print_slow("THE END.")
    play_again()

def page_13():
    print_slow("You enter the cabin, and the old woman offers you a cup of tea.")
    print_slow("As you drink, you feel a strange sensation and realize the tea was poisoned.")
    print_slow("You collapse, and everything goes black.")
    print_slow("GAME OVER.")
    play_again()

def page_14():
    print_slow("You follow the hidden path and come across a clearing.")
    print_slow("In the center of the clearing is a portal glowing with light.")
    print_slow("1. Step through the portal.")
    print_slow("2. Turn back and return to the forest.")
    print_slow("3. Examine the portal closely.")
    choice = input("What do you do? (1, 2, or 3): ")
    if choice == "1":
        page_17()
    elif choice == "2":
        page_9()
    elif choice == "3":
        page_31()
    else:
        print_slow("Invalid choice. Please try again.")
        page_14()

def page_15():
    print_slow("You search for a way back and find a glowing portal.")
    print_slow("You step through and find yourself back in the original room.")
    print_slow("The red and blue doors are gone, replaced by a single golden door.")
    print_slow("1. Open the golden door.")
    print_slow("2. Examine the room for clues.")
    choice = input("What do you do? (1 or 2): ")
    if choice == "1":
        page_18()
    elif choice == "2":
        page_32()
    else:
        print_slow("Invalid choice. Please try again.")
        page_15()

def page_16():
    print_slow("You embrace the darkness, and it consumes you.")
    print_slow("You become one with the shadows, forever lost in the alternate reality.")
    print_slow("GAME OVER.")
    play_again()

def page_17():
    print_slow("You step through the portal and find yourself in a peaceful meadow.")
    print_slow("The sun is shining, and you feel a sense of calm.")
    print_slow("You realize you've escaped the strange world and are finally free.")
    print_slow("THE END.")
    play_again()

def page_18():
    print_slow("You open the golden door and step into a bright, white room.")
    print_slow("In the center of the room is a pedestal with a glowing orb.")
    print_slow("You touch the orb, and a voice says, 'You have proven yourself worthy.'")
    print_slow("The orb grants you the power to control time and space.")
    print_slow("You use your new powers to return home, forever changed by your journey.")
    print_slow("THE END.")
    play_again()

# Additional pages for extended gameplay
def page_22():
    print_slow("You investigate the walls and find a hidden lever.")
    print_slow("Pulling the lever opens a secret door.")
    print_slow("1. Enter the secret door.")
    print_slow("2. Ignore it and continue down the hallway.")
    choice = input("What do you do? (1 or 2): ")
    if choice == "1":
        page_33()
    elif choice == "2":
        page_4()
    else:
        print_slow("Invalid choice. Please try again.")
        page_22()

def page_23():
    print_slow("You climb a tree and see a distant tower in the forest.")
    print_slow("1. Head toward the tower.")
    print_slow("2. Climb down and continue exploring.")
    choice = input("What do you do? (1 or 2): ")
    if choice == "1":
        page_34()
    elif choice == "2":
        page_5()
    else:
        print_slow("Invalid choice. Please try again.")
        page_23()

def page_24():
    print_slow("You call for help, and your voice echoes through the cave.")
    print_slow("Suddenly, a group of glowing creatures appears.")
    print_slow("1. Ask them for help.")
    print_slow("2. Hide and observe them.")
    choice = input("What do you do? (1 or 2): ")
    if choice == "1":
        print_slow("The creatures lead you to a hidden exit. You escape the cave!")
        print_slow("THE END.")
        play_again()
    elif choice == "2":
        print_slow("The creatures notice you and surround you. They seem friendly and guide you out.")
        print_slow("THE END.")
        play_again()
    else:
        print_slow("Invalid choice. Please try again.")
        page_24()

def page_25():
    print_slow("You peek through the window and see the old woman chanting over a cauldron.")
    print_slow("1. Knock on the door and confront her.")
    print_slow("2. Sneak away quietly.")
    choice = input("What do you do? (1 or 2): ")
    if choice == "1":
        print_slow("The old woman turns around and smiles. She invites you in and offers you a potion.")
        print_slow("You drink it and gain magical powers!")
        print_slow("THE END.")
        play_again()
    elif choice == "2":
        print_slow("You sneak away but trip over a branch. The old woman hears you and curses you.")
        print_slow("GAME OVER.")
        play_again()
    else:
        print_slow("Invalid choice. Please try again.")
        page_25()

def page_26():
    print_slow("You smash the mirror, and the glass shatters into a thousand pieces.")
    print_slow("The shards swirl around you, forming a portal.")
    print_slow("1. Step through the portal.")
    print_slow("2. Stay where you are.")
    choice = input("What do you do? (1 or 2): ")
    if choice == "1":
        print_slow("The portal takes you to a mysterious island. You begin a new adventure.")
        print_slow("THE END.")
        play_again()
    elif choice == "2":
        print_slow("The portal closes, and you are trapped in the hallway forever.")
        print_slow("GAME OVER.")
        play_again()
    else:
        print_slow("Invalid choice. Please try again.")
        page_26()

def page_27():
    print_slow("You investigate the chest and find a hidden mechanism.")
    print_slow("1. Activate the mechanism.")
    print_slow("2. Leave it alone.")
    choice = input("What do you do? (1 or 2): ")
    if choice == "1":
        print_slow("The mechanism opens a secret passage. You find a map to a hidden treasure!")
        print_slow("THE END.")
        play_again()
    elif choice == "2":
        print_slow("You leave the chest and continue exploring, but the cave collapses behind you.")
        print_slow("GAME OVER.")
        play_again()
    else:
        print_slow("Invalid choice. Please try again.")
        page_27()

def page_28():
    print_slow("You ask the old woman who she is, and she reveals herself as a powerful sorceress.")
    print_slow("1. Ask her to teach you magic.")
    print_slow("2. Politely decline and leave.")
    choice = input("What do you do? (1 or 2): ")
    if choice == "1":
        print_slow("She agrees and trains you in the magical arts. You become a powerful wizard!")
        print_slow("THE END.")
        play_again()
    elif choice == "2":
        print_slow("You leave the cabin, but the forest seems darker and more dangerous.")
        print_slow("GAME OVER.")
        play_again()
    else:
        print_slow("Invalid choice. Please try again.")
        page_28()

def page_29():
    print_slow("You rest under a tree and fall asleep.")
    print_slow("When you wake up, you find yourself back in the original room.")
    print_slow("1. Go through the red door.")
    print_slow("2. Go through the blue door.")
    choice = input("What do you do? (1 or 2): ")
    if choice == "1":
        page_2()
    elif choice == "2":
        page_3()
    else:
        print_slow("Invalid choice. Please try again.")
        page_29()

def page_30():
    print_slow("You scream for help, and your voice echoes through the void.")
    print_slow("A shadowy figure appears and offers to guide you out.")
    print_slow("1. Accept their help.")
    print_slow("2. Refuse and try to find your own way.")
    choice = input("What do you do? (1 or 2): ")
    if choice == "1":
        print_slow("The figure leads you to a portal. You step through and find yourself back in the forest.")
        print_slow("THE END.")
        play_again()
    elif choice == "2":
        print_slow("You wander the void forever, lost and alone.")
        print_slow("GAME OVER.")
        play_again()
    else:
        print_slow("Invalid choice. Please try again.")
        page_30()

def page_31():
    print_slow("You examine the portal closely and notice strange symbols.")
    print_slow("1. Touch the symbols.")
    print_slow("2. Step through the portal.")
    choice = input("What do you do? (1 or 2): ")
    if choice == "1":
        print_slow("The symbols glow brightly, and you are transported to a futuristic city.")
        print_slow("THE END.")
        play_again()
    elif choice == "2":
        page_17()
    else:
        print_slow("Invalid choice. Please try again.")
        page_31()

def page_32():
    print_slow("You examine the room and find a hidden compartment in the wall.")
    print_slow("Inside is a key with a strange symbol.")
    print_slow("1. Use the key on the golden door.")
    print_slow("2. Keep the key and look for another exit.")
    choice = input("What do you do? (1 or 2): ")
    if choice == "1":
        print_slow("The key unlocks the door, revealing a portal to your home.")
        print_slow("THE END.")
        play_again()
    elif choice == "2":
        print_slow("You search for another exit but find nothing. The room begins to collapse.")
        print_slow("GAME OVER.")
        play_again()
    else:
        print_slow("Invalid choice. Please try again.")
        page_32()

def page_33():
    print_slow("You enter the secret door and find yourself in a library filled with ancient books.")
    print_slow("1. Search for a book on escaping.")
    print_slow("2. Leave the library and return to the hallway.")
    choice = input("What do you do? (1 or 2): ")
    if choice == "1":
        print_slow("You find a book that teaches you how to open a portal. You escape!")
        print_slow("THE END.")
        play_again()
    elif choice == "2":
        page_2()
    else:
        print_slow("Invalid choice. Please try again.")
        page_33()

def page_34():
    print_slow("You head toward the tower and find it guarded by a fierce dragon.")
    print_slow("1. Try to sneak past the dragon.")
    print_slow("2. Challenge the dragon to a battle.")
    choice = input("What do you do? (1 or 2): ")
    if choice == "1":
        print_slow("You successfully sneak past the dragon and find a treasure inside the tower.")
        print_slow("THE END.")
        play_again()
    elif choice == "2":
        print_slow("The dragon defeats you in battle. You are no more.")
        print_slow("GAME OVER.")
        play_again()
    else:
        print_slow("Invalid choice. Please try again.")
        page_34()

def play_again():
    choice = input("Would you like to play again? (yes or no): ").lower()
    if choice == "yes":
        page_1()
    else:
        print_slow("Thanks for playing!")

# Start the game
print_slow("Welcome to 'Choose Your Own Adventure: The Mysterious Room'!")
page_1()
