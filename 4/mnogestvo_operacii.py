#сегодня мы с вами попробуем выступить в роли детектива
# у нас есть множество людей, которые пользуется машинной марки, которую пользуется убийца
# есть множество людей, которые живут недалеко от мест преступления
# и множество людей, у которых и работа недалеко от мест преступления

#имена обычно значения неуникальные, но предплоложим, это были бы номер соц страховок
shevrole_owner = {'sam', 'edit', 'semen', 'petr'}

work_near = {'konstantin', 'vladislav', 'sam', 'petr', 'edit'}

live_near = {'john', 'vladislav', 'olga', 'mike', 'grant', 'covid', 'bilbo' }
# сначала нам нужно объединить всех, кто живет неподалеку, и работает неподалеку

be_near = work_near | live_near  # объединяем их в один спискок,н но без дубликатов
# потом делаем срез, кто из них владел машиной шевроле
#  для этого нам нужно сделать такую логическую операцию, как пересечение
suspect = be_near & shevrole_owner

print(suspect)


