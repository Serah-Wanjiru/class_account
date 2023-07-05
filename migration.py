
class Migration:
    def __init__(self, species, location, weather_pattern, river_levels):
        self.species = species
        self.location = location
        self.weather_pattern = weather_pattern
        self.river_levels = river_levels

    def migration(self):
        if self.weather_pattern == "dry" and self.river_levels == "low":
            print(f"Migration of {self.species} will occur from {self.location} due to lack of water and food.")
        else:
            print(f"Migration of {self.species} will not occur from {self.location} due to presence of food and water.")

migration_instance = Migration("wildebeest", "Serengeti", "wet", "high")
migration_instance.migration()