from json import load
from random import randint, choice
from time import time 

# Function to read JSON file
def json_reader(filename):
    with open(filename) as file:
        f = load(file)
        return f

# Welcome function
def welcome_part():
    start = time()
    print('*****__Welcome! Now, you are playing MATH TIMED game!__*****')
    rules = input('Do you know rules (Yes/No): ').lower()
    end = time()
    if end - start >= 5:
        print('The game is stopped because of time limit!')
        return False
    if rules == 'no':
        input('Press enter to read rules')
        r = json_reader('info3.json')
        print(r['rules'])
    return True

# Function to get player information
def players():
    players = int(input('How many players will play the game? (1 or 2): '))
    if players == 1:
        player = input('Enter player\'s name: ')
        return 1, player
    elif players == 2:
        pl_1 = input('Enter N1 player\'s name: ')
        pl_2 = input('Enter N2 player\'s name: ')
        return 2, pl_1, pl_2

# Function to generate easy math problems
def easy_maker():
    min_op = json_reader('info3.json')['min_op']
    max_op = json_reader('info3.json')['max_op']
    operators = json_reader('info3.json')['operators']
    
    left = randint(min_op, max_op)
    right = randint(min_op, max_op)
    operator = choice(operators)
    expr = f"{left} {operator} {right}"
    answer = eval(expr)
    return expr, answer

# Function to check the guess
def check_guess(answer, problem_number, expr, player_name, score):
    while True:
        guess = input(f"{player_name}, Problem #{problem_number}: {expr} = ")
        if guess == 'stop':
            print('You stopped the game')
            return False
        if guess == str(answer):
            score["right answers"] += 1
            return True
        else:
            score["wrong answers"] += 1
            print("Incorrect. Try again.")

# Easy mode function
def easy(player_name, score):
    for i in range(10):
        expr, answer = easy_maker()
        if not check_guess(answer, i + 1, expr, player_name, score):
            return False
    print(f"Great job, {player_name}, you completed all problems!")
    return True

# Medium mode function
def medium(player_name, score):
    problems = json_reader('info3.json')['med_problems']
    for i in range(10):
        expr = choice(problems)
        answer = eval(expr)
        if not check_guess(answer, i + 1, expr, player_name, score):
            return False
    print(f"Great job, {player_name}, you completed all problems!")
    return True

# Hard mode function
def hard(player_name, score):
    problems = json_reader('info3.json')['hard_problems']
    for i in range(10):
        expr = choice(problems)
        answer = eval(expr)
        if not check_guess(answer, i + 1, expr, player_name, score):
            return False
    print(f"Great job, {player_name}, you completed all problems!")
    return True

# Function to choose the complication level
def complication(player_name, score):
    input('Press enter to start')
    comp = input('Enter complication (e)asy/(m)edium/(h)ard: ').lower()
    if comp == 'e':
        return easy(player_name, score)
    elif comp == 'm':
        return medium(player_name, score)
    elif comp == 'h':
        return hard(player_name, score)