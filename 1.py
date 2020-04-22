import random
number = random.randint(1, 100)
name = input('Как тебя зовут? ')
print ('Привет, ' + name.title() + ', ' + 'давай сыграем в игру? Ответь "Да" или "Нет"')
No = ('Нет')
Yes = ('Да')
Game = str(input('Ответ: '))
if Game == No:
    print('Жаль, возвращайся когда будет настроение :(')
if Game == Yes:
    print('Поехали! '
           'Угадай число от 1 до 100, которое я загадал, но сначала, выбери уровень сложности: '
           'легкий, средний или сложный')
else:
    print('Не разобрал ответ, попробуй еще раз')
level = input('Выбрать уровень: ')
hard = ('сложный')
medium = ('средний')
easy = ('легкий')
if level == hard:
    print('Отлично, у вас 6 попыток')
    for i in range(6):
        a = int(input())
        if a > number:
            print('Слишком много')
        if a < number:
            print('Слишком мало')
        if a == number:
            print('Победа! Поздравляю!')
            break
if level == medium:
    print('Олично, у вас 9 попыток')
    for i in range(9):
        a = int(input())
        if a > number:
            print('Слишком много')
        if a < number:
            print('Слишком мало')
        if a == number:
            print('Победа! Поздравляю!')
if level == easy:
    print('Отлично, у вас 12 попыток')
    for i in range(12):
        a = int(input())
        if a > number:
            print('Слишком много')
        if a < number:
            print('Слишком мало')
        if a == number:
         print('Победа! Поздравляю!')
else:
 print('Попытки закончились, к сожалению ты проиграл, попробуй еще раз')

 print("Привет, Мир!")