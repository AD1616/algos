import random

win_no_switch = 0
win_switch = 0

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


def computer():
    # Referencing the global variables so the function can update them
    global win_switch
    global win_no_switch
    # Picking a random number to be the "car"
    car = random.randint(1,3)

    # Randomly picking a number to simulate the "contestant"
    firstChosen = random.randint(1, 3)
    # 50 50 of whether you switch or don't switch
    decision = random.randint(0,1)
    # Checking for a win and updating variables
    # Decision being 0 means no switch; if the original choice was car, this is a win
    if decision == 0:
        if firstChosen == car:
            win_no_switch +=1
    # Decision being 1 means switch
    # User knows one choice is goat, so as long as original choice wasn't car, switching wins
    if decision == 1:
        if firstChosen != car:
            win_switch +=1


def testerChoose():
    choose()


def testerComputer():
    total = 0
    x = int(input("How many samples do you want to test? "))
    y = int(input("How large do you want each sample to be? "))
    for i in range(0, x):
        for i in range(0, y):
            computer()
        print(win_switch, win_no_switch)
        total += win_switch/win_no_switch
    average = total/x
    print("The average ratio of winning with switching to winning without switching was " + str(average))


if __name__ == "__main__":
    testerComputer()