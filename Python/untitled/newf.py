"""
def bigram_hist(word):
    new_word = word.upper()
    final = {}
    counter1 = 0

    ch_list = []
    ch_list2 = []
    ch_list3 = []


    for i in range(0, len(new_word)-1):
        ch_list.append(new_word[i])
    for j in range(0, len(new_word)-1):
        ch_list2.append(new_word[j+1])

    for i in range(0, len(ch_list)):
        ch_list3.append(str(ch_list[i])+str(ch_list2[i]))

    for i in range(0, len(ch_list3)):
        counter1 = ch_list3.count(ch_list3[i])
        final.update({ch_list3[i].lower(): counter1})
    #print(final)
word = "misSissipPi"
bigram_hist(word)
"""

def topla(x,y):

    return x+y

def goster():

    return print(topla(3,5))

goster()