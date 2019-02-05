class Author():
    next_id = 0
    def __init__(self, given_name = None, family_name = None):
        self.given_name = given_name
        self.family_name = family_name
        self.Author_id = Author.next_id
        Author.next_id += 1

    def __str__(self):
        return (self.family_name +","+" "+self.given_name[0]+".")




class Document():
    def __init__(self, authors = [], title = "", year = None):
        self.authors = authors
        self.title = title
        self.year = year


    def __str__(self):
        yeni = ""
        yeni += self.authors[0].__str__()
        for i in range(1, len(self.authors)):
            yeni  += " and " + self.authors[i].__str__()

        return ("{}   ({}).  {}.".format(yeni, self.year, self.title))



class Book(Document):
    def __init__(self, authors, title, year, publisher):
        super().__init__(authors, title, year)
        self.publisher = publisher


    def __str__(self):
        return("{} {}.".format(super().__str__(), self.publisher))



author1 = Author("Isaac", "Newton")
author2 = Author("Alfred", "Whitehead")
author3 = Author("Bertrand", "Russell")
publisher = "Cambridge University Press"


#document1 = Document([author1, author2, author3], "Principia", 1687)
#print(document1)
book1 = Book([author1], "Principia", 1687, publisher)
book2 = Book([author1, author2], "Principia Mathematica", 1910, publisher)
print(book1)
print(book2)


