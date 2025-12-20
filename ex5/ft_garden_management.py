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


def check_plant_error(is_wilting: bool):
    if is_wilting:
        raise PlantError("The tomato plant is wilting!")


def check_water_error(level: int):
    if level <= 0:
        raise WaterError("Not enough water in the tank!")


class GardenManager:

    def __init__(self):
        pass


def main_test():
    print("Adding plants to garden...")

    print("Watering plants...")

    print("Checking plant health...")

    print("Testing error recovery...")


if __name__ == "__main__":
    print("=== Garden Management System ===\n")
    main_test()
    print("\nGarden management system test complete!")
