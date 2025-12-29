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


def check_plant_error(is_wilting: bool) -> None:
    '''
    Raise a PlantError
    '''
    if is_wilting:
        raise PlantError("The tomato plant is wilting!")


def check_water_error(level: int) -> None:
    '''
    Raise WaterError
    '''
    if level <= 0:
        raise WaterError("Not enough water in the tank!")


def test_custom_errors() -> None:
    '''
    Test multiple custom errors
    '''
    print("Testing PlantError...")
    try:
        check_plant_error(True)
    except PlantError as e:
        print("Caught PlantError:", e)
    print()

    print("Testing WaterError...")
    try:
        check_water_error(0)
    except WaterError as e:
        print("Caught WaterError:", e)
    print()

    for elem in ["plant", "water"]:
        if elem == "plant":
            try:
                check_plant_error(True)
            except GardenError as e:
                print("Caught a garden error", e)
        else:
            try:
                check_water_error(0)
            except GardenError as e:
                print("Caught a garden error", e)


if __name__ == "__main__":
    print("=== Custom Garden Errors Demo ===\n")
    test_custom_errors()
    print("\nAll custom error types work correctly!")
