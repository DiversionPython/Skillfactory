#Приветствие
def greeting():
    print('--------Приветствую в игре--------', \
                  '--------Крестики и Нолики---------', \
                  sep = '\n')
greeting()
#Правила
def rules ():
    r = input("Если хотите узнать правила введите 'да', если нет нажмите 'Ввод': ")
    r = r.lower()
    if r == 'да' or r == 'yes':
        print('--------------------------------------------------------',
          'Игроки по очереди ставят на свободные клетки поля 3×3 знаки ',
          'путем указания координат по номеру строки и столбца',
          '(один всегда крестики, другой всегда нолики). ',
          'Первый, выстроивший в ряд 3 своих фигуры ',
          'по вертикали, горизонтали или диагонали, выигрывает. ',
          'Первый ход делает игрок, ставящий крестики.',
          '------------------------------------------------------------', sep='\n')
    else:
        return False

rules()

#Вывод игрового поля
field = [['-']*3 for _ in range(3)]
def game_field(f):
    print ('  0 1 2')
    for i in range (len(field)):
        print(str(i), *field[i])

#Проверка ввода юзера
def users_input(f):
    while True:
        place=input(f"Поставьте '{user}' путем указания двух координат через пробел:\n ").split()
        if len(place)!=2:
            print('Введите 2 координаты')
            continue
        if not(place[0].isdigit() and place [1].isdigit()):
            print('Координаты вводятся цифрами в диапозоне от 0 до 2')
            continue
        x,y=map(int, place)
        if not(x>=0 and x<3 and y>=0 and y<3):
            print('Вы вышли из диапозона')
            continue
        if f[x][y]!='-':
            print('Клетка занята')
            continue
        break
    return x,y

#Проверка выйгрыша
def win(f, user):
    def check(a1,a2,a3,user):
        if a1==user and a2==user and a3==user:
            return True
    for n in range(3):
        if check(f[n][0],f[n][1],f[n][2], user) \
        or check(f[0][n],f[1][n],f[2][n], user) \
        or check(f[0][0],f[1][1],f[2][2], user) \
        or check(f[2][0],f[1][1],f[0][2], user):
            return True
    return False

#Ввод координат
field = [['-']*3 for i in range(3)]
count = 0
while True:
    if count==9:
        print('Ничья')
        break
    if count%2==0:
        user='X'
    else:
        user='0'
    game_field(field)
    x,y=users_input(field)
    field[x][y]=user
    if win(field, user):
        print(f'Выйграл {user}!!!')
        game_field(field)
        break
    count+=1





