class Plant:
    def __init__(self, name, height, age):
        self.name = name
        self.height = height
        self.age = age


class Flower(Plant):
    def __init__(self, name, height, age, color):
        super().__init__(name, height, age)
        self.color = color

    def show_info(self):
        print(
            f"{self.name} (Flower): {self.height}cm, "
            f"{self.age} days, {self.color} color"
        )

    def bloom(self):
        print(f"{self.name} is blooming beautifully!")


class Tree(Plant):
    def __init__(self, name, height, age, trunk_diameter):
        super().__init__(name, height, age)
        self.trunk_diameter = trunk_diameter

    def show_info(self):
        print(
            f"{self.name} (Tree): {self.height}cm, "
            f"{self.age} days, {self.trunk_diameter}cm diameter"
        )

    def produce_shade(self):
        shade_area = self.trunk_diameter + 28
        print(f"{self.name} provides {shade_area} square meters of shade")


class Vegetable(Plant):
    def __init__(self, name, height, age, harvest_season, nutritional_value):
        super().__init__(name, height, age)
        self.harvest_season = harvest_season
        self.nutritional_value = nutritional_value

    def show_info(self):
        print(
            f"{self.name} (Vegetable): {self.height}cm, "
            f"{self.age} days, {self.harvest_season} harvest"
        )

    def nutrition(self):
        print(f"{self.name} is rich in {self.nutritional_value}")


if __name__ == "__main__":
    print("=== Garden Plant Types ===")
    plants = [
        Flower("Rose", 25, 30, "red"),
        Flower("Lily", 35, 40, "white"),

        Tree("Oak", 500, 1825, 50),
        Tree("Pine", 600, 2000, 40),

        Vegetable("Tomato", 80, 90, "summer", "vitamin C"),
        Vegetable("Carrot", 30, 70, "winter", "vitamin A"),
    ]

    for i in range(6):
        if isinstance(plants[i], Flower):
            plants[i].show_info()
            plants[i].bloom()
        elif isinstance(plants[i], Tree):
            plants[i].show_info()
            plants[i].produce_shade()
        else:
            plants[i].show_info()
            plants[i].nutrition()
