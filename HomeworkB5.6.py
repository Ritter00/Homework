print('Добро пожаловать, в игру "крестики-нолики"')
player_name1 =input('Введите имя первого игрока: ')
player_name2 =input('Введите имя второга игрока: ')
size_field =3 #int(input('Введите размер поля для игры(число): '))
print(player_name1,'(ходит "крестиками" - Х),',player_name2,'(ходит "ноликами" - O)')
print(
    '''Правила игры следующие:
    Введитете номер строки и номер столбца,той клетки, котрую
    вы хотите занять. На этом месте появиться символ "Х" или "О",
    в зависимости от того, кто ходит первым.
    Если вы ввели неправильные координаты - вам будет предложено
    сделать свой ход повторно.
    Победа будет присужена игроку, который первым займет все клетки
    по горизонтали или вертикали или диагонали.
    Если никто не выполнит условия для победы, то будет обьявлена ничья.
    '''
)

field = [['-' for i in range(size_field + 1)]for j in range(size_field + 1)]
for i in range(0,len(field[0])):
    field[0][i] = i
for i in range(0, len(field)):
    field[i][0] = i
field[0][0] = ' '

def print_field(f):
    print('____' * (size_field+1))
    for i in f:
        for j in i:
            print('| {: ^2}'.format(j), end='')
        print('|')
    print('____' * (size_field+1))


def play():
    while True:
        coord = input(f'введите номер строки и стобца, через пробел: ').split()

        if len(coord) != 2:
            print('Ведите 2 координаты')
            continue
        a, b = coord
        if not(a.isdigit()) or not(b.isdigit()):
            print('Введите числа!')
            continue
        a, b = int(a), int(b)
        if a not in range(size_field+1) or b not in range(size_field+1):
            print('Координаты выходят за рамки поля')
            continue
        if field[a][b] != '-':
            print('Клетка занята')
            continue
        return a, b

def check():
    win = (((1, 1),(1, 2),(1, 3)), ((2, 1),(2, 2),(2, 3)),((3, 1),(3, 2),(3, 3)),
           ((1, 1),(2, 1),(3, 1)),((1, 2),(2, 2),(3, 2)), ((1, 3),(2, 3),(3, 3)),
           ((1, 1),(2, 2),(3, 3)), ((1, 3),(2, 3),(3, 1))
           )
    for s in win:
        S = []
        for i in s:
            S.append(field[i[0]][i[1]])
        if S == ['X', 'X', 'X']:
            print(f'{player_name1} выиграл')
            print('Game over')
            return True
        if S == ['O', 'O', 'O']:
            print(f'{player_name2} выиграл')
            print('Game over')
            return True
    return False


count = 0
while True:
    count += 1
    print_field(field)
    if count % 2 == 1:
        print(f'{player_name1} ходит "X"')
    else :
        print(f'{player_name2} ходит "O"')

    a , b = play()

    if count % 2 == 1:
        field[a][b] = 'X'
    else:
        field[a][b] = 'O'

    if check():
        break

    if count == 9:
        print('Ничья')
        print('Game over')
        break