class Book:
    material = "бумага"
    text = True

    def __init__(self, title, avtor, numpage, ISBN, reserved):
        self.title = title
        self.avtor = avtor
        self.numpage = numpage
        self.ISBN = ISBN
        self.reserved = reserved

    def get_data(self):
        if self.reserved is True:
            print("Название :", self.title, "Автор :", self.avtor, "cтраниц :", self.numpage, "материал :",
                  Book.material,
                  ", зарезервирована")
        else:
            print("Название :", self.title, "Автор :", self.avtor, "cтраниц :", self.numpage, "материал :",
                  Book.material)


books = Book("Идиот,", "Достоевский,", "500,", 2424, reserved=False)
books_1 = Book("Му-Му,", "Тургенев,", "550,", 2424, reserved=True)
books_2 = Book("Властелин колец,", "Толкиен,", "1500,", 2424, reserved=False)
books_3 = Book("Мертвые души,", "Гоголь,", "400,", 2424, reserved=True)
books_4 = Book("Шарик в гостях у Барбоса,", "Носов,", "500,", 2424, reserved=False)

books_1.get_data()
