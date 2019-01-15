"""
word guessing Internship Exam
"""
import random
import json
def hangman():
    """ main function"""
    # init var
    guess = 10
    corrected = 0
    display = []
 
    print("Select Category:")
    print("Computer Knowledge", "Big Company", "Famous Person", sep="\n",end="\n\n")

    vocab = open("cat{0}.txt".format(int(input())), "r")
    sq = json.loads(vocab.read())
    wordset = sq[random.randint(0,2)]
    word = wordset[0]
    hint = wordset[1]

    # convert to puzzle
    for i in word:
        if i.isalpha():
            display += ["_"]
        else:
            display += [i]
    scr = 0
    wrong = ""
    wrong_guess = True

    print("\nHint: \"{0}\"".format(hint))
    print("{0}\t score {1}, remaining guess word {2}".format(" ".join(display), scr, guess))
    
    lowercase = word.lower()

    # checking and cmd display
    while guess > 0 and (display.count("_") != 0):
        chr = input().lower()
        if chr.isalpha:
            if not (chr in lowercase):
                guess -= 1 * (not(chr in wrong))
                wrong_guess = False
            else :
                for i in range(len(display)):
                    if chr == lowercase[i]:
                        corrected += 1
                        display = list(display)
                        display[i] = word[i]
                        scr += 15
        print("{0}\t score {1}, remaining guess word {2}".format(" ".join(display), scr, guess), end="")
        if not wrong_guess:
            wrong += (" " + chr) * (not(chr in wrong) and not(chr in lowercase))
            print(", wrong guessed:", wrong, sep="")
        else:
            print()
hangman()
