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


def mx_vec_mult(tup, vec):

    if not check_valid_mx(tup):
        return False


tup1 = ((1, 2), (3, 4), (5, 6))
vec1 = ((2), (2))

print(mx_vec_mult(tup1, vec1))


