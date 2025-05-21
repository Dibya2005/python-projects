import random
from hangmanword import word

import random
#dictionary which have a keyb which is a number and a tuple as value

hangman={1:('''
           --------
           |      |
           |      
           |    
           |      
           |     
           -
        '''),2:('''
           --------
           |      |
           |      O
           |    
           |      
           |     
           -
        '''),3:('''
           --------
           |      |
           |      O
           |     \\|
           |      |
           |     
           -
        '''),4:(  '''
           --------
           |      |
           |      O
           |     \\|/
           |      |
           |      
           -
        '''),5:( '''
           --------
           |      |
           |      O
           |     \\|/
           |      |
           |     / 
           -
        '''),6:('''
           --------
           |      |
           |      O
           |     \\|/
           |      |
           |     / \\
           -
        '''),0:(""
        ""
        ""
        ""
        "")}
#function to get a random word from the list
for line in hangman:
    print(hangman[0])
def display(wronguess):
    for line in hangman[wronguess]:
            print(line)

        
            break
    pass
def displayhint(hint):
    print(" ".join(hint)) #join the list with space

    pass
def displayanswer(answer):
    print(" ".join(answer)) #join the list with space
    pass
def main():
    answer=random.choice(word)
    hint=["_"]*len(answer) #list of underscores length of the word
    wrongguess=0
    #we going to track the number of wrong guesses
    guessletter=set() #set of letters guessed empty set is represented like this
    isrunning=True
    while isrunning:
        display(wrongguess)
        displayhint(hint)
        guess=input("guess a letter: ").lower()
        if len(guess)>1 or not guess.alpha():
            #if the length of the guess is greater than 1 or not a letter
            print("invalid input")
            continue
        if guess in guessletter:
            print("you already guessed that letter")
            continue
        guessletter.add(guess)
        if guess in answer:
             for i in range(len(answer)):
                if answer[i]==guess:
                    hint[i]=guess
        else:
            wrongguess+=1
        if "_" not in hint:
                display(wrongguess)
                displayanswer(answer)
                print("you win")
                isrunning=False
        elif wrongguess>=6:
            display(wrongguess)
            displayanswer(answer)
            print("you lose")
            isrunning=False
             
    
if __name__=="__main__":
    main()
# Compare this snippet from sss/sigma/guessnumber.py:

    
