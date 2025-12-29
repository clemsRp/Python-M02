#!/usr/bin/env python3

def water_plants(plant_list: list) -> None:
    '''
    Simulate the watering of multiple plants
    '''
    state = True
    print("Opening watering system")
    try:
        for plant in plant_list:
            print("Watering " + plant)
    except TypeError:
        state = False
        print(f"Error: Cannot water {plant} - invalid plant!")
    finally:
        print("Closing watering system (cleanup)")
        if state:
            print("Watering completed successfully!")


def test_watering_system() -> None:
    '''
    Test the error handling of the water_plants function
    with different list of plants
    '''
    print("Testing normal watering...")
    water_plants(["Tomato", "Carrots", "Lettuce"])
    print()

    print("Testing with error...")
    water_plants(["Tomato", "Carrots", None, "Lettuce"])
    print()


if __name__ == "__main__":
    print("=== Garden Watering System ===\n")
    test_watering_system()
    print("Cleanup always happens, even with errors!")
