from dataclasses import dataclass
from typing import List

INPUT_FILE = 'input_day11'


@dataclass
class OctoFlashes:
    input_file: str
    octopus_grid: List[List[int]] | None = None
    total_flashes: int = 0

    def __post_init__(self):
        self.get_starting_octopus_grid()

    def get_starting_octopus_grid(self) -> None:
        self.octopus_grid = []
        with open(self.input_file, 'r', newline='') as file:
            for row in file:
                self.octopus_grid.append([int(digit) for digit in row.strip()])

    def get_octo_flash_count(self, days: int) -> int:
        for _ in range(days):
            self.let_day_pass()
        return self.total_flashes

    def get_synchronization_step(self) -> int:
        step = 0
        while not all(value == 0 for row in self.octopus_grid for value in row):
            self.let_day_pass()
            step += 1
        return step

    def let_day_pass(self):
        self.octopus_grid = [[cell + 1 for cell in row] for row in self.octopus_grid]
        for i, row in enumerate(self.octopus_grid):
            for j, cell in enumerate(row):
                if cell >= 10:
                    self.octopus_grid[i][j] = -1000000000
                    self.update_surrounding_cells(i, j)
                    self.total_flashes += 1
        self.octopus_grid = [[max(0, cell) for cell in row] for row in self.octopus_grid]

    def update_surrounding_cells(self, row_idx, column_idx):
        grid_len = len(self.octopus_grid)
        grid_width = len(self.octopus_grid[0])
        for r in range(row_idx - 1, row_idx + 2):
            for c in range(column_idx - 1, column_idx + 2):
                if (r, c) != (row_idx, column_idx) and 0 <= r < grid_len and 0 <= c < grid_width:
                    self.octopus_grid[r][c] += 1
                    if self.octopus_grid[r][c] >= 10:
                        self.octopus_grid[r][c] = -1000000000
                        self.total_flashes += 1
                        self.update_surrounding_cells(r, c)


if __name__ == "__main__":
    octo_flash_1 = OctoFlashes(INPUT_FILE)
    octo_flash_2 = OctoFlashes(INPUT_FILE)
    print(f"The answer for day 11 part 1: {octo_flash_1.get_octo_flash_count(days=100)}")
    print(f"The answer for day 11 part 2: {octo_flash_2.get_synchronization_step()}")