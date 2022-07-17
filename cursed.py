import json
import sys
import random

JSON_PATH = "cursed_dict.json"
CURSED_LVL = 0.5    # symbol change probability coefficient
ASCII_ONLY = False    # determines whether to use non-ascii characters

if CURSED_LVL > 1:
    print("err : CURSED_LVL > 1")
    sys.exit(1)


def insert():
    print("Please enter replaceable symbol (or sequence):")
    replaceable = str(input())
    # replaceable = replaceable.lower()

    print("Please enter replacing symbol (or sequence appropriate length):")
    replacing = str(input())

    print("Checking for pair {0} -> {1}".format(replaceable, replacing))

    try:
        with open(JSON_PATH, "r+") as read_file:
            substitutions = json.load(read_file)
    except:
        substitutions = {}

    # If there are only one symbol in replaceable -> we are add a replacing sequence as substitution to replaceable.
    # If len(replaceable)>1 and len(replaceable)==len(replacing) -> all pairs of symbols with the same index are substitutions.

    if len(replaceable) == 1 and len(replacing) > 0:
        # checking for existing of replaceable symbol array
        if not (replaceable in substitutions):
            substitutions[replaceable] = [replacing]
            print("Thx! {0} -> {1} added.".format(replaceable, replacing))
        else:
            # checking for replacing symbol in replaceable array
            if not replacing in substitutions[replaceable]:
                substitutions[replaceable].append(replacing)
                print(substitutions[replaceable])
                print("Thx! {0} -> {1} added.".format(replaceable, replacing))
            else:
                print("Awersome! But this substitution is almost there ;)")
    elif len(replaceable) > 1 and len(replaceable) == len(replacing):
        for i in range(len(replaceable)):
           # checking for existing of replaceable symbol array
            if not (replaceable[i] in substitutions):
                substitutions[replaceable[i]] = [replacing[i]]
                print(
                    "Thx! {0} -> {1} added.".format(replaceable[i], replacing[i]))
            else:
                # checking for replacing symbol in replaceable array
                if not replacing[i] in substitutions[replaceable[i]]:
                    substitutions[replaceable[i]].append(replacing[i])
                    print(substitutions[replaceable[i]])
                    print(
                        "Thx! {0} -> {1} added.".format(replaceable[i], replacing[i]))
                else:
                    print("Awersome! But this substitution is almost there ;)")
    else:
        print("\nSomething went wrong!\n")

    with open(JSON_PATH, "w+") as write_file:
        json.dump(substitutions, write_file)


def generate():
    print("Enter the phrase:")
    raw_string = str(input())  # .lower()
    revised = ""

    def replace_indicator():
        return random.choices([True, False], weights=[CURSED_LVL, 1-CURSED_LVL])[0]

    def isascii(character):
        return len(character) == len(character.encode())

    try:
        with open(JSON_PATH, "r") as read_file:
            substitutions = json.load(read_file)
            for symbol in raw_string:
                if symbol in substitutions and replace_indicator():
                    if ASCII_ONLY:  # if in ascii-only mode
                        selected = random.choices(substitutions[symbol])[0]
                        if isascii(selected):
                            revised = revised + selected
                        else:
                            revised = revised + symbol
                    else:
                        revised = revised + \
                            random.choices(substitutions[symbol])[0]
                else:
                    revised = revised + symbol
        print(revised)
    except FileNotFoundError:
        print("Sorry! Unfortunately {0} is unavailable ;(".format(JSON_PATH))


def change_level():
    print("Enter the necessary cursed level:")
    global CURSED_LVL
    try:
        cursed_lvl = float(input())
        if cursed_lvl < 0 or cursed_lvl > 1:
            throw
        CURSED_LVL = cursed_lvl
    except:
        print("Oops! There are some problems with input...")


if __name__ == "__main__":
    print(
        "(1) to add new substitution\n(2) to generate cursed phrase\n(3) to change the level of the curse [0,1]\n(4) to use or not a non-ASCII characters\n(q) to quit\n")
    while True:
        print("Select menu option: (1) (2) (3) (4) (q)")
        print("Now level of the curse is", CURSED_LVL)
        if ASCII_ONLY:
            print("You are currently in ASCII-only mode")
        else:
            print("You are currently NOT in ASCII-only mode")
        scenario = str(input())
        if scenario == "1":
            insert()
        elif scenario == "2":
            generate()
        elif scenario == "3":
            change_level()
        elif scenario == "4":
            ASCII_ONLY = not ASCII_ONLY
        elif scenario == "q" or scenario == "й":
            break
