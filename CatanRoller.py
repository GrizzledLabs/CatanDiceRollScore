import random

def roller(number, keepers):
    for i in range(number):
        roll.append(random.choice(options))
    print(' '.join(roll), keepers)
    keepers = input('Keeping: ').upper()
    return keepers

def keepset(keepers):
    klen = len(keepers)
    number = 6 - klen
    return number

score = 0
options = ['GOLD', 'ORE', 'LUMBER', 'BRICK', 'SHEEP', 'WHEAT']
print('Catan Dice Game Roller\n\nIt will roll for you and let you choose what to keep. When stating what you keep, use just letters, like lblb, instead of lumber lumber brick brick.\n\nAt the end of each round, it will ask for the score for that round, then total your current score.')
while True:
    print('')
    roll = []
    keepers = ''
    number = 6
    keepers = roller(number, keepers)
    roll = []
    number = keepset(keepers)
    keepers = roller(number, keepers)
    roll = []
    number = keepset(keepers)
    for i in range(number):
        roll.append(random.choice(options))
    print('\nFINAL ROLL: ', ' '.join(roll), ' '.join(list(keepers)))
    score += int(input('score: '))
    print(f'Score: {score}')
