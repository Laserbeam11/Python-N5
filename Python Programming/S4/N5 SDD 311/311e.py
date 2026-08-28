import random

header = "=" * 68
def word_list():
    #words were chosen by ai
    words = [
    "apple", "beach", "chair", "dance", "earth", "field", "grape", "house", "image", "juice",
    "knife", "lemon", "money", "night", "ocean", "paper", "queen", "river", "smile", "table",
    "uncle", "voice", "water", "young", "zebra", "about", "above", "actor", "acute", "admit",
    "adopt", "adult", "after", "again", "agent", "agree", "ahead", "alarm", "album", "alert",
    "alike", "alive", "allow", "alone", "along", "alter", "among", "anger", "angle", "angry",
    "apart", "apply", "arena", "argue", "arise", "array", "arrow", "aside", "asset", "audio",
    "audit", "avoid", "award", "aware", "awful", "bacon", "badge", "baker", "basic", "basis",
    "basket", "bunch", "cabin", "cable", "camel", "camera", "camp", "candy", "cargo", "carry",
    "carve", "case", "catch", "cause", "cedar", "chain", "chalk", "champ", "chant", "chaos",
    "charm", "chart", "chase", "cheap", "check", "cheek", "cheer", "chef", "chess", "chest",
    "chief", "child", "chili", "chill", "chime", "china", "chips", "chirp", "choir", "choke",
    "chord", "chore", "chunk", "churn", "cigar", "cider", "circus", "cite", "civic", "civil",
    "claim", "clamp", "clank", "claps", "clash", "clasp", "class", "claws", "clean", "clear",
    "cleat", "cleft", "clerk", "click", "cliff", "climb", "cling", "clink", "cloak", "clock",
    "clog", "clone", "close", "cloth", "cloud", "clove", "clown", "cluck", "clump", "clung",
    "coach", "coast", "cobra", "cocoa", "codes", "coils", "coins", "colds", "colic", "colon",
    "colts", "comas", "combo", "combs", "comes", "comet", "comfy", "comic", "comma", "conch",
    "condo", "cones", "conga", "conic", "cooks", "cools", "coops", "copes", "copra", "coral",
    "cords", "cores", "corgi", "corks", "corky", "corns", "corny", "corps", "costs", "couch",
    "cough", "could", "count", "coupe", "court", "cover", "covet", "covey", "cows", "craft"
    ]

    
    return words

def hud():
    global guess_n
    print()
    print(f"\n{header}\n")
    print("welcome to wordley")
    print("definitely not a copy of wordle :) ©newyork times 2026")
    print(f"\n{header}\n")
    print()

def split_word(thisWord):
    lr1 = thisWord[0]
    lr2 = thisWord[1]
    lr3 = thisWord[2]
    lr4 = thisWord[3]
    lr5 = thisWord[4]

    return lr1, lr2, lr3, lr4, lr5

def BYG_SORTER(thisWord, thisGuess):
    global guess_n, guess

    lr1, lr2, lr3, lr4, lr5 = split_word(thisWord)
    
    lg1, lg2, lg3, lg4, lg5 = split_word(thisGuess)
    
    if lr1 == lg1:
        print(f"{lg1}")
    elif lg1 in thisWord:
        print(f"{lg1}?")
    else:
        print("?")

    if lr2 == lg2:
        print(f"{lg2}")
    elif lg2 in thisWord:
        print(f"{lg2}?")
    else:
        print("?")
    
    if lr3 == lg3:
        print(f"{lg3}")
    elif lg3 in thisWord:
        print(f"{lg3}?")
    else:
        print("?")

    if lr4 == lg4:
        print(f"{lg4}")
    elif lg4 in thisWord:
        print(f"{lg4}?")
    else:
        print("?")

    if lr5 == lg5:
        print(f"{lg5}")
    elif lg5 in thisWord:
        print(f"{lg5}?")
    else:
        print("?") 



def wordley(random_word, guess_n):
    guess = ""
    print()
    while guess_n < 6 and guess != random_word:
        guess = input(f"guess {guess_n}: ")
        BYG_SORTER(random_word, guess)
        guess_n += 1
    return guess_n

# main program
random_word = random.choice(word_list())
hud() # 2. display intro text
guess_n = wordley(random_word, 1)


print("END OF THE ROAD")
