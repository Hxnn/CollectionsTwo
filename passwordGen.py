import random

choice1 = [random.choice('abcdefghijklmnopqrstuvwxyz') for q in range(2)]
choice2 = [random.choice('ABCDEFGHIJKLMNOPQRSTUVWXYZ') for i in range(random.randint(1, 3))]
choice3 = [random.choice('1234567890') for o in range(random.randint(4, 7))]
choice4 = [random.choice('!@#$%^&*()') for y in range(3)]

choice1n2 = choice1 + choice2
random.shuffle(choice1n2)
choiceALL = choice1 + choice2 + choice3 + choice4
random.shuffle(choiceALL)
choiceTotal = choice1n2 + choiceALL
choiceE = 24 - len(choiceTotal)
choiceADD = [random.choice('abcdefghijklmnopqrstuvwxyz') for x in range(choiceE)]
if len(choiceTotal) < 24:
    print(''.join(choiceTotal + choiceADD))
    print('Totale karakters:', len(choiceTotal + choiceADD))
else:
    print(choiceTotal)
