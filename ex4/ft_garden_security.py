class SecurePlant:
    def __init__(self, name, height, age):
        self.name = name
        self.__height = height
        self.__age = age

    def set_height(self, height):
        if height < 0:
            print(f"Invalid operation attempted: height {height}cm [REJECTED]")
            print("Security: Negative height rejected")
        else:
            self.__height = height
            print(f"Height updated: {self.__height}cm [OK]")

    def set_age(self, age):
        if age < 0:
            print(f"Invalid operation attempted: age {age}days [REJECTED]")
            print("Security: Negative height rejected")
        else:
            self.__age = age
            print(f"Age updated: {self.__age} days [OK]")

    def get_height(self):
        return self.__height

    def get_age(self):
        return self.__age

    def get_info(self):
        print(
            f"Current plant: {self.name} ({self.__height}cm, "
            f"{self.__age} days)"
        )


if __name__ == "__main__":
    print("=== Garden Security System ===")
    plants = SecurePlant("Rose", 25, 30)
    print("Plant created:", plants.name)
    plants.set_height(plants.get_height())
    plants.set_age(plants.get_age())

    plants.set_height(-5)

    plants.get_info()
