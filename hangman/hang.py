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

def guessformat(chr):
    """gussing format"""
    if chr.isalpha() and len(chr) == 1:
        return chr.lower()
    print("Input one alphabet character only", end=" : ")
    return guessformat(input())
    
def hangman():
    """ main game"""
    # init var
    guess, score = 10, 0
    wrong_yet, wrong = False, ""
    
    #setting word and score
    wordset = getword()
    word, hint, full = wordset[0], wordset[1], len([i for i in wordset[0] if i.isalpha()])*15
    print()

    # convert to puzzle
    con = lambda x : '_' if x.isalpha() else x
    display = [con(i) for i in word]

    # checking and cmd display
    print("\nHint: \"{0}\"".format(hint))
    print("{0}\t score {1}/{2}, remaining guess word {3}".format(" ".join(display), score, full, guess))
    lowercase = word.lower()

    # guessing
    while guess > 0 and (display.count("_") != 0):
        chr = guessformat(input())
        if (chr in display or chr.upper() in display or chr in wrong):
            print(chr+" had already been guessed", end=" : ")
            continue
        if not (chr in lowercase):
            guess -= 1
            wrong_yet = True
            score -= 5
        else :
            for i in range(len(display)):
                if chr == lowercase[i]:
                    display = list(display)
                    display[i] = word[i]
                    score += 15
        print("{0}\t score {1}/{2}, remaining guess word {3}".format(" ".join(display), score, full, guess), end="")
        
        if wrong_yet:
            wrong += (" " + chr) * (not(chr in wrong) and not(chr in lowercase))
            print(", wrong guessed:", wrong, sep="")
        else:
            print()
    # endgame
    if guess > 0 :
        print("You guessed!!!! \n{0}, Score : {1}/{2}".format(wordset[0], score, full))
    else:
        print("You lose \nThe answer is {0}, Score : {1}/{2}".format(wordset[0], score, full))
    
def main():
    """ main function """
    hangman()
    while True:
        print("Continue playing? Y = Yes/N = No:", end=" ")
        option = input().lower()
        if option == 'y':
            hangman()
        elif option == 'n':
            break
        else:
            continue
    print("Thanks for playing.")
main()