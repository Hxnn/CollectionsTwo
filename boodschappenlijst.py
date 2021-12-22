lijst = {}


def add():
    global lijst
    question = input('Wat wilt u aan de boodschappen lijst toevoegen? ')
    amount = input("Hoeveel {} wilt u? ".format(question))
    more = input('Wilt u nog meer aan uw lijst toevoegen? Y/N ')
    lijst[question] = amount
    if more == 'Y':
        return add()
    elif more == 'N':
        return lijst


print(add())
