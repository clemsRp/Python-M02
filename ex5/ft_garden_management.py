#!/usr/bin/env python3

class GardenError(Exception):
    '''
    Class for GardenError
    '''
    pass


class PlantError(GardenError):
    '''
    Class for PlantError
    '''
    pass


class WaterError(GardenError):
    '''
    Class for WaterError
    '''
    pass


class SunlightError(GardenError):
    '''
    Class for SunlightError
    '''
    pass


class Plant:
    '''
    Simulate the behaviour of a plant
    '''

    def __init__(self, name: str, water: int, sun: int) -> None:
        '''
        Initialize the plant
        '''
        if name == "":
            raise PlantError("Plant name cannot be empty!")
        self.name = name
        self.water = water
        self.sun = sun

    def check_health(self) -> None:
        '''
        Raise an error if one of the plant's value is invalid
        '''
        if self.water < 1:
            raise WaterError(f"Water level {self.water} is too low (min 1)")
        elif self.water > 10:
            raise WaterError(f"Water level {self.water} is too high (max 10)")
        elif self.sun < 2:
            raise SunlightError(f"Sunlight hours {self.sun} "
                                "is too low (min 2)")
        elif self.sun > 12:
            raise SunlightError(f"Sunlight hours {self.sun} "
                                "is too high (max 12)")


class GardenManager:
    '''
    Simulate the behaviour of a garden manager
    '''

    def __init__(self, owner: str) -> None:
        '''
        Initialize the garden manager
        '''
        self.owner = owner
        self.plants = []

    def add_plant(self, name, water, sun) -> None:
        '''
        Add a plant to the garden manager
        '''
        try:
            plant = Plant(name, water, sun)
            self.plants.append(plant)
            print(f"Added {name} successfully")
        except PlantError as e:
            print("Error adding plant:", e)

    def water_plants(self) -> None:
        '''
        Simulate the watering of all plants
        '''
        print("Opening watering system")
        try:
            for plant in self.plants:
                plant.water += 2
                print("Watering " + plant.name + " - success")
        except TypeError:
            print(f"Error: Cannot water {plant} - invalid plant!")
        finally:
            print("Closing watering system (cleanup)")

    def check_health(self) -> None:
        '''
        Verify if all plant's health is good
        '''
        for plant in self.plants:
            try:
                plant.check_health()
                print(f"{plant.name}: healthy "
                      f"(water: {plant.water}, sun: {plant.sun})")
            except GardenError as e:
                print(f"Error checking {plant.name}:", e)


def main_test() -> None:
    '''
    Test all the different possible error cases,
    checking all the error are correctly handle
    '''
    garden = GardenManager("Alice")
    print("Adding plants to garden...")
    garden.add_plant("Tomato", 5, 8)
    garden.add_plant("Lettuce", 15, 3)
    garden.add_plant("", 6, 10)
    print()

    print("Watering plants...")
    garden.water_plants()
    print()

    print("Checking plant health...")
    garden.check_health()
    print()

    print("Testing error recovery...")
    try:
        raise WaterError("Not enough water in tank")
    except GardenError as e:
        print("Caught GardenError:", e)
        print("System recovered and continuing...")


if __name__ == "__main__":
    print("=== Garden Management System ===\n")
    main_test()
    print("\nGarden management system test complete!")
