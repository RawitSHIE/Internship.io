"""
word guessingg
"""
def hangman():
    # int var
    guess = 10
    corrected = 0
    display = []
    word = list("1- project51")
    for i in word:
        if i.isalpha():
            display += ["_"]
        else:
            display += [i]
    scr = 0
    wrong = ""
    flag = True
    print("hint : \"{0}\"".format("hint"))
    print("{0}\t score {1}, remaining guess word {2}".format(" ".join(display), scr, guess))
    
    # checking and cmd display
    while guess > 0 and (display.count("_") != 0):
        chr = input().lower()
        if chr.isalpha:
            if not (chr in word):
                guess -= 1 * (not(chr in wrong))
                flag = False
            else :
                for i in range(len(display)):
                    if chr == word[i]:
                        corrected += 1
                        display = list(display)
                        display[i] = chr
                        scr += 15
        print("{0}\t score {1}, remaining guess word {2}".format(" ".join(display), scr, guess), end="")
        if not flag:
            wrong += (" " + chr) * (not(chr in wrong) and not(chr in word))
            print(", wrong guessed:", wrong, sep="")
        else:
            print()

hangman()
