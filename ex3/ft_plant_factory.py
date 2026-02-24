class Plant:
    def __init__(self, name, starting_height, starting_age):
        self.name = name
        self.starting_height = starting_height
        self.starting_age = starting_age

    def create(self):
        print(
            f"Created: {self.name} ({self.starting_height}cm, "
            f"{self.starting_age} days)"
        )


if __name__ == "__main__":
    print("=== Plant Factory Output ===")
    plants = [
        Plant("Rose", 25, 30),
        Plant("Oak", 200, 365),
        Plant("Cactus", 5, 90),
        Plant("Sunflower", 80, 45),
        Plant("Fern", 15, 120)
    ]
    for i in range(len(plants)):
        plants[i].creat()
    print("\nTotal plants created:", len(plants))
