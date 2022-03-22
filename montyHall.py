import random


def choose():
    options = [1, 2, 3]
    car = random.randint(1, 3)
    try:
        print("Pick 1, 2, or 3")
        firstChosen = int(input("Which option would you like to choose?"))
        for x in options:
            if x == firstChosen:
                options.remove(x)
    except:
        print("Pick either 1, 2, or 3")

    for x in options:
        if x == car:
            options.remove(x)

    print(str(options[0]) + " is a goat. Do you want to pick " + str(firstChosen) + " or switch your choice?")

    try:
        secondChosen = int(input("Pick an option"))
    except:
        print("Pick either 1, 2, or 3")

    if secondChosen == car:
        print("You win a car!")
    else:
        print("goat")


def tester():
    choose()


if __name__ == "__main__":
    tester()