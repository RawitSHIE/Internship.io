"""
Word guessing
"""
import random
import json
def getword():
    """get word"""
    num = selectcat()
    sq = json.loads(open("cat{0}.txt".format(num), "r").read())
    return sq[random.randint(0,4)]

def selectcat():
    """show category"""
    print("Select Category:","1. Computer Knowledge", "2. Big Company", "3. Famous Person", sep="\n",end="\n\n")
    num = input()
    return  num if not num.isalpha() and  0 < int(num) < 4 else selectcat()

def hangman():
    """ main game"""
    # init var
    guess, score = 10, 0
    wrong = ""
    wrong_yet = False
    
    #seting word
    wordset = getword()
    word, hint = wordset[0], wordset[1]

    # convert to puzzle
    con = lambda x : '_' if x.isalpha() else x
    display = [con(i) for i in word]

    # checking and cmd display
    print("\nHint: \"{0}\"".format(hint))
    print("{0}\t score {1}, remaining guess word {2}".format(" ".join(display), score, guess))
    lowercase = word.lower()

    while guess > 0 and (display.count("_") != 0):
        checkchr = lambda tmp : tmp if len(tmp) == 1 and tmp.isalpha() else checkchr(input())
        chr = checkchr(input()).lower()
        if (chr in display or chr in wrong):
            print(chr+" had already been guessed")
            continue
        if not (chr in lowercase):
            guess -= 1
            wrong_yet = True
        else :
            for i in range(len(display)):
                if chr == lowercase[i]:
                    display = list(display)
                    display[i] = word[i]
                    score += 15
        print("{0}\t score {1}, remaining guess word {2}".format(" ".join(display), score, guess), end="")
        if wrong_yet:
            score -= 5
            wrong += (" " + chr) * (not(chr in wrong) and not(chr in lowercase))
            print(", wrong guessed:", wrong, sep="")
        else:
            print()
    if guess > 0 :
        print("You guessed!!!! \n{0}, Score : {1}".format(wordset[0], score))
    else:
        print("You lose \nThe answer is {0}".format(wordset[0]))
hangman()
