#Goker Guner
"""
default="fıstıkçı şahap"
tr_en={"ş":"s",
            "ç":"c",
            "ö":"o",
            "ğ":"g",
            "ü":"u",
            "ı":"i",
            "Ş":"S",
            "Ç":"C",
            "Ö":"O",
            "Ğ":"G",
            "Ü":"U",
            "İ":"I",
            }
items=tr_en.items()
keys=tr_en.keys()
values=tr_en.values()

for i in default:
    default.replace()
    for j in keys:
        for k in values:
            if i == j:
                i == k

print(default)

"""
tr="şçöğüıŞÇÖĞÜİ"
en="scoguiSCOGUI"
tablo=str.maketrans(tr,en)
metin=input("Bir metin girin:")
print(metin.translate(tablo))
