class Book:
    material = "бумага"
    text = True
    reserved = False

    def __init__(self, title, avtor, numpage, ISBN):
        self.title = title
        self.avtor = avtor
        self.numpage = numpage
        self.ISBN = ISBN

    def get_data(self):

        if self.reserved is True:
            print("Название :", self.title, "Автор :", self.avtor, "cтраниц :", self.numpage, "материал :",
                  Book.material,
                  ", зарезервирована")
        else:
            print("Название :", self.title, "Автор :", self.avtor, "cтраниц :", self.numpage, "материал :",
                  Book.material)


class SchoolBook(Book):
    def __init__(self, title, avtor, numpage, ISBN, subject, klass, task):
        super().__init__(title, avtor, numpage, ISBN)
        self.subject = subject
        self.klass = klass
        self.task = task

    def get_data1(self):

        if self.reserved is True:
            print("Название :", self.title, "Автор :", self.avtor, "cтраниц :", self.numpage, "предмет :",
                  self.subject, "класс :", self.klass, ", зарезервирована")
        else:
            print("Название :", self.title, "Автор :", self.avtor, "cтраниц :", self.numpage, "предмет :",
                  self.subject, "класс :", self.klass)


books_5 = SchoolBook("Алгебра", "Толстой", "500", "34534", "Математика", "7А",
                     "True")
books_6 = SchoolBook("Геометрия", "Ленин", "600", "54534", "Математика", "7Б",
                     "True")
books_5.reserved = True
books_5.get_data1()

books = Book("Идиот,", "Достоевский,", "500,", 2424)
books_1 = Book("Му-Му,", "Тургенев,", "550,", 2424)
books_2 = Book("Властелин колец,", "Толкиен,", "1500,", 2424)
books_3 = Book("Мертвые души,", "Гоголь,", "400,", 2424)
books_4 = Book("Шарик в гостях у Барбоса,", "Носов,", "500,", 2424)

books_2.reserved = True
books_2.get_data()
