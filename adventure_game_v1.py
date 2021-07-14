import time
import random


def print_slow(message):
    print(message)
    time.sleep(2)


def valid_input(prompt, options):
    while True:
        option = input(prompt).lower()
        if option in options:
            return option
        print_slow(f"Sorry, the option '{option}' is invalid.\nTry again!")


def intro():
    print_slow("In a small village, cursed by an old and wisdown shaman,")
    print_slow("there's a rumor of a bounty for defeating him and giving")
    print_slow("back the control of the village to the people.")
    print_slow("This shaman is called Arkutir and he's hide in somewhere")
    print_slow("around the village forest.")
    print_slow("He controls the city with spells that make people from")
    print_slow("village very sick and weaker everyday.")
    print_slow("You've heard about an owner of a magic store,")
    print_slow("in the south of the village, who know where the shaman is.")
    print_slow("You know that just with some magic equipments to defeat him.")
    print_slow("You are in the center of the village.")


def get_direction(equipment):
    print_slow("\nWhere would like to go?")
    print_slow("""
               To the forest?
               To the magic store?
               Runaway from the village?\n""")
    response = valid_input("Choices: forest | store | runaway\n", [
                           "forest", "store", "runaway"])
    if "forest" in response:
        go_florest(equipment)
    elif "store" in response:
        go_magicstore(equipment)
    elif "runaway" in response:
        giveup()


def go_florest(equipment):
    print_slow("You are in the forest and theres a dark foggy")
    print_slow("but you can see two red brigth eyes in a direction")
    print_slow("What would you like to do?")
    print_slow("""
               Walk into eye's direction.
               Seat and wait to see what happens?
               Go back to the village.""")
    response = valid_input("Choices: eye | seat | village\n", [
                           "eye", "seat", "village"])
    if "eye" in response:
        print_slow("You start to walk into the eye's direction.")
        go_fight(equipment)
    elif "seat" in response:
        print_slow("You seat and wait about 5 hours and nothing happens.")
        print_slow(
            "And sudenly you see those red away get closer to you")
        print_slow("and you start to listen 'I'm gonna kill",
                   " you!!' coming to you")
        gofight_seat(equipment)
    elif "village" in response:
        print_slow("You go back to the south entrance of the village")
        get_direction(equipment)


def go_magicstore(equipment):
    if "MAGIC SWORD" and "MAGIC SHIELD" in equipment:
        print_slow("What are you doing here? You must be at the forest!")
        print_slow("You already have the maigc items go to the forest!")
        get_direction(equipment)
    print_slow("You arrived at the Ster's Magic Store and")
    print_slow("the owner comes to you and greets you.")
    print_slow("At the entrace of the store you see a banner")
    print_slow("about the bounty on the shaman's head")
    print_slow("You can also see that Mr Ster looks preety bad,")
    print_slow("not health at all and has some wounds")
    print_slow("Mr Ster says: 'I see you are a new face here.")
    print_slow("What are you here for?'\n")
    print_slow("""
               I'm here to accept the hunt of the shamam!
               I'm just having a look at your products.
               """)
    response = valid_input("Choices: accept | products\n",
                           ["accept", "products"])
    if "accept" in response:
        print_slow("Wow finnaly someone to solve our problems here!")
        print_slow(
            "I'll give you a magic sword and shield to fight for us!")
        print_slow("If you kill him, I'll also give you a bounty.")
        equipment.append("MAGIC SWORD")
        equipment.append("MAGIC SHIELD")
        get_direction(equipment)
    elif "products" in response:
        print_slow("Mr Ster says:'Take a look around we don't have much.")
        print_slow("But you shouldn't stay in this village!'")
        print_slow("You don't feel good because of the curse")
        print_slow("so you should take a better decision.")
        get_direction(equipment)


def giveup():
    print_slow("You ran away from the city gave up of this amazing adventure!")


def gofight_seat(equipment):
    if "MAGIC SWORD" and "MAGIC SHIELD" in equipment:
        print_slow("When he notice you he immediately cast some")
        print_slow("powerfull eletric bolt in you direction.")
        print_slow("Your magic shield starts to shine and you feel it's power")
        print_slow("You act fast and reflect the magic to",
                   " him with your shield.")
        print_slow("He gets hit and fallback looking like dead.")
        print_slow("As you get closer to his body your sword starts to shine.")
        print_slow("You hear a voice whispers in your mind")
        print_slow("pierce his hearth so you can release all the souls")
        print_slow("and end all the curses")
        print_slow("You get you sword and stick into his heart")
        print_slow("his body immediately turns into dust")
        print_slow("and a good energy starts to take control of the place.")
        get_bounty()
    else:
        print_slow("When he notice you he immediately cast some")
        print_slow("powerfull eletric bolt in you direction.")
        print_slow("You try to use your shield but it just hits you so hard")
        print_slow("that you are thrown far away get really hurts.")
        print_slow("He comes closer to you cast a spell cursing your soul")
        print_slow("and you start soffer a of pain and starts to die.")
        print_slow(
            "You cant use fight against a shaman without magic equipments.")
        print_slow("You have been defeated by the shaman and you died!")


def go_fight(equipment):
    if "MAGIC SWORD" and "MAGIC SHIELD" in equipment:
        print_slow("You get closer to the eyes and hear a some weird sounds")
        print_slow("you can now see his shape and how scary he looks.")
        print_slow("You notice that he has some",
                   "eletricity aura around his hand.")
        print_slow("When he notice you he immediately cast some")
        print_slow("powerfull eletric bolt in you direction.")
        print_slow("Your magic shield starts to shine",
                   "and you feel it's power")
        print_slow("You act fast and reflect the",
                   "magic to him with your shield.")
        print_slow("He gets hit and fallback looking like dead.")
        print_slow("As you get closer to his body your sword starts to shine.")
        print_slow("You hear a voice whispers in your mind")
        print_slow("pierce his hearth so you can release all the souls")
        print_slow("and end all the curses")
        print_slow("You get you sword and stick into his heart")
        print_slow("his body immediately turns into dust")
        print_slow("and a good energy starts to take control of the place.")
        get_bounty()
    else:
        print_slow("When he notice you he immediately cast some")
        print_slow("powerfull eletric bolt in you direction.")
        print_slow("You try to use your shield but it just hits you so hard")
        print_slow("that you are thrown far away get really hurts.")
        print_slow("He comes closer to you cast a spell cursing your soul")
        print_slow("and you start soffer a of pain and starts to die.")
        print_slow(
            "You cant use fight against a shaman without magic equipments.")
        print_slow("You have been defeated by the shaman and you died!")


def get_bounty():
    print_slow("You just got a bounty for your brave and defeating the shamam")
    print_slow("I'll give you " +
               random.choice(["500", "700", "1000"]) + " gold pieces!")
    celebtration()


def celebtration():
    print_slow("You go back to the village and start to notice")
    print_slow("that everybody is starting to look fine and health.")
    print_slow("You are now a hero in the village, you recieve a big round")
    print_slow("of apluse and an amazing feast to celebrate!")


def play_again():
    return valid_input("Do you want to play again? [y|n]\n", ["y", "n"])


def end_game():
    print_slow(
        "Nice to have you here, come back whenever",
        "you want to play the Adventure game")


def play_game():
    equipment = []
    intro()
    get_direction(equipment)


def game():
    while True:
        play_game()
        if play_again() == "n":
            break
    end_game()


if __name__ == "__main__":
    game()
