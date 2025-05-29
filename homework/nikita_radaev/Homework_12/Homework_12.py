class Flower:
    def __init__(self, name, color, stem_length, freshness, price, lifespan_days):
        self.name = name
        self.color = color
        self.stem_length = stem_length
        self.freshness = freshness  # 0–10
        self.price = price
        self.lifespan_days = lifespan_days

    def __repr__(self):
        return f"{self.name} ({self.color}) – {self.price}₽"


class Rose(Flower):
    def __init__(self, color, stem_length, freshness, price):
        super().__init__("Роза", color, stem_length, freshness, price, lifespan_days=7)


class Tulip(Flower):
    def __init__(self, color, stem_length, freshness, price):
        super().__init__("Тюльпан", color, stem_length, freshness, price, lifespan_days=5)


class Lily(Flower):
    def __init__(self, color, stem_length, freshness, price):
        super().__init__("Лилия", color, stem_length, freshness, price, lifespan_days=6)


class Bouquet:
    def __init__(self):
        self.flowers = []

    def add_flower(self, flower):
        self.flowers.append(flower)

    def total_price(self):
        return sum(f.price for f in self.flowers)

    def average_lifespan(self):
        if not self.flowers:
            return 0
        return sum(f.lifespan_days for f in self.flowers) / len(self.flowers)

    def sort_by(self, parameter):
        if hasattr(Flower, parameter) or all(hasattr(f, parameter) for f in self.flowers):
            self.flowers.sort(key=lambda f: getattr(f, parameter))
        else:
            print(f"Невозможно отсортировать по параметру: {parameter}")

    def find_by_lifespan(self, min_life):
        return [f for f in self.flowers if f.lifespan_days >= min_life]

    def __repr__(self):
        return f"Букет: {', '.join(str(f) for f in self.flowers)}"
