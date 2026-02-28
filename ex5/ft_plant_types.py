class Plant:
    def __init__(self, name: str, height: int, age: int) -> None:
        self.name = name
        self.height = height
        self.age = age


class Flower(Plant):
    def __init__(self, name: str, height: int, age: int, color: str) -> None:
        super().__init__(name, height, age)
        self.color = color

    def show_info(self) -> None:
        print(
            f"{self.name} (Flower): {self.height}cm, "
            f"{self.age} days, {self.color} color"
        )

    def action(self) -> None:
        print(f"{self.name} is blooming beautifully!")


class Tree(Plant):
    def __init__(self, name: str, height: int, age: int, trunk: int) -> None:
        super().__init__(name, height, age)
        self.trunk = trunk

    def show_info(self) -> None:
        print(
            f"{self.name} (Tree): {self.height}cm, "
            f"{self.age} days, {self.trunk}cm diameter"
        )

    def action(self) -> None:
        shade_area = self.trunk + 28
        print(f"{self.name} provides {shade_area} square meters of shade")


class Vegetable(Plant):
    def __init__(
        self, name: str, height: int, age: int, harvest: int, value: str
    ) -> None:
        super().__init__(name, height, age)
        self.harvest = harvest
        self.value = value

    def show_info(self) -> None:
        print(
            f"{self.name} (Vegetable): {self.height}cm, "
            f"{self.age} days, {self.harvest} harvest"
        )

    def action(self) -> None:
        print(f"{self.name} is rich in {self.value}")


if __name__ == "__main__":
    print("=== Garden Plant Types ===")
    print()
    plants = [
        Flower("Rose", 25, 30, "red"),
        Flower("Lily", 35, 40, "white"),

        Tree("Oak", 500, 1825, 50),
        Tree("Pine", 600, 2000, 40),

        Vegetable("Tomato", 80, 90, "summer", "vitamin C"),
        Vegetable("Carrot", 30, 70, "winter", "vitamin A"),
    ]

    for i in range(6):
        plants[i].show_info()
        plants[i].action()
        print()
