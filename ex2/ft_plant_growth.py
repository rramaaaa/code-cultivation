class Plant:
    def __init__(self, name: str, height: int, old: int) -> None:
        self.name = name
        self.height = height
        self.old = old

    def ft_get_info(self) -> None:
        print(self.name, ":", self.height, "cm,", self.old, "days old")

    def grow(self) -> None:
        self.height = self.height + 1

    def age(self) -> None:
        self.old = self.old + 1


if __name__ == "__main__":
    plant = Plant("Rose", 25, 30)
    print("=== Day 1 ===")
    plant.ft_get_info()
    for i in range(6):
        plant.grow()
        plant.age()
    print("=== Day 7 ===")
    plant.ft_get_info()
    print("Growth this week: +6cm")
