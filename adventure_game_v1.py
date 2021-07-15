import time
import random


def print_pause(message, delay=0):
    print(message)
    time.sleep(delay)


# def text_color(message, color, background=False):
#    soc = '\33[48;5;' if background else '\33[38;5;'
#    eoc = '\033[0m'
#    return f"{soc}{color}m{message}{eoc}"


def valid_input(prompt, options):
    while True:
        option = input(prompt).lower()
        if option in options:
            return option
        print_pause(f"Sorry, the option '{option}' is invalid.\n",
                    "Try again!", 1)


def intro():
    print_pause("In a small village, cursed by an old and wisdom shaman,"
                " there's a rumor of a bounty for defeating him and giving"
                " back the control of the village to the people.", 2)
    print_pause("This shaman is called Arkutir and he's hide in somewhere"
                " around the village forest.", 2)
    print_pause("He controls the city with spells that make people from"
                " village very sick and weaker everyday.", 2)
    print_pause("You've heard about an owner of a magic store,"
                " in the south of the village, who know where"
                " the shaman is.", 2)
    print_pause("You know that just with some magic equipments"
                " to defeat him.", 2)
    print_pause("You are in the center of the village.", 1)


def get_direction(equipment):
    print_pause("\nWhere would like to go?", 1)
    print_pause("""
               To the forest?
               To the magic store?
               Runaway from the village?\n""", 1)
    response = valid_input("Choices: forest | store | runaway\n", [
                           "forest", "store", "runaway"])
    if "forest" in response:
        go_florest(equipment)
    elif "store" in response:
        go_magicstore(equipment)
    elif "runaway" in response:
        give_up()


def go_florest(equipment):
    print_pause("You are in the forest and theres a dark foggy"
                " but you can see two red bright eyes in a direction.", 2)
    print_pause("What would you like to do?", 1)
    print_pause("""
               Walk into eye's direction.
               Seat and wait to see what happens?
               Go back to the village.""")
    response = valid_input("Choices: eye | seat | village\n", [
                           "eye", "seat", "village"])
    if "eye" in response:
        print_pause("You start to walk into the eye's direction.", 2)
        go_fight(equipment)
    elif "seat" in response:
        print_pause("You seat and wait about 5 hours and nothing happens.", 2)
        print_pause(
            "And suddenly you see those red away get closer to you and you "
            "start to listen 'I'm gonna kill you!!' coming to you!", 2)
        go_fight_seat(equipment)
    elif "village" in response:
        print_pause("You go back to the south entrance of the village")
        get_direction(equipment)


def go_magicstore(equipment):
    if "MAGIC SWORD" and "MAGIC SHIELD" in equipment:
        print_pause("What are you doing here? You must be at the forest!"
                    "You already have the magic items go to the forest!", 1)
        get_direction(equipment)
    print_pause("You arrived at the Steer's Magic Store and "
                "the owner comes to you and greets you.", 2)
    print_pause("At the entrance of the store you see a banner"
                "about the bounty on the shaman's head.", 2)
    print_pause("You can also see that Mr Ster looks pretty bad,"
                "not health at all and has some wounds.", 2)
    print_pause("Mr. Steer says: 'I see you are a new face here.", 2)
    print_pause("What are you here for?'\n", 1)
    print_pause("""
               I'm here to accept the hunt of the shaman!
               I'm just having a look at your products.
               """)
    response = valid_input("Choices: accept | products\n",
                           ["accept", "products"])
    if "accept" in response:
        print_pause("Wow finally someone to solve our problems here!", 2)
        print_pause(
            "I'll give you a magic sword and shield to fight for us!", 1)
        print_pause("If you kill him, I'll also give you a bounty.", 1)
        equipment.append("MAGIC SWORD")
        equipment.append("MAGIC SHIELD")
        get_direction(equipment)
    elif "products" in response:
        print_pause("Mr Ster says:'Take a look around we don't have much.", 2)
        print_pause("But you shouldn't stay in this village!'", 2)
        print_pause("You don't feel good because of the curse"
                    "so you should take a better decision.", 1)
        get_direction(equipment)


def give_up():
    print_pause("You ran away from the city gave up of this"
                " amazing adventure!", 1)


def go_fight_seat(equipment):
    if "MAGIC SWORD" and "MAGIC SHIELD" in equipment:
        print_pause("When he notice you he immediately cast some"
                    "powerful electric bolt in you direction.", 2)
        print_pause("Your magic shield starts to shine and you"
                    " feel it's power.", 2)
        print_pause("You act fast and reflect the magic to"
                    " him with your shield.", 2)
        print_pause("He gets hit and fallback looking like dead.", 2)
        print_pause("As you get closer to his body your sword"
                    " starts to shine.", 2)
        print_pause("You hear a voice whispers in your mind"
                    " pierce his hearth so you can release all the souls"
                    " and end all the curses", 2)
        print_pause("You get you sword and stick into his heart"
                    " his body immediately turns into dust"
                    " and a good energy starts to take control of the place.", 2)
        get_bounty()
    else:
        print_pause("When he notice you he immediately cast some"
                    "powerful electric bolt in you direction.", 2)
        print_pause("You try to use your shield but it just hits you so hard"
                    " that you are thrown far away get really hurts.", 2)
        print_pause("He comes closer to you cast a spell cursing your soul"
                    " and you start suffer a of pain and starts to die.", 2)
        print_pause(
            "You cant use fight against a shaman without magic equipments.", 1)
        print_pause("You have been defeated by the shaman and you died!", 1)


def go_fight(equipment):
    if "MAGIC SWORD" and "MAGIC SHIELD" in equipment:
        print_pause("You get closer to the eyes and hear a some weird sounds "
                    "you can now see his shape and how scary he looks.", 2)
        print_pause("You notice that he has some "
                    "electricity aura around his hand.", 2)
        print_pause("When he notice you he immediately cast some"
                    "powerful electric bolt in you direction.", 2)
        print_pause("Your magic shield starts to shine"
                    "and you feel it's power", 2)
        print_pause("You act fast and reflect the"
                    "magic to him with your shield.", 2)
        print_pause("He gets hit and fallback looking like dead.")
        print_pause("As you get closer to his body your sword"
                    " starts to shine.", 2)
        print_pause("You hear a voice whispers in your mind "
                    "pierce his hearth so you can release all the souls"
                    " and end all the curses", 2)
        print_pause("You get you sword and stick into his heart"
                    "his body immediately turns into dust"
                    "and a good energy starts to take control of the place.", 2)
        get_bounty()
    else:
        print_pause("When he notice you he immediately cast some"
                    "powerfull eletric bolt in you direction.", 2)
        print_pause("You try to use your shield but it just hits you so hard"
                    "that you are thrown far away get really hurts.", 2)
        print_pause("He comes closer to you cast a spell cursing your soul"
                    "and you start suffer a of pain and starts to die.", 2)
        print_pause(
            "You cant use fight against a shaman without magic equipments.", 1)
        print_pause("You have been defeated by the shaman and you died!", 1)


def get_bounty():
    print_pause("You just got a bounty for your brave and"
                " defeating the shaman!", 1)
    print_pause("I'll give you " +
                random.choice(["500", "700", "1000"]) + " gold pieces!", 1)
    celebration()


def celebration():
    print_pause("You go back to the village and start to notice "
                "that everybody is starting to look fine and health.", 2)
    print_pause("You are now a hero in the village, you receive a big round "
                "of applause and an amazing feast to celebrate!", 2)


def play_again():
    return valid_input("Do you want to play again? [y|n]\n", ["y", "n"])


def end_game():
    print_pause(
        "Nice to have you here, come back whenever"
        "you want to play the Adventure game", 1)


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
