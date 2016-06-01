import re

with open('2.txt', 'r', encoding = 'cp1251') as f: #указать название и кодировку нужного файла. Это тестовый.
    test = f.readlines()
cleaned = open('cleaned.txt', 'w', encoding = 'utf-8')

#все используемые теги TEI
tei_tags = ['superEntry', 'entry', 'form', 'orth', 'stress', 'gramGrp', 'sense', 'def', 'cit', 'pos',
            'gen', 'number', 'case', 'iType', 'per', 'tns', 'mood', 'subc', 'colloc', 'usg', 'quote', 'bibl',
            'author', 'xr', 'etym', 're', 'note', 'lang', 'date', 'mentioned', 'gloss', 'pron', 'lbl', 'q',
            'gram', 'ref', 'quote']
#сюда попадут теги, не принадлежащие TEI
deleted = []
#счетчик
line_n = 0

for line in test:
    line_n+=1
    if line_n%5 == 0:
        print('Cleaning line: ', line_n) #лог
    #достаём имена всех тегов в строке
    tags = re.findall('</?([A-Za-z]+) ?.*?>', line)
    for tag in tags: #для каждого из них проверяем, есть ли он в словаре TEI
        if tag not in tei_tags: #если нет
            full_tags = re.findall('</?'+tag+' ?.*?>', line) #достаём теги полностью с атрибутами
            for full_tag in full_tags:
                line = re.sub(full_tag, '', line) #и убираем их из строки
            deleted.append(tag) #фиксируем удалённые теги
    cleaned.write(line) #записываем чистую строку в файл
print('tags deleted: ', deleted)
cleaned.close()