rage = ("you rage quit the game and never played it again. Ending: Rage quit")
dragon_killer = ("You have beat the game. Ending: Beat the game")
wood = ("You chopped more wood and build a house and just explored the surface. Ending: Timber")
commands = ("You got stuck with the minecraft commands because it was so fun because of the biggest command update. Ending: Commander")
Horrible = ("You just quit the game because the first thing you did was jumping off the mountain. Special ending: Horrible death")
overworld = ("You were able to get resources, but wasn't able to go to the nether because you didn't have strong tools.\nSo you just went up and build a house. Ending: Overworld")
creative_why = ("You just quit the game because you thought creative mode was going to block you from dying. Special ending: Creative death")
cool_house = ("You didn't go to the end, but made a luxurious house by the resource that you gathered. Ending: Luxurious house")
the_strongest_bed = ("You unfortunately didn't know that the bed explodes in the nether or the end. Special ending: Explosive beds")

afk = ("You were slan by monsters because you did nothing until the night come. \nrespawn? \n1.Yes \n2.No")

#################################################3

def start():
    print("Start of the story.")  # Placeholder for story introduction
    print("You just bought minecraft to play with. Now choose an action.")
    start_game()

#######################################################3

def start_game():
    print("You spawned on top of a mountain.")
    print("1. Find a way to go down the mountain safe.")
    print("2. Change into creative mode.")
    print("3. Jump off the mountain.")

    choice = input("Enter 1, 2, or 3: ")
    if choice == "1":
        normal()
    elif choice == "2":
        creative()
    elif choice == "3":
        why()
    else:
        print("Invalid choice. Please try again.")
        start_game()

############################################################

def normal():
    print("You find a safe way and find a way to the plains. What is you next action?")  # Placeholder for outcome 1
    print("1. Chop some wood")
    print("2. Go inside the cave")
    print("3. Do nothing")
    choice = input("Enter 1, 2, or 3: ")

    if choice == "1":
        survive()
    elif choice == "2":
        cave()
    elif choice == "3":
        afk_dead()
    else:
        print("Invalid choice. Please try again.")
        normal()

###############################################################

def survive():
    print("You chopped some wood and got the basic tools. \nChoose your next action")       
    print("1. Chop some more wood")
    print("2. Go inside the cave")
    print("3. Do nothing")
    choice = input("Enter 1, 2, or 3: ")
    
    if choice == "1":
        print(wood)
    elif choice == "2":
        right_way()
    elif choice == "3":
        afk_dead()
    else:
        print("Invalid choice. Please try again.")
        survive()

######################################################################

def right_way():
    print("You are able to defeat the zombies and went deeper.")
    print("1. Mine some ores.")
    print("2. Go even deeper.")
    choice = input("Enter 1 or 2: ")
    if choice == "1":
        nether()
    elif choice == "2":
        print(overworld)
    else:
        print("Invalid choice. Please try again.")
        right_way()

###############################################################################

def nether():
    print("You got stronger tools and went deeper.")
    print("You have found some diamonds and made a nether portal and found a fortress.")
    print("Go inside the fortress? \n1.Yes \n2.No \n3.Place a bed in the nether")
    choice = input("Enter 1, 2 or 3: ")
    if choice == "1":
        go_end()
    elif choice == "2":
        print(cool_house)
    elif choice == "3":
        print(the_strongest_bed)
    else:
        print("Invalid choice. Please try again.")
        nether()
############################################################################

def go_end():
    print("You have got blaze powers and ender pearl and made eye of enders.\nAre you going to the end?")
    print("1.Yes")
    print("2.No")
    choice = input("Enter 1 or 2: ")
    if choice == "1":
        the_end()
    elif choice == "2":
        print(cool_house)
    else:
        print("Invalid choice. Please try again.")
        go_end()

#########################################################################################

def the_end():
    print("You have reached the end. Choose you last action")
    print("1.Go fight the dragon.")
    print("2.Change into creative mode and kill the dragon because you were scared of dying.")
    print("3.Place a bed in the end.")
    choice = input("Enter 1, 2, or 3: ")
    if choice == "1":
        print(dragon_killer)
    elif choice == "2":
        dragon_fight_creative()
    elif choice == "3":
        print(the_strongest_bed)
    else:
        print("Invalid choice. Please try again.")
        the_end()

########################################################################

def cave():
    print("You were attacked by zombies and died because you didn't had any tools. Ending:Monsters\nrespawn? \n1.Yes \n2.No")
    choice = input("Enter 1 or 2: ")
    if choice == "1":
        start_game()
    elif choice == "2":
        print (rage)
    else:
        print("Invalid choice. Please try again.")
        cave()

##############################################################

def afk_dead():
    print (afk)
    choice = input("Enter 1 or 2: ")
    if choice == "1":
        start_game() 
    elif choice == "2":
        print (rage)
    else:
        print("Invalid choice. Please try again.")
        afk_dead()

##################################################
###################################################

def creative():
    print("You changed into creative mode. What are you going to do now?.")
    print("1.Change back to survival mode. \n2.Get portal frame and eye of ender. \n3.Get some command blocks because you are intrested with minecraft commands.")
    choice = input("Enter 1, 2, or 3: ")
    if choice == "1":
        start_game()
    elif choice == "2":
        creative_end()
    elif choice == "3":
        commander()
    else:
        print("Invalid choice. Please try again.")
        creative()

#################################################################################

def creative_end():
    print("You are in the end with creative mode.")
    print("1. Go fight the dragon.")
    print("2. Kill the deagon with a command.")
    print("3. Jump into the void.")
    choice = input("Enter 1, 2, or 3: ")
    if choice == "1":
        dragon_fight_creative()
    elif choice == "2":
        command_kill()
    elif choice == "3":
        creative_dead()
    else:
        print("Invalid choice. Please try again.")
        creative_end()

#########################################################################

def dragon_fight_creative():
    print("You easily killed the ender dragon with creative mode.")
    print(dragon_killer)

################################################################33

def command_kill():
    print("You have killed the ender dragon with just typing some letters. Now you are intrested in minecraft commands.\n Are you going to learn more about commands?")
    print("1. Yes")
    print("2. No")
    choice = input("Enter 1 or 2: ")
    if choice == "1":
        print(commands)
    elif choice == "2":
        print(dragon_killer)
    else:
        print("Invalid choice. Please try again.")
        command_kill()

#########################################################################

def creative_dead():
    print("You literally jump off to the void and died miserably. \nrespawn? \n1.Yes \n2.No")
    choice = input("Enter 1 or 2: ")
    if choice == "1":
        start_game()
    elif choice == "2":
        print (creative_why)
    else:
        print("Invalid choice. Please try again.")
        creative_dead()

#############################################33333333333

def commander():
    print(commands)

###################################################################

def why():
    print("You literally jump off the mountain and died miserably. \nrespawn? \n1.Yes \n2.No")
    choice = input("Enter 1 or 2: ")
    if choice == "1":
        start_game()
    elif choice == "2":
        print (Horrible)
    else:
        print("Invalid choice. Please try again.")
        why()

########################################################################################
start()
