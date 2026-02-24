class Plant:
    def __init__(self, name, height, age):
        self.name = name
        self.height = height
        self.age = age

    def grow(self):
        self.height += 1
        print(f"{self.name} grew 1cm")

    def info_line(self):
        return f"- {self.name}: {self.height}cm"


class FloweringPlant(Plant):
    def __init__(self, name, height, age, color):
        super().__init__(name, height, age)
        self.color = color
        self.blooming = False

    def bloom(self):
        self.blooming = True

    def info_line(self):
        if self.blooming:
            state = "blooming"
        else:
            state = "not blooming"
        return f"- {self.name}: {self.height}cm, {self.color}flowers ({state})"


class PrizeFlower(FloweringPlant):
    def __init__(self, name, height, age, color, prize_points):
        super().__init__(name, height, age, color)
        self.prize_points = prize_points

    def info_line(self):
        base = super().info_line()
        return f"{base}, Prize points: {self.prize_points}"


class Garden:
    def __init__(self, owner):
        self.owner = owner
        self.plants = []
        self.total_growth = 0
        self.plants_added = 0

    def add_plant(self, plant):
        self.plants.append(plant)
        self.plants_added += 1
        print(f"Added {plant.name} to {self.owner}'s garden")

    def help_all_plant_grow(self):
        print(f"{self.owner} is helping all plants grow...")
        for plant in self.plants:
            before = plant.height
            plant.grow()
            after = plant.height
            self.total_growth += (after - before)

    def show_report(self, stats_helper):
        print(f"=== {self.owner}'s Garden Report ===")
        print("Plants in garden:")
        for plant in self.plants:
            print(plant.info_line())
        stats_helper.print_garden_analytics(self)


class GardenManager:
    def __init__(self):
        self.gardens = {}
        self.total_gardens_managed = 0
        self.stats = self.GardenStats()

    def add_garden(self, owner):
        if owner not in self.gardens:
            self.gardens[owner] = Garden(owner)
            self.total_gardens_managed += 1
        return self.gardens[owner]

    def add_plant_to_garden(self, owner, plant):
        garden = self.add_garden(owner)
        garden.add_plant(plant)

    def get_garden(self, owner):
        return self.gardens.get(owner)

    def garden_scores(self):
        scores = {}
        for owner, garden in self.gardens.items():
            scores[owner] = self.stats.score_garden(garden)
        return scores

    class GardenStats:
        @staticmethod
        def count_types(garden):
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
        def total_height(garden):
            total = 0
            for plant in garden.plants:
                total += plant.height
            return total

        @staticmethod
        def total_prize_points(garden):
            total = 0
            for plant in garden.plants:
                if hasattr(plant, "prize_points"):
                    total += plant.prize_points
            return total

        @staticmethod
        def blooming_count(garden):
            total = 0
            for plant in garden.plants:
                if hasattr(plant, "blooming") and plant.blooming:
                    total += 1
            return total

        @classmethod
        def score_garden(cls, garden):

            score = 0
            score += cls.total_height(garden)
            score += cls.total_prize_points(garden)
            score += cls.blooming_count(garden) * 10
            score += garden.total_growth
            return score

        @classmethod
        def print_garden_analytics(cls, garden):
            regular, flowering, prize = cls.count_types(garden)
            print(
                f"Plants added: {garden.plants_added}, "
                f"Total growth: {garden.total_growth}cm"
            )
            print(
                f"Plant types: {regular} regular, {flowering} flowering, "
                f"{prize} prize flowers"
            )

    @staticmethod
    def validate_height(height):
        return height >= 0

    @classmethod
    def create_garden_network(cls):
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

        return manager


if __name__ == "__main__":
    print("=== Garden Management System Demo ===\n")

    manager = GardenManager.create_garden_network()

    alice_garden = manager.get_garden("Alice")
    if alice_garden:
        alice_garden.help_all_plant_grow()
        alice_garden.show_report(manager.stats)

    print(f"Height validation test: {GardenManager.validate_height(10)}")
    scores = manager.garden_scores()
    print(
        f"Garden scores - Alice: {scores.get('Alice')}, "
        f"Bob: {scores.get('Bob')}"
    )

    print(f"Total gardens managed: {manager.total_gardens_managed}")
