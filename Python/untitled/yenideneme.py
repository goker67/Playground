"""
def vec_scalar_mult(tup, scalar):
    sonuc = []
    liste = list(tup)
    for i in range(0, len(tup)):
        sonuc.append(liste[i] * scalar)

    return tuple(sonuc)

tup_ex = (2, -2, 2)
print(vec_scalar_mult(tup_ex, 2))
"""
"""
tup = (2, -2, 2)
liste = list(tup)
scalar = 2
sonuc = []
for i in range(0, len(tup)):
    sonuc.append(scalar * liste[i])
print(tuple(sonuc))
"""


def vec_inner_product(tup1, tup2):
    sonuc = []
    toplam = 0
    liste1 = list(tup1)
    liste2 = list(tup2)
    for i in range(0, len(tup1)):
        sonuc.append(liste1[i] * liste2[i])
        toplam += sonuc[i]
    print(tuple(sonuc))
    print(toplam)

"""
vec1 = (2, 2, 2)
vec2 = (-3, 1, 3)
vec_inner_product(vec1, vec2)
"""

def check_valid_mx(tup):

    liste = []

    for i in range(0, len(tup)):

        if len(tup[i]) != len(tup[i-1]):
            return False
        liste.append(list(tup[i]))

    liste2 = [j for i in liste for j in i]

    if liste2 == []:
        return False
    j = 0
    while j <= len(liste2)-1:
        if type(liste2[j]) != (int or float):
            return False
            break
        j += 1


    return True
tup1 = ((1, 2, 3), (4, 5, 6,), (7, 8, 9))
tup2 = ((1, 2), (3,  4), (5, 6))
tup3 = ((1, 2), ('a'))
tup4 = ()
tup5 = ((1, 2), (5, 6, 7))
for t in [(tup1), (tup2), (tup3), tup4, tup5]:
    print(t, check_valid_mx(t))


