import sys
from random import randint


def guessing(ans, guess1, start, end):
    try:
        if start <= guess1 <= end:
            if guess1 == ans:
                return 'You won :)'
            else:
                return 'Try again :('
        else:
            return f'Give a number {start}~{end}.'
    except (ValueError, TypeError):
        return f'Give a number {start}~{end}.'


def gamers_help(ans, gue):
    if gue > ans:
        return "Seek number is lower than your answer. Your Welcome :)"
    else:
        return "Seek number is greater than your answer. Your Welcome :)"


if __name__ == '__main__':
    try:
        first = int(sys.argv[1])
        last = int(sys.argv[2])
        attempts = int(sys.argv[3])
    except ValueError:
        print("Arguments need to be integers!! Try Again.")
        quit()
    except IndexError:
        print("Give 3 arguments while starting a program!! Try Again.")
        quit()

    answer = randint(first, last)
    for i in range(attempts):
        try:
            guess = int(input(f"Guess the number between {first}~{last}:  "))
            result = guessing(answer, guess, first, last)
            print(result)
            if result == "You won :)":
                break
            if i == (attempts - 1):
                print('Game Over')
                break
            print(gamers_help(answer, guess))
        except (ValueError, TypeError):
            print(f'Give a number {first}~{last}.')

    

        






