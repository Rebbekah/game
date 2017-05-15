#hangman by rebbekah

#import
import random

#lists
WORD3 = ["dog", "cat", "rat", "bat", "zoo", "red", "bed",
         "two", "and", "ant", "rug", "bug", "tug", "hot",
         "sad", "pot", "not", "yes", "car", "age", "ego",
         "hid", "him", "hit", "had", "bad", "hat", "mad",
         "mat", "Sat", "key", "pat", "cue", "sew", "saw",
         "see", "sea", "pod", "ore", "now", "wow", "war",
         "tar", "toe", "tow", "one", "too", "let", "rip",
         "pig", "sip", "fit", "fin", "cow", "web", "end",
         "nod", "own", "bee", "buy", "bye", "ice", "sun",
         "son", "ton", "dad", "mum", "are", "tie", "try",
         "tap", "lab", "lap", "lob", "sob", "lad", "zit",
         "zed", "rim", "zip", "fez", "fat", "vet", "ava",
         "van", "eve", "ivy", "ova", "vow", "rig", "jab",
         "jag", "jam", "jar", "jaw", "jet", "jew", "jib",
         "jig", "dew", "inn", "job","jog", "joy", "jug",
         "tai"]


WORD4 = ["fort", "four", "free", "from", "fuel", "full",
         "fund", "gain", "game", "gate", "gave", "gear",
         "gene", "gift", "girl", "give", "glad", "Goal",
         "Goes", "Gold", "Golf", "Gone", "Good", "Gray",
         "Grew", "Grey", "Grow", "Gulf", "Hair", "Half",
         "Hall", "Hand", "Hang", "Hard", "Harm", "Hate",
         "Have", "Head", "Hear", "Heat", "held", "hell",
         "help", "here", "hero", "high", "hill", "hire",
         "hold", "hole", "holy", "home", "hope", "host",
         "hour", "huge", "hung", "hunt", "hurt", "idea",
         "inch", "into", "iron", "item", "join", "jump",
         "jury", "just", "keen", "keep", "kept", "kick",
         "kill", "kind", "king", "knee", "knew", "know",
         "lack", "lady", "laid", "lake", "land", "lane",
         "last", "late", "lead", "left", "less", "life",
         "lift", "like", "line", "link", "list", "live",
         "load", "loan", "lock", "logo", "long", "look",
         "lord", "lose", "loss", "lost", "love", "luck",
         "made", "mail", "main", "make", "male", "many",
         "mass", "meal", "mean", "meat", "meet", "menu",
         "mile", "milk", "mill", "mind", "mine", "miss",
         "mode", "mood", "moon", "more", "most", "move",
         "much", "must", "name", "navy", "near", "neck",
         "need", "next", "nice", "nine", "none", "nose",
         "note", "okay", "once", "only", "onto", "open",
         "oral", "over", "pace", "pack", "page", "paid",
         "pain", "pair", "palm", "park", "part", "pass",
         "past", "path", "peak", "pick", "pink", "pipe",
         "plan", "play", "plot", "plug", "plus", "Poll",
         "pool", "poor", "port", "post", "pull", "pure",
         "push", "race", "rail", "rain", "rank", "rare",
         "rate", "read", "real", "rear", "rely", "rent",
         "rest", "rice", "rich", "ride", "ring", "rise",
         "risk", "road", "rock", "role", "roll", "roof",
         "room", "root", "rose", "rule", "rush", "safe",
         "said", "sake", "sale", "salt", "same", "sand",
         "save", "seat", "seed", "seek", "seem", "seen",
         "self", "sell", "send", "sent", "Sept", "Ship",
         "Shop", "Shot", "Show", "Shut", "Sick", "Side",
         "Sign", "Site", "Size", "Skin", "Slip", "Slow",
         "Snow", "Soft", "Soil", "Sold", "Sole", "Some",
         "Song", "Soon", "Sort", "Soul", "Spot", "Star"]


incorrect = []
correct = []
hangman_bord = ["hi","z","t"]
word= (" ")
# actions for the buttons
def word_list(wordList):
    word = wordList.pop
    return word  


# cheecking guess
def cheek_guess():
    while True:
        guess = input(" ")
        guess = input().lower# not sure might change
        if guess == incorrect or guess == correct:
            print ("you have already Guessed that")
            return none
        elif guess == int():
            print (" please enter a Letter or a {} letter word".format(len(word)+1))
        elif len(guess) != len(word) or len(guess) > 0:
            print (" please enter either one letter or a {} letter word.".format(len(word)+1))
        elif guess == 0:
            print ("please make a guess")
        break 
    
    if guess in word:
        correct.append(guess)
    else: 
        incorrect.append(guess)
    
    
    
def hangman_board():
    print(hangman_bord(len(incorrect)))
    for i in word :
        if i in word :
            print(i,end=' ')
        else:
            print('_',end=' ')
            
        print ("incorrect words")
        for i in incorrect:
            print(i, end=' ')
    
    
def win_or_lose():
    if len(incorrect) == len(hangman_bord):
        return "loss"
        
while True:
    letters = int(input("choose a number from 3 to 6 for the amount of letters you want in your word."))
    while letters <= 6 or  letters >= 3:
        letters = int(input("choose a number from 3 to 6 for the amount of letters you want in your word."))

    if letters == 3:
        word = word_list(WORD3)
    elif letters == 4:
        word = word_list(WORD4)
    elif letters == 5:
        word = word_list()
    else :
        word = word_list()

        
    while True:
        hangman_board()
        cheek_guess()
        endGame = win_or_lose()
        if endGame == "loss":
            break
