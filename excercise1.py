f = open("/Users/Anya/Downloads/bts_part.txt", "r", encoding='utf-8')
bts = f.readlines()
astring = ''
wstring = ''
for line in bts:
    line = line.replace("\n", "")
    if line[0:2] == '@A':
        astring = line
    elif line[0:2] == '@w':
        wstring = line
        print(astring + "\t\t\t" + wstring)
