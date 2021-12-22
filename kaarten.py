import random


def kaarten():
    harten = ['Harten 2', 'Harten 3', 'Harten 4', 'Harten 5', 'Harten 6', 'Harten 7', 'Harten 8', 'Harten 9',
              'Harten 10', 'Harten Boer', 'Harten Vrouw', 'Harten Heer', 'Harten Aas']
    schoppen = ['Schoppen 2', 'Schoppen 3', 'Schoppen 4', 'Schoppen 5', 'Schoppen 6', 'Schoppen 7', 'Schoppen 8',
                'Schoppen 9', 'Schoppen 10', 'Schoppen Boer', 'Schoppen Vrouw', 'Schoppen Heer', 'Schoppen Aas']
    klaver = ['Klaver 2', 'Klaver 3', 'Klaver 4', 'Klaver 5', 'Klaver 6', 'Klaver 7', 'Klaver 8', 'Klaver 9',
              'Klaver 10', 'Klaver Boer', 'Klaver Vrouw', 'Klaver Heer', 'Klaver Aas']
    ruiten = ['Ruiten 2', 'Ruiten 3', 'Ruiten 4', 'Ruiten 5', 'Ruiten 6', 'Ruiten 7', 'Ruiten 8', 'Ruiten 9',
              'Ruiten 10', 'Ruiten Boer', 'Ruiten Vrouw', 'Ruiten Heer', 'Ruiten Aas']
    joker = ['Joker', 'Joker']
    cards = harten + schoppen + klaver + ruiten + joker
    num = 0
    random.shuffle(cards)
    for i in range(7):
        hand = [cards.pop(random.randint(0, 5))]
        num += 1
        print('kaart', num, ':', hand)
    print('deck [47 kaarten] ', cards)


kaarten()
