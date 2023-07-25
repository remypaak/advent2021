from dataclasses import dataclass
from typing import List, Counter as CounterType
from collections import Counter

INPUT_FILE = 'input_day14'


@dataclass
class Polymerization:
    input_file: str
    polymer_template: List[str] = None
    insertion_rules: dict = None

    def __post_init__(self):
        self.parse_file()

    def parse_file(self):
        self.insertion_rules = {}
        with open(self.input_file, 'r') as file:
            polymer_template, instructions = file.read().split('\n\n')
            self.polymer_template = [element.strip() for element in polymer_template]
            for instruction in instructions.splitlines():
                pair, insertion = instruction.split('->')
                self.insertion_rules[pair.strip()] = insertion.strip()

    def get_polymer_result(self, cycles: int):
        char_count = Counter()
        pair_count = self.get_polymer_template_pair_count()
        for _ in range(cycles - 1):
            new_counter = Counter()
            for pair, counter in pair_count.items():
                left_pair = pair[0] + self.insertion_rules[pair]
                right_pair = self.insertion_rules[pair] + pair[1]
                new_counter[left_pair] += counter
                new_counter[right_pair] += counter
            pair_count = new_counter

        for pair, counter in pair_count.items():
            char_count[pair[0]] += counter
            char_count[self.insertion_rules[pair]] += counter
        char_count[self.polymer_template[-1]] += 1

        return max(char_count.values()) - min(char_count.values())

    def get_polymer_template_pair_count(self) -> CounterType[str]:
        pair_count = Counter()
        for idx, polymer in enumerate(self.polymer_template):
            if idx + 2 > len(self.polymer_template):
                break
            pair_count[polymer + self.polymer_template[idx + 1]] += 1
        return pair_count


if __name__ == "__main__":
    polymerization_1 = Polymerization(INPUT_FILE)
    polymerization_2 = Polymerization(INPUT_FILE)
    print(f"The answer for day 14 part 1: {polymerization_1.get_polymer_result(10)}")
    print(f"The answer for day 14 part 2: {polymerization_2.get_polymer_result(40)}")
