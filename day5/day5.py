from dataclasses import dataclass
import numpy as np
import re
from typing import List

INPUT_FILE = 'input_day5'


@dataclass
class HydrothermalVents:
    input_file: str
    field: np.ndarray | None = None

    @staticmethod
    def parse_line(line: str) -> List[int]:
        coordinates = re.findall(r'\d+', line)
        return [int(coordinate) for coordinate in coordinates]

    def mark_field(self, line: List[int], include_diagonal: bool) -> None:
        x1, y1, x2, y2 = line
        if x1 == x2:
            self.field[min(y1, y2) : max(y1, y2) + 1, x1] += 1
        elif y1 == y2:
            self.field[y1, min(x1, x2) : max(x1, x2) + 1] += 1
        elif include_diagonal:
            if x1 < x2:
                start_idx = (x1, y1)
                end_idx = (x2, y2)
            else:
                start_idx = (x2, y2)
                end_idx = (x1, y1)
            if start_idx[1] < end_idx[1]:
                step = 1
            else:
                step = -1
            diagonal_coordinates = [
                (i, j)
                for i, j in zip(range(start_idx[0], end_idx[0] + 1), range(start_idx[1], end_idx[1] + step, step))
            ]
            for x, y in diagonal_coordinates:
                self.field[y, x] += 1

    def calculate_overlap(self, include_diagonal: bool) -> int:
        self.field = np.zeros((1000, 1000))
        with open(self.input_file, 'r', newline='') as file:
            for line in file.readlines():
                coordinates = self.parse_line(line)
                self.mark_field(coordinates, include_diagonal=include_diagonal)
        return np.count_nonzero(self.field >= 2)


if __name__ == "__main__":
    hydrothermal_vents = HydrothermalVents(INPUT_FILE)
    print(f"The answer for day 5 part 1: {hydrothermal_vents.calculate_overlap(include_diagonal=False)}")
    print(f"The answer for day 5 part 2: {hydrothermal_vents.calculate_overlap(include_diagonal=True)}")
