#!/usr/bin/env python3

def check_temperature(temp_str: str):
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
