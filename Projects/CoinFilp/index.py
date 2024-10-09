from random import randint


def flip():

    coin = ["heads", "tails"]

    return coin[randint(0, 1)]


print("\nLet's flip a coin!!! You get:")
print(flip() + "\n")
