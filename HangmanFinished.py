def wrapper():
    import random
    wordList = []
    lettersGuessed = []
    strikes = []
    art =      ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']
    def loadWord():
        #Opens text file of words and splits up all the words, then appends to wordList
            textfile = open('hangman_words.txt', 'r')
            for word in textfile.read().split():
                wordList.append(str(word))
            #closes textfile        
            textfile.close()
            secretWord = random.choice(wordList)
            return secretWord
           
    def whichArt(art,strikes):
        #Prints art depending on strikes
            if len(strikes) >= 1:
                n = len(strikes)
                print art[n]
            
    def isWin(secretWord, letterGuessed):
       #Checks to see if they won
        n = len(secretWord)
        for letter in letterGuessed:
            if letter in secretWord:
                count = secretWord.count(letter)
                n -= count
            if n == 0:
                return True       
    
    def isLose(strikes):
        #checks strikes to see if they lost
        if strikes.count('strike') == 6:
            return True
        
    def getGuessedWord(secretWord, lettersGuessed):
        #prints letters guessed that are correct, in order
        printedWord = ''
        for letter in secretWord:
            if letter in lettersGuessed:
                printedWord += letter + ' '
            else:
                printedWord += '_'
        return printedWord
        


    def letterGuess():
        #Asks for guess, checks if valid input, and then checks if correct or wrong.
        guess =raw_input("Choose a letter to guess. ").lower()
        if guess in lettersGuessed:
            print "You've already used that letter, try a different one."
            letterGuess()
        elif len(guess) != 1:
            print "Sorry, Invalid Input. Enter only one character at a time."
            letterGuess()
        elif guess.isalpha() == False:
            print "Sorry, Invalid Input. Alphabetical letters only."
            letterGuess()
        else:
            if lettersGuessed.count(guess) != 1:
                if guess.isalpha():
                    if guess in secretWord:
                        print "Nice job, you got it correct. "
                        lettersGuessed.append(guess)
                    if guess not in secretWord:
                        print "Sorry, that is incorrect. "
                        lettersGuessed.append(guess)  
                        strikes.append('strike')
                        
        
    def hangman(secretWord,lettersGuessed,strikes,art):
        #prints letters correct and spaces. prints art. prints win/lose screen, then loops all.
        spaces = getGuessedWord(secretWord, lettersGuessed)
        print spaces
        letterGuess()
        print "You've guessed the following letters.",lettersGuessed
        
        whichArt(art, strikes)
        if isLose(strikes) == True:
            print "Game Over"
            print "The word was %s. Try Again?" %secretWord.title()
            wrapper()
        if isWin(secretWord,lettersGuessed) == True:
            print "You Win! Nicejob."
            wrapper()
        hangman(secretWord,lettersGuessed,strikes,art)
        
            
            
    #calls  and hint for letter count.  
    raw_input("Welcome to hangman. Press enter to start playing!")
    secretWord = loadWord()
    getGuessedWord(secretWord, lettersGuessed)
    print "The word contains %s letters." %(len(secretWord))
    hangman(secretWord,lettersGuessed,strikes,art)
wrapper()




    
