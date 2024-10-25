#guessing game
secret=9
guessCount=0
guessLimit=3
while guessCount <guessLimit:
    guess = int(input('guess: '))
    guessCount +=1
    if guess == secret:
        print('you won')
        break
else:
     print('sorry you failed')       
