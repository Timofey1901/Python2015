shevrole_owner = {'sam', 'edit', 'semen', 'petr'}
work_near = {'konstantin', 'vladislav', 'sam', 'petr', 'edit'}
live_near = {'john', 'vladislav', 'olga', 'mike', 'grant', 'covid', 'bilbo' }

be_near = work_near | live_near
suspect = be_near & shevrole_owner

print(suspect)


