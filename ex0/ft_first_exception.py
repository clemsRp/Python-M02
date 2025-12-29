#!/usr/bin/env python3

def check_temperature(temp_str: str) -> int:
    '''
    Print a message depending the temperature,
    then return the temperature if there are no error
    '''
    try:
        num = int(temp_str)
    except Exception:
        print(f"Error: '{temp_str}' is not a valid number")
        return
    if num >= 0 and num <= 40:
        print(f"Temperature {num}°C is perfect for plants!")
    elif num < 0:
        print(f"Error: {num}°C is too cold for plants (min 0°C)")
    elif num > 40:
        print(f"Error: {num}°C is too hot for plants (max 40°C)")
    return num


if __name__ == "__main__":
    check_temperature("abc")
    check_temperature("25")
    check_temperature("100")
    check_temperature("50")
