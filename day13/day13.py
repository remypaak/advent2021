from dataclasses import dataclass
from typing import List

INPUT_FILE = 'input_day13'


@dataclass
class PaperFolding:
    input_file: str
    sheet: List[List[str]] | None = None
    instructions: List[List] | None = None

    def __post_init__(self):
        self.parse_file()

    def parse_file(self):
        with open(self.input_file, 'r') as file:
            content, instructions = file.read().split('\n\n')
            dot_map = [item.split(',') for item in content.splitlines()]
            instructions = [instruction.split(' ')[2] for instruction in instructions.split('\n')]
            self.instructions = [item.split('=') for item in instructions]
            self.fill_sheet(dot_map)

    def fill_sheet(self, dot_map):
        max_x = max([int(line[0]) for line in dot_map]) + 1
        max_y = max([int(line[1]) for line in dot_map]) + 1
        self.sheet = [['.' for _ in range(max_x)] for _ in range(max_y)]
        for coordinates in dot_map:
            x, y = int(coordinates[0]), int(coordinates[1])
            self.sheet[y][x] = '#'

    def get_visible_dots_after_x_folds(self, amount_of_folds: int):
        for fold in range(amount_of_folds):
            self.fold_paper(self.instructions[fold])
        return len([char for row in self.sheet for char in row if char == '#'])

    def get_visible_dots_after_all_folds(self) -> None:
        for instruction in self.instructions:
            self.fold_paper(instruction)
        for row in self.sheet:
            for char in row:
                print(f'  {char}', end='') if char == '#' else print('   ', end='')
            print('\n')

    def fold_paper(self, instruction: List):
        axis, line_number = instruction[0], int(instruction[1])
        if axis == 'y':
            for y in range(line_number + 1, len(self.sheet)):
                for x in range(len(self.sheet[0])):
                    if self.sheet[y][x] == '#':
                        self.sheet[y - ((y - line_number) * 2)][x] = '#'
            self.sheet = self.sheet[:line_number]
        elif axis == 'x':
            for y in range(len(self.sheet)):
                for x in range(line_number + 1, len(self.sheet[0])):
                    if self.sheet[y][x] == '#':
                        self.sheet[y][x - ((x - line_number) * 2)] = '#'
            self.sheet = [row[: -line_number - 1] for row in self.sheet]


if __name__ == "__main__":
    paper_folding = PaperFolding(INPUT_FILE)
    paper_folding_2 = PaperFolding(INPUT_FILE)
    print(f"The answer for day 13 part 1: {paper_folding.get_visible_dots_after_x_folds(amount_of_folds=1)}")
    print(f"The answer for day 13 part 2: {paper_folding_2.get_visible_dots_after_all_folds()}")
