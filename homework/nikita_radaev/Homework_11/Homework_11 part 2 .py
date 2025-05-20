class Book:
    material = "бумага"
    text = True

    def __init__(self, title, avtor, numpage, ISBN, reserved):
        self.title = title
        self.avtor = avtor
        self.numpage = numpage
        self.ISBN = ISBN
        self.reserved = reserved


class SchoolBook(Book):
    def __init__(self, title, avtor, numpage, ISBN, reserved, subject, klass, task):
        super().__init__(title, avtor, numpage, ISBN, reserved)
        self.subject = subject
        self.klass = klass
        self.task = task

    def get_data(self):

        if self.reserved is True:
            print("Название :", self.title, "Автор :", self.avtor, "cтраниц :", self.numpage, "предмет :",
                  self.subject, "класс :", self.klass, ", зарезервирована")
        else:
            print("Название :", self.title, "Автор :", self.avtor, "cтраниц :", self.numpage, "предмет :",
                  self.subject, "класс :", self.klass)


books_5 = SchoolBook("Алгебра ,", "Достоевский ,", "600 ,", "345", True,
                     "Математика ,", "7А", True)
books_6 = SchoolBook("Геометрия", "Толстой ,", "800 ,", "355", False,
                     "Геометрия ,", "10А", False)
books_5.get_data()
