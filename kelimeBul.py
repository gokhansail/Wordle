f = open("sozlukAlti.txt", "r", encoding="cp1254")

harfList = ['a', 'd', 'l', 'e']
olmayanHarfList = ['p', 'r', 'm', 'k', 'ç', 'y', 'o', 'ş']
pozisyondaOlmayanHarfList = [[0, 'e'], [1, 'a'], [2, 'l'], [3, 'd'], [4, 'a'], [5, 'a'], [1, 'l']]

pozisyondaHarfList = [[0, ''], [1, ''], [2, ''], [3, ''], [4, ''], [5, '']]
gecerliKelimeler = []

def HarfIcersin(word):
    for harf in harfList:
        if harf not in word:
            return False

    return True

def HarfIcermesin(word):
    for harf in olmayanHarfList:
        if harf in word:
            return False

    return True

def PozisyondaHarfIcersin(word):
    for harf in pozisyondaHarfList:
        if word[harf[0]] != harf[1]:
            return False

    return True

def PozisyonKontrol(word):
    for harf in pozisyondaOlmayanHarfList:
        if word[harf[0]] == harf[1]:
            return False

    return True


for kelime in f:
    kelime = kelime.strip('\n')
    if HarfIcersin(kelime) == False:
        continue

    if HarfIcermesin(kelime) == False:
        continue

    #if PozisyondaHarfIcersin(kelime) == False:
    #    continue

    if PozisyonKontrol(kelime) == False:
        continue

    gecerliKelimeler.append(kelime)

for kelim in gecerliKelimeler:
    print(kelim)