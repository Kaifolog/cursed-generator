import json
import sys
import random

JSON_PATH = "cursed_dict.json"
p = 1 # symbol change probability coefficient

if p>1:
    print("err : p > 1")
    sys.exit(1)

def insert():
    print("Please enter replaceable symbol:")
    replaceable = str(input())
    if len(replaceable)>1:
        print("err: replaceable symbol length > 1")
        return
    # replaceable = replaceable.lower()
    
    print("Please enter replacing symbol:")
    replacing = str(input())
    # if len(replacing)>1: # Im not sure its necessary
    #     print("err: replacing symbol length > 1")
    #     return
    
    print("Checking for pair {0} -> {1}".format(replaceable, replacing))
    
    try:
        with open(JSON_PATH, "r") as read_file:
            substitutions = json.load(read_file)
    except:
        substitutions = {}
    
    if not (replaceable in substitutions): # checking for existing of replaceable symbol array
        substitutions[replaceable] = [replacing]
        print("Thx! {0} -> {1} added.".format(replaceable, replacing))
    else:
        if not replacing in substitutions[replaceable]: # checking for replacing symbol in replaceable array
            substitutions[replaceable].append(replacing)
            print(substitutions[replaceable])
            print("Thx! {0} -> {1} added.".format(replaceable, replacing))
        else:
            print("Awersome! But this substitution is almost there)")

    with open(JSON_PATH, "w+") as write_file:
        json.dump(substitutions, write_file)



def generate():
    print("Enter the phrase:")
    raw_string = str(input()) # .lower()
    revised = ""
    def replace_indicator():
        return random.choices([True, False], weights = [p , 1-p])[0]
        
    try:
        with open(JSON_PATH, "r") as read_file:
            substitutions = json.load(read_file)
            for symbol in raw_string:
                if symbol in substitutions and replace_indicator():
                    revised = revised + random.choices(substitutions[symbol])[0]
                else:
                    revised = revised + symbol
        print(revised)
    except FileNotFoundError:
        print("Sory! Unfortunately {0} is unavailable ;(".format(JSON_PATH))

if __name__ == "__main__":
    print("(1) to insert new substitution\n(2) to generate cursed phrase\n(q) to quit\n")
    while True:
        print("Select menu option: (1) (2) (q)")
        scenario = str(input())
        if scenario == "1":
            insert()
        elif scenario == "2":
            generate()
        elif scenario == "q":
            break