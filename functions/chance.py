import random

def coin_flip():
    return random.choice(["Heads", "Tails"])

def die_roll():
    return random.ranint(1,6)
