def binary_search(t, elmt):
    if len(t) == 0:
        return False
    else:
        mid = len(t) // 2
        if elmt == t[mid]:
            return True
        else:
            if elmt > t[mid]:
                return binary_search(t[mid+1:], elmt)
            else:
                return binary_search(t[:mid], elmt)
liste = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
desired = 4
desired2 = 11

binary_search(liste, desired)


for l, e in [(liste, desired), (liste, desired2), ([3], 4), ([4], 4), ([], 4), ([1, 2], 2), ([1, 2], 1), ([1, 2], 3)]:
    print(l, e, binary_search(l, e))
