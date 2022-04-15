f = open("sozluk.txt", "r", encoding="cp1254")

sixLetterWords = []

for line in f:
    line = line.strip('\n')
    line = line.replace("ÄŸ", 'ğ').replace("ÅŸ", 'ş').replace("Ä°", 'İ').replace("Ä±", 'ı').replace("Ã¼", 'ü').replace("Ã¶", 'ö').replace("Ã§", 'ç')
    #line = line.upper()
    if len(line) == 6:
        sixLetterWords.append(line)


with open('sozlukAlti.txt', 'w') as out:
    for l in sixLetterWords:
        #l = l.decode('utf8')
        out.write('{}\n'.format(l))
