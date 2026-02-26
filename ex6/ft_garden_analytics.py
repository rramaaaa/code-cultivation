class Plant:
    def __init__(self, name: str, height: int, age: int) -> None:
        self.name = name
        self.height = height
        self.age = age

    def grow(self) -> None:
        self.height += 1
        print(f"{self.name} grew 1cm")

    def info_line(self) -> str:
        return f"- {self.name}: {self.height}cm"


class FloweringPlant(Plant):
    def __init__(self, name: str, height: int, age: int, color: str) -> None:
        super().__init__(name, height, age)
        self.color = color
        self.blooming = False

    def bloom(self) -> None:
        self.blooming = True

    def info_line(self) -> str:
        if self.blooming:
            state = "blooming"
        else:
            state = "not blooming"
        return f"- {self.name}: {self.height}cm, {self.color}flowers ({state})"


class PrizeFlower(FloweringPlant):
    def __init__(
        self, name: str, height: int, age: int, color: str, prize_points: int
    ) -> None:
        super().__init__(name, height, age, color)
        self.prize_points = prize_points

    def info_line(self) -> str:
        base = super().info_line()
        return f"{base}, Prize points: {self.prize_points}\n"


class Garden:
    def __init__(self, owner: str) -> None:
        self.owner = owner
        self.plants = []
        self.total_growth = 0
        self.plants_added = 0

    def add_plant(self, plant: Plant) -> None:
        self.plants.append(plant)
        self.plants_added += 1
        print(f"Added {plant.name} to {self.owner}'s garden")

    def help_all_plant_grow(self, silent: bool = False) -> None:
        if not silent:
            print(f"{self.owner} is helping all plants grow...")
        for plant in self.plants:
            before = plant.height
            if silent:
                plant.height += 1
            else:
                plant.grow()
            self.total_growth += (plant.height - before)
        print()

    def show_basic_report(self) -> None:
        print(f"=== {self.owner}'s Garden Report ===")
        print("Plants in garden:")
        for plant in self.plants:
            print(plant.info_line())


class GardenManager:
    class GardenStats:
        @staticmethod
        def count_types(garden: "Garden") -> tuple[int, int, int]:
            regular = 0
            flowering = 0
            prize = 0
            for plant in garden.plants:
                if hasattr(plant, "prize_points"):
                    prize += 1
                elif hasattr(plant, "color"):
                    flowering += 1
                else:
                    regular += 1
            return regular, flowering, prize

        @staticmethod
        def total_height(garden: "Garden") -> int:
            total = 0
            for plant in garden.plants:
                total += plant.height
            return total

        @staticmethod
        def total_prize_points(garden: "Garden") -> int:
            total = 0
            for plant in garden.plants:
                if hasattr(plant, "prize_points"):
                    total += plant.prize_points
            return total

        @staticmethod
        def blooming_count(garden: "Garden") -> int:
            total = 0
            for plant in garden.plants:
                if hasattr(plant, "blooming") and plant.blooming:
                    total += 1
            return total

        @classmethod
        def score_garden(cls, garden: "Garden") -> int:
            score = 0
            score += cls.total_height(garden)
            score += cls.total_prize_points(garden)
            score += cls.blooming_count(garden) * 10
            score += garden.total_growth
            regular, flowering, prize = cls.count_types(garden)
            score += prize * 7
            return score

        @classmethod
        def print_garden_analytics(cls, garden: "Garden") -> None:
            regular, flowering, prize = cls.count_types(garden)
            print(
                f"Plants added: {garden.plants_added}, "
                f"Total growth: {garden.total_growth}cm"
            )
            print(
                f"Plant types: {regular} regular, {flowering} flowering, "
                f"{prize} prize flowers"
            )

    def __init__(self) -> None:
        self.gardens = {}
        self.total_gardens_managed = 0
        self.stats = self.GardenStats()

    def add_garden(self, owner: str) -> Garden:
        if owner not in self.gardens:
            self.gardens[owner] = Garden(owner)
            self.total_gardens_managed += 1
        return self.gardens[owner]

    def add_plant_to_garden(self, owner: str, plant: Plant) -> None:
        garden = self.add_garden(owner)
        garden.add_plant(plant)

    def get_garden(self, owner: str) -> Garden:
        return self.gardens.get(owner)

    def garden_scores(self) -> dict:
        scores = {}
        for owner, garden in self.gardens.items():
            scores[owner] = self.stats.score_garden(garden)
        return scores

    def show_full_report(self, owner: str) -> None:
        garden = self.get_garden(owner)
        if not garden:
            return
        garden.show_basic_report()
        self.stats.print_garden_analytics(garden)

    @staticmethod
    def validate_height(height: int) -> bool:
        return height >= 0

    @classmethod
    def create_garden_network(cls) -> "GardenManager":
        manager = cls()

        oak = Plant("Oak Tree", 100, 500)
        rose = FloweringPlant("Rose", 25, 30, "red")
        sunflower = PrizeFlower("Sunflower", 50, 45, "yellow", 10)

        rose.bloom()
        sunflower.bloom()

        manager.add_plant_to_garden("Alice", oak)
        manager.add_plant_to_garden("Alice", rose)
        manager.add_plant_to_garden("Alice", sunflower)

        bob_plant = Plant("Cactus", 90, 200)
        manager.add_plant_to_garden("Bob", bob_plant)

        print()

        return manager


if __name__ == "__main__":
    print("=== Garden Management System Demo ===\n")

    manager = GardenManager.create_garden_network()

    alice_garden = manager.get_garden("Alice")
    if alice_garden:
        alice_garden.help_all_plant_grow()
        manager.show_full_report("Alice")

    bob_garden = manager.get_garden("Bob")
    if bob_garden:
        bob_garden.help_all_plant_grow(silent=True)

    print(f"Height validation test: {GardenManager.validate_height(10)}")

    scores = manager.garden_scores()
    print(
        f"Garden scores - Alice: {scores.get('Alice')}, "
        f"Bob: {scores.get('Bob')}"
    )

    print(f"Total gardens managed: {manager.total_gardens_managed}")
