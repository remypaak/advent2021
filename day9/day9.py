import heapq
from dataclasses import dataclass, field
from typing import List, Dict, Tuple, Optional

INPUT_FILE = 'input_day9'


@dataclass
class Basin:
    visited: Dict[Tuple[int, int], int] = field(default_factory=dict)
    size: int = 1


@dataclass
class SmokeBasin:
    input_file: str
    height_map: List[List[int]] | None = None
    low_points: Dict[Tuple[int, int], int] | None = None
    basin_size_list: List[int] = field(default_factory=list)

    def set_height_map(self) -> None:
        self.height_map = []
        with open(self.input_file, 'r', newline='') as file:
            self.height_map = [[int(char) for char in row.strip()] for row in file.readlines()]

    def set_low_points(self) -> None:
        self.set_height_map()
        self.low_points = {}
        for row in range(len(self.height_map)):
            for column in range(len(self.height_map[0])):
                if self.is_low_point(row, column):
                    self.low_points[(row, column)] = self.height_map[row][column] + 1

    def get_sum_of_risk_point(self) -> int:
        self.set_low_points()
        return sum(self.low_points.values())

    def initialize_data(self):
        self.set_low_points()
        for (row_idx, column_idx), _ in self.low_points.items():
            basin = Basin()
            self.basin_size_list.append(self.get_basin_size(row_idx, column_idx, basin))

    def get_product_of_largest_basins(self):
        self.initialize_data()
        largest_basins = heapq.nlargest(3, self.basin_size_list)
        return largest_basins[0] * largest_basins[1] * largest_basins[2]

    def get_basin_size(self, row_idx: int, column_idx: int, basin: Basin) -> int:
        if row_idx < 0 or column_idx < 0 or row_idx >= len(self.height_map) or column_idx >= len(self.height_map[0]):
            return basin.size
        basin.visited[(row_idx, column_idx)] = True
        if (row_idx - 1, column_idx) not in basin.visited and self.get_square_above(row_idx, column_idx) not in [9, None]:
            basin.size += 1
            self.get_basin_size(row_idx - 1, column_idx, basin)
        if (row_idx + 1, column_idx) not in basin.visited and self.get_square_under(row_idx, column_idx) not in [9, None]:
            basin.size += 1
            self.get_basin_size(row_idx + 1, column_idx, basin)
        if (row_idx, column_idx - 1) not in basin.visited and self.get_square_left(row_idx, column_idx) not in [9, None]:
            basin.size += 1
            self.get_basin_size(row_idx, column_idx - 1, basin)
        if (row_idx, column_idx + 1) not in basin.visited and self.get_square_right(row_idx, column_idx) not in [9, None]:
            basin.size += 1
            self.get_basin_size(row_idx, column_idx + 1, basin)
        return basin.size

    def is_low_point(self, row_idx: int, column_idx: int) -> bool:
        point = self.height_map[row_idx][column_idx]
        neighbors = [
            self.get_square_above(row_idx, column_idx),
            self.get_square_under(row_idx, column_idx),
            self.get_square_left(row_idx, column_idx),
            self.get_square_right(row_idx, column_idx)
        ]

        for neighbor in neighbors:
            if neighbor is not None and neighbor <= point:
                return False
        return True

    def get_square_above(self, row_idx: int, column_idx: int) -> Optional[int]:
        prev_point = self.height_map[row_idx - 1][column_idx] if row_idx > 0 else None
        return prev_point

    def get_square_under(self, row_idx: int, column_idx: int) -> Optional[int]:
        next_point = self.height_map[row_idx + 1][column_idx] if row_idx < len(self.height_map) - 1 else None
        return next_point

    def get_square_left(self, row_idx: int, column_idx: int) -> Optional[int]:
        prev_point = self.height_map[row_idx][column_idx - 1] if column_idx > 0 else None
        return prev_point

    def get_square_right(self, row_idx: int, column_idx: int) -> Optional[int]:
        next_point = self.height_map[row_idx][column_idx + 1] if column_idx < len(self.height_map[0]) - 1 else None
        return next_point


if __name__ == "__main__":
    smoke_basin = SmokeBasin(INPUT_FILE)
    print(f"The answer for day 9 part 1: {smoke_basin.get_sum_of_risk_point()}")
    print(f"The answer for day 9 part 2: {smoke_basin.get_product_of_largest_basins()}")
