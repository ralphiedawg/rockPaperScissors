import time
import random
playingTheGame = False
name = input("What's your name? ")
time.sleep(.8)
wouldYouLikeToPlayAGame = input(f'Would you like to play a game, {name}?: ')
match wouldYouLikeToPlayAGame:
    case 'y':
        userChoice = input('What is your Pick?: r - rock, p - paper, s - scissors : ')
        botChoice = random.randint(1,3)
        match userChoice:
            case 'r':
                if botChoice == 1:
                    print('Tie, run the program again.')
                if botChoice == 2:
                    print('I won.')
                if botChoice == 3:
                    print('You win.')
            case 'p':
                if botChoice == 2:
                    print('Tie, run the program again.')
                if botChoice == 3:
                    print('I won.')
                if botChoice == 1:
                    print('You win.')
            case 's':
                if botChoice == 3:
                    print('Tie, run the program again.')
                if botChoice == 1:
                    print('I won.')
                if botChoice == 2:
                    print('You win.')
            case _:
                print("Wasn't an option idiot")
    case 'n':
        print('that sucks')
    case _:
        print("That wasn't an option, rerun the program.")