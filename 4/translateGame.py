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

