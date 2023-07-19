from dataclasses import dataclass
from typing import List, Dict
import re

INPUT_FILE = 'input_day2'

@dataclass
class Submarine:
    input_file: str

    def get_coordinates(self) -> Dict[str, int]:
        pattern = r'\d+'
        coördinates = {'forward': 0, 'down': 0, 'up': 0}
        with open(self.input_file, 'r', newline='') as file:
            for row in file.readlines():
                if row[0] == 'f':
                    direction = 'forward'
                elif row[0] == 'd':
                    direction = 'down'
                elif row[0] == 'u':
                    direction = 'up'
                units = int(re.search(pattern, row).group())
                coördinates[direction] += units
        return coördinates

    def get_coordinates_2(self) -> Dict[str, int]:
        pattern = r'\d+'
        coördinates = {'forward': 0, 'down': 0, 'up': 0}
        aim = 0
        depth = 0
        horizontal_position = 0
        with open(self.input_file, 'r', newline='') as file:
            for row in file.readlines():
                units = int(re.search(pattern, row).group())
                if row[0] == 'f':
                    direction = 'forward'
                    horizontal_position += units
                    depth += (aim * units)
                elif row[0] == 'd':
                    direction = 'down'
                    aim += units
                elif row[0] == 'u':
                    direction = 'up'
                    aim -= units
        return horizontal_position * depth


    def calculate_forward_times_depth(self) -> int:
        coordinates = self.get_coordinates()
        return coordinates['forward'] * (coordinates['down'] - coordinates['up'])




submarine = Submarine(input_file = INPUT_FILE)


print(f'The answer for day 2 part 1: "{submarine.calculate_forward_times_depth()}"')
print(f'The answer for day 2 part 2: "{submarine.get_coordinates_2()}"')