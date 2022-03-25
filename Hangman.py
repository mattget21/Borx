import os
'''
Created on Jan 29, 2021

@author: mgetachew21
'''
clearConsole = lambda: os.system('cls' if os.name in ('nt', 'dos') else 'clear')
def Hangman():
    ask = input("Do you want to play a game? (Yes/No): ")
    ask = ask.lower()
    clearConsole()
    while ask == "yes":
        secretWord = input("Player 1, put your secret word here: ")
        numLettersLeft = len(secretWord)
        num_spaces = " _ " * numLettersLeft
        hangman = ""
        counter = 1
        clearConsole()
        numGuessesLeft = numLettersLeft+6
        copy_numLettersLeft = numLettersLeft 
        while numGuessesLeft > 0 and numLettersLeft > 0:
            player_guess = str(input("player 2, guess a letter:" ))
            numGuessesLeft -= 1 
            for i in range(numLettersLeft):
                if secretWord[i] == player_guess:
                    y = num_spaces[0:i]
                    z = num_spaces[i+1:]
                    num_spaces = y + player_guess + z
                    print(num_spaces)
                    numLettersLeft -= 1
                else:
                    if counter == 1:
                        hangman += " O \n"
                        print (hangman)
                        
                    elif counter == 2:
                        hangman += "/"
                        print (hangman)
                        
                    elif counter == 3:
                        hangman += "|"
                        print (hangman)
                        
                    elif counter == 4:
                        hangman += "\ \n"
                        print (hangman)
                        
                    elif counter == 5:
                        hangman += "/"
                        print (hangman)
                        
                    elif counter == 6:
                        hangman += " \ \n"
                        print (hangman)
                        
                    else:
                        hangman = " +---+ \n |   | \n O   | \n/|\  | \n/ \  | \n     | \n======="
                        print (hangman)
                    counter += 1
        if copy_numLettersLeft == 0:
            print("player 2 wins!") 
        elif numGuessesLeft == 0:
            print("You Lose")
        ask = input("Do you want to play again? (Yes/No): ")
    if ask == "no" or ask == "NO" or ask == "No":
        print("You Lose")
Hangman()