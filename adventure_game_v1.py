import time
import random


def print_slow(message):
    print(message)
    time.sleep(2)


def valid_input(prompt, option1, option2, option3):
    while True:
        response = input(prompt).lower()
        if option1 in response:
            break
        elif option2 in response:
            break
        elif option3 in response:
            break
        else:
            print_slow("Sorry, I don't understand")
    return response


def intro():
    print_slow("In a small village, cursed by an old and wisdown shaman")
    print_slow(
        "there's a rumor of a bounty for killing him and giving back the control of the village to the farmers.")
    print_slow(
        "This shaman is called Arkutir, he's hide in somewhere around the village florest.")
    print_slow(
        "He controls the city with spells that make people from village very sick and weaker everyday.")
    print_slow(
        "You've heard about an owner of a magic store, in the south of the village, who know where the shaman is.")
    print_slow(
        "You know that against shamam you just have a fair chance to win the fight with some magic equipments.")
    print_slow("You are in the center of the village.")


def get_direction(equipment):
    response = valid_input("Where would like to go?\n"
                           "To the florest?\nTo the magic store?\n"
                           "Far away from the city?\n", "florest",
                           "magic store", "away")
    if "florest" in response:
        go_florest(equipment)
    elif "magic store" in response:
        go_magicstore(equipment)
    elif "away" in response:
        giveup()


def go_florest(equipment):
    print_slow(
        "You are in the florest and theres a dark foggy but you can see two red brigth eyes in a direction")
    response = valid_input("What would you like to do?\n"
                           "Walk into eye's direction.\n"
                           "Seat and wait to see what happens?\n"
                           "Go back to the village.\n", "eye", "seat", "village")
    if "eye" in response:
        print_slow("You start to walk into the eye's direction.")
        go_fight()
    elif "seat" in response:
        print_slow("You seat and wait for around 5 hours and nothing happens.")
        print_slow(
            "And when you think there's about time to do something different.")
        print_slow("You see that those red eyes start to get closer")
        go_fight()
    elif "village" in response:
        print_slow("You go back to the south entrance of the village")
        get_direction()


def go_fight(equipment):
    print_slow(
        "As far as you get closer to it you start to listen a lot of sounds and star to see his shape")
    if "MAGIC SWORD" and "MAGIC SHIELD" in equipment:
        print_slow("")
        print_slow("")
        print_slow("")
    else:
        # his defeat
        print_slow("")
        print_slow("")
        print_slow("You have been defeated by the shaman and you died!")
        response = valid_input(
            "Would you like to play again? Yes or no\n", "Yes", "No", "Yes")
    if "yes" in response:
        play_game()
    else:
        return False


def go_magicstore(equipment):
    print_slow(
        "You arrived at the Ster's Magic Store and the owner comes to you and greets you.")
    print_slow(
        "At the entrace of the store you see a banner telling about the bounty on the shaman's head")
    print_slow("You can also see that Mr Ster looks preety bad, looks like not health at all and has some wounds on the skin")
    response = valid_input("Mr Ster say: 'I see you are a new face here, what are you here for?\n"
                           "I accept the hunt of the shamam!\n"
                           "I'm just having a look at your products.\n"
                           "Nothing I'm just walking around.\n", "accept", "products", "walk")
    if "accept" in response:
        print_slow("Wow finnaly someone to solve our problems here!\n"
                   "You look like a very strong and smart fighter\n"
                   "I'll give you a magic sword and a shield to fight for us!\n"
                   "After killing him, come here and I'll also give you the bounty")
        magic_equipments = ["MAGIC SWORD", "MAGIC SHIELD"]
        equipment.append(magic_equipments)
        get_direction(equipment)
    elif "products" in response:
        print_slow(
            "Mr Ster says: 'Take a look around we don't have much and you shouldn't be for so long in this village!'")
        print_slow(
            "You really don't feel confortable and should take a better decision")
        get_direction(equipment)
    elif "walk" in response:
        print_slow(
            "Mr Ster says: 'You shouldn't be walking here, go somewhere else!")
        get_direction(equipment)


def giveup():
    print_slow(
        "You ran away from the city and gave up of the fight and the bounty")
    # my valid_input functin requires 3 options but in these one i only have two
    # what can I do to solve it?
    response = valid_input(
        "Would you like to play again? Yes or no\n", "Yes", "No", "Yes")
    if "yes" in response:
        play_game()
    else:
        return False


def play_game():
    equipment = []
    intro()
    get_direction(equipment)


play_game()
