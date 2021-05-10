#!/usr/bin/env python3
import argparse
import colorsys
import math
import sys
from PIL.ImageColor import getrgb
from colors import colors


def gethex(color: tuple):
    """Converts the given RGB tuple into a hex representation."""
    converted = [hex(component)[2:].rjust(2, "0") for component in color]
    return f"#{''.join(converted)}"


def print_pretty_color(color: tuple, distance: int):
    """Prints the given RGB color tuple prettily."""
    as_hex = gethex(color)
    name = colors[color]
    distance = round(distance, 2)
    
    color_escape_code = f"\033[48;2;{color[0]};{color[1]};{color[2]}m"
    reset_escape_code = "\033[0m"
    color_rect = f"{color_escape_code}{' ' * 6}{reset_escape_code}"
    
    print(as_hex.center(20) + color_rect)
    print(name.center(20) + color_rect)
    if distance > 0.0:
        print(f"Distance {distance}".center(20) + color_rect)
    else:
        print(f"Exact match".center(20) + color_rect)


def distance(a: tuple, b: tuple) -> int:
    """Calculates the distance between two colors."""
    return math.sqrt(
        (a[0] - b[0]) ** 2 +
        (a[1] - b[1]) ** 2 +
        (a[2] - b[2]) ** 2
    )


def parse_args():
    parser = argparse.ArgumentParser(description="Finds the nearest colorname for the given color.")
    parser.add_argument("color", metavar="COLOR", type=str, help="The color to search for")
    color = parser.parse_args().color
    try:
        rgb = getrgb(color)
    except ValueError:
        print("Unable to parse color", file=sys.stdout)
        sys.exit(1)
    return rgb


def find_nearest(color: tuple) -> tuple:
    """Finds the nearest color for the given color. Returns the nearest color and the distance."""
    all_distances = {}
    for check_color in colors:
        all_distances[distance(color, check_color)] = check_color

    lowest_distance = min(all_distances.keys())
    return all_distances[lowest_distance], lowest_distance


def main():
    color = parse_args()
    nearest_color, distance = find_nearest(color)
    print_pretty_color(nearest_color, distance)


if __name__ == "__main__":
    main()
