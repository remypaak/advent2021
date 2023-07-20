from dataclasses import dataclass
import statistics
from typing import List

INPUT_FILE = 'input_day7'


@dataclass
class CrabSubmarine:
    input_file: str

    def calculate_fuel_p1(self) -> int:
        with open(self.input_file, 'r', newline='') as file:
            horizontal_positions = [int(digit) for digit in file.readline().split(',')]
            median = int(statistics.median(horizontal_positions))
            total_fuel = sum(abs(position - median) for position in horizontal_positions)
        return total_fuel

    def calculate_fuel_p2(self) -> int:
        with open(self.input_file, 'r', newline='') as file:
            horizontal_positions = [int(digit) for digit in file.readline().split(',')]
            fuel_costs = [
                self.get_fuel_cost(position, horizontal_positions)
                for position in range(min(horizontal_positions), max(horizontal_positions) + 1)
            ]
        return min(fuel_costs)

    @staticmethod
    def get_fuel_cost(position: int, numbers: List[int]) -> int:
        return sum(abs(n - position) * (abs(n - position) + 1) // 2 for n in numbers)


if __name__ == "__main__":
    crab_submarine = CrabSubmarine(INPUT_FILE)
    print(f"The answer for day 7 part 1: {crab_submarine.calculate_fuel_p1()}")
    print(f"The answer for day 7 part 2: {crab_submarine.calculate_fuel_p2()}")
