f = open('BTSoriginal.txt','r',encoding = 'utf-8') 
bts = f.readlines() # читаем файл построчно

word = '' # заглавное слово
definition = '' # значение
defCount = 1 # счётчик значений; по умолчанию равен 1

for line in bts: 
    if line[0:2] == '@A': # определяем нужный тег  
        word = line # если тег встретился, эта строка - заглавное слово 
    elif line[0:2] == '@w': # новый тег
        definition = definition + '\n' + str(defCount) + ')' + line
# если встретился тег "@w", эта строка - значение; "накапливает" толкования
        defCount += 1 # для возможных следующих значений счётчик увеличивается
    elif line == '\n': # пустая строка означает начало следующей статьи
        print('\t\t\t', word, definition)
        definition = '' # обнуляется для "накапливания" толкований в новой статье
        defCount = 1 # счётчик сбрасывается до значения по умолчанию

f.close()       
