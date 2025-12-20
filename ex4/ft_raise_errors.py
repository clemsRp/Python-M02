#!/usr/bin/env python3

def check_plant_health(plant_name: str, water_level: int, sunlight_hours: int):
    if plant_name == "":
        raise ValueError("Error: Plant name cannot be empty!")
    elif water_level < 1:
        raise ValueError(f"Water level {water_level} "
                         "is too low (min 1)")
    elif water_level > 10:
        raise ValueError(f"Water level {water_level} "
                         "is too high (max 10)")
    elif sunlight_hours < 2:
        raise ValueError(f"Sunlight hours {sunlight_hours} "
                         "is too low (min 2)")
    elif sunlight_hours > 12:
        raise ValueError(f"Sunlight hours {sunlight_hours} "
                         "is too high (max 12)")
    else:
        print(f"Plant '{plant_name}' is healthy!")


def test_plant_checks():
    print("Testing good values...")
    try:
        check_plant_health("Rose", 8, 5)
    except ValueError as e:
        print(e)
    print()

    print("Testing empty plant name...")
    try:
        check_plant_health("", 8, 5)
    except ValueError as e:
        print(e)
    print()

    print("Testing bad water level...")
    try:
        check_plant_health("Rose", 15, 5)
    except ValueError as e:
        print(e)
    print()

    print("Testing bad sunlight hours...")
    try:
        check_plant_health("Rose", 8, 0)
    except ValueError as e:
        print(e)


if __name__ == "__main__":
    print("=== Garden Plant Health Checker ===\n")
    test_plant_checks()
    print("\nAll error raising tests completed!")
