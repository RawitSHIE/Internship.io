"""
word guessingg
"""
import random
def hangman():

    # int var
    guess = 10
    corrected = 0
    display = []
 
    print("Select Category:")
    print("Computer Knowledge", "Big Company", "Famous Person", sep="\n",end="\n\n")

    vocab =	[
        [["End System", "Part of Edge Network"], ["Random Access memory" ,  "A Volatile Memory"], ["Mainboard", "Main Curcuit of Computer"]],
        [["Google" ,  "A search engine"], ["Facebook", "Social Media Platform"], ["Youtube",  "Video Streaming Platform"]],
        [["Donald Trump" ,  "I'm gonna build a wall."], ["Drake", "You used to call me on my cell phone~~~"], ["Tom Hanks",  "Mama always said life was like a box of chocolates."]]
    ]

    wordset = vocab[int(input()) - 1][random.randint(0,2)]
    word = wordset[0]
    hint = wordset[1]

    for i in word:
        if i.isalpha():
            display += ["_"]
        else:
            display += [i]
    scr = 0
    wrong = ""
    flag = True

    print("\nHint: \"{0}\"".format(hint))
    print("{0}\t score {1}, remaining guess word {2}".format(" ".join(display), scr, guess))
    
    lowercase = word.lower()

    # checking and cmd display
    while guess > 0 and (display.count("_") != 0):
        chr = input().lower()
        if chr.isalpha:
            if not (chr in lowercase):
                guess -= 1 * (not(chr in wrong))
                flag = False
            else :
                for i in range(len(display)):
                    if chr == lowercase[i]:
                        corrected += 1
                        display = list(display)
                        display[i] = word[i]
                        scr += 15
        print("{0}\t score {1}, remaining guess word {2}".format(" ".join(display), scr, guess), end="")
        if not flag:
            wrong += (" " + chr) * (not(chr in wrong) and not(chr in lowercase))
            print(", wrong guessed:", wrong, sep="")
        else:
            print()
        
hangman()
