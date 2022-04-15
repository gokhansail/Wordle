f = open("sozlukAlti.txt", "r", encoding="cp1254")

harfList = [a,b,c]
gecerliKelimeler = []

def HarfIcersin(word):
    for harf in harfList:
        if harf not in word:
            return False

    return True

def HarfIcermesin(word):


for kelime in f:
    kelime = kelime.strip('\n')
    if HarfIcersin(kelime) == False:
        continue

    if