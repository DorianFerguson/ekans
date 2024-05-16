import time
import random


def print_pause(message_to_print):
    print(message_to_print)
    time.sleep(2)


def print_pause_2(message_to_print, s):
    print(message_to_print, s)
    time.sleep(2)


def print_pause_3(message_to_print, s, t):
    print(message_to_print, s, t)
    time.sleep(2)


def intro():
    print_pause("You find yourself in a surprisingly familiar setting.")
    print_pause_2("Four gray walls enclosing just enough",
                  "space to hold the basic neccessities.")
    print_pause_2("Lamenting the fact that even computers games",
                  "cannot help you escape your dreary studio apartment")
    print_pause("you suddenly hear the distant sound... of trains?")
    print_pause_2("Upon reaching the window you realize the city",
                  "is completely foreign, although the apartment is same.")
    print_pause_2("GGRRRRREEEERRRRR your stomach bellows,",
                  "informing you of your famished state.")
    print_pause_3("You look at the clock, it's 10:00 p.m.,",
                  "most places are closed and you don't know your",
                  "way around this city.")
    print_pause("To make things worse, you're a vegitarian.\n")


def try_again():
    choice = input("\n Would you like to try again?\n"
                   "1. yes\n"
                   "2. no\n")
    if "1" in choice:
        print_pause("Odd choice ,but it's your call")
        play_game()
    elif "2" in choice:
        print_pause_2("Surprised you made it this far.",
                      "Goodbye!! Thanks for playing!")
    else:
        print_pause("Sorry, I do not understand.")
        try_again()


def play_game():
    items = []
    intro()
    who_cooks(items)


def roid_chicken():
    print_pause_2("WOW, giving up on vegetarianism to end a",
                  "simple game, such weak resolve.")
    print_pause("You ate the chicken, all of it, and exploded.")
    try_again()


def fridge_raid(items):
    print_pause_2("Underwhelmed by the 'creative' idea to play a game",
                  "about getting dinner")
    print_pause("you decide to end it all very quickly.")
    print_pause_3("You open the frigde to find a 4 pound, ",
                  "GMO infested , definitely not pasture",
                  "raised chicken breast.")
    choice = input("Do you want to eat it?\n"
                   "1. yes\n"
                   "2. no\n")
    if "1" in choice:
        roid_chicken()
    elif "2" in choice:
        print_pause("Alright then, so")
        who_cooks(items)
    else:
        print_pause("Please choose '1' or '2'.")
        fridge_raid(items)


def who_cooks(items):
    print_pause("You have two choices:")
    print_pause("1. Eat whatever is in the fridge.")
    print_pause("2. I'm sure there's a restaurant nearby.")
    chef = input("How will you sate your hunger?\n")
    if "1" in chef:
        fridge_raid(items)
    elif "2" in chef:
        print_pause("You franticly run to the elevator.")
        print_pause_2("You exit the elevator on the ground",
                      "floor and head towards the exit.")
        outside_apartment(items)
    else:
        print_pause("Please choose '1' or '2'.")
        who_cooks(items)


def outside_apartment(items):
    print_pause("Once outiside the building you have three choices:")
    print_pause("1. Go down the dark alley")
    print_pause("2. Go down the city block")
    print_pause("3. Go back inside the building")
    path = input("Which path do you choose?\n")
    if "1" in path:
        dark_alley(items)
    elif "2" in path:
        city_block(items)
    elif "3" in path:
        who_cooks(items)
    else:
        print_pause("Please choose 1, 2, or 3.")
        outside_apartment(items)


def dark_alley(items):
    restaurant_name = ['Clean Eatz', 'Veggie Betty', 'Beet Geek']
    print_pause_2("Proceeding down the dark alley,",
                  "you notice something shiny on the ground.")
    if "member card" in items:
        print_pause_2("Ouch! you try to pick it up ,but cut yourself instead.",
                      "It's just a peice of glass.")
        print_pause("You head back to the Apartment building.\n")
        outside_apartment(items)
    else:
        print_pause("You pick up the shiny object.")
        print_pause("A " + random.choice(restaurant_name) + ' member card!')
        print_pause("Nice! now to find the restaurant")
        print_pause_2("Feeling lucky, you head back to the",
                      "Apartment building.\n")
        items.append("member card")
        outside_apartment(items)


def city_block(items):
    print_pause_2("You pass by several concrete cube-like buildings.",
                  "At the end of the block there is a wood cabin.")
    print_pause_2("The cabin has a mural depicting anthropomorphic brussel",
                  " sprouts defeating cows in Mortal Kombat.")
    print_pause_2("This is the restaurant, you walk in",
                  " and go straight to the counter.")
    print_pause_3('"Good evening", says the cashier,',
                  '"before we get started I must inform you of our',
                  'store policy."')
    print_pause_2('"We only serve those who hold a member card.',
                  'It doesn\'t even have to be yours."')
    print_pause('"You just need to have one in your hand."')
    print_pause_2("If you do not have a card,",
                  "you will be kindly asked to leave.")
    print_pause("Do you have a member card?\n")
    response = input("Yes or no\n")
    if "yes" in response.lower():
        if "member card" in items:
            print_pause_2('"Yes, it\'s right here", you say',
                          '"May I have a super green health salad deluxe?"')
            print_pause_2('"Yes, eat up! Thanks for dining with us tonight."',
                          'the cahsier responds')
            print_pause("You eat your meal and go home.")
            print_pause("Congratulations!! You are a WINNER!!")
            try_again()
        else:
            print_pause("Liars do not win in this game.")
            try_again()
    else:
        print_pause('"No" you respond.')
        print_pause_3("The cashier calmly walks to you, transforms",
                      "into an incredible hulk like creature,",
                      "and throws you out the window.")
        print_pause_2("You groggily stumble around, heading towards",
                      "your apartment.")
        print_pause('\"Where can I find a \'member card\'" you wonder.')
        outside_apartment(items)


play_game()
