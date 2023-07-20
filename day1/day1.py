from dataclasses import dataclass
from typing import List

INPUT_FILE = 'input_day1'


@dataclass
class OceanDepth:
    input_file: str

    def calculate_amount_of_depth_increases(self) -> int:
        previous_depth = 1000000
        depth_increases = 0
        with open(self.input_file, 'r', newline='') as file:
            for row in file.readlines():
                current_depth = int(row)
                if current_depth > previous_depth:
                    depth_increases += 1
                previous_depth = current_depth
        return depth_increases

    def sliding_window(self):
        previous_depth = 1000000
        depth_increases = 0
        window_length = 3
        depth_list = self.get_depth_list()
        for i in range(len(depth_list) - window_length + 1):
            current_depth = sum(depth_list[i : i + window_length])
            if current_depth > previous_depth:
                depth_increases += 1
            previous_depth = current_depth
        return depth_increases

    def get_depth_list(self) -> List[int]:
        depth_list = []
        with open(self.input_file, 'r', newline='') as file:
            for row in file.readlines():
                depth_list.append(int(row))
        return depth_list


ocean_depth = OceanDepth(input_file=INPUT_FILE)

print(f'The answer for day 1 part 1 : "{ocean_depth.calculate_amount_of_depth_increases()}"')
print(f'The answer for day 1 part 2: "{ocean_depth.sliding_window()}"')
