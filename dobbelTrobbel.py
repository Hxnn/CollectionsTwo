import random
from random import choice

print('Welcome to the rolling dice game!')
RedM2 = -2
BlueM2 = -2
RedD = [1, 2, 3, 4, 5, 6]
BlueD = [1, 2, 3, 4, 5, 6]
WhiteD = [1, 1, 1, 2, 2, 3]
ScoreR = [RedM2, '', '', '', '', '', '', '', '', '']
ScoreB = ['', '', '', '', '', '', '', '', '', BlueM2]
ScoreW = ['', '', '', '', '']
Repeat = 0
Round = 0
ScoreR1 = ''
ScoreB1 = ''
ScoreW1 = ''

for x in ScoreR:
    ScoreR1 += '[' + str(x) + ']'
for y in ScoreB:
    ScoreB1 += '[' + str(y) + ']'
for z in ScoreW:
    ScoreW1 += '[' + str(z) + ']'


def error():
    print("This isn't an available option. Please try again: ")
