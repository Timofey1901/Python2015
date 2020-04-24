print("Приветствую в игре Транслатион! "
      "Введите слова и их переводы, а я "
      "проведу тестирование по этим словам!")

dictionary = {}

# Цикл для заполнения словаря
while True:
    key = input("Введите слово на английском или stop: ").title()
    if key == "Stop":
        break
    value = input("Введите его перевод или stop: ").title()
    if value == "Stop":
        break
    dictionary[key] = value

print("")

scores = 0
error = 0

for key, value in dictionary.items():
    translation = input("Введи перевод слова " + key + ": ").title()
    if translation == value:
        scores += 1
print(scores)

"""
Подсчёт ошибок
+Дружелюбие
Перемешать элементы словаря random.shuffle()
Проигрыш при условии 3 ошибок+
Перевести все вводные строки к нижнему регистру
Удалить пробелы в вводных строках
"""