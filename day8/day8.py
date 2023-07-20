from dataclasses import dataclass, field
from typing import List, Dict

INPUT_FILE = 'input_day8'


@dataclass
class DigitDisplay:
    input_file: str
    numbers: Dict = field(default_factory=dict)

    def get_total_easy_digits(self) -> int:
        with open(self.input_file, 'r', newline='') as file:
            output_digits = [
                digit for row in file.readlines() for digit in row.strip().split(' ')[-4:] if len(digit) in (2, 3, 4, 7)
            ]
        return len(output_digits)

    def get_total_production(self) -> int:
        total_production = 0
        with open(self.input_file, 'r', newline='') as file:
            for row in file.readlines():
                all_digits = [''.join(sorted(digit)) for digit in row.strip().split(' ') if digit != '|']
                self.deduct_numbers(all_digits)
                output_digits = all_digits[-4:]
                output_string = ''
                for digit in output_digits:
                    output_string += str(self.get_key_from_value(self.numbers, digit))
                total_production += int(output_string)
        return total_production

    def deduct_numbers(self, digits: List[str]):
        self.numbers = {}
        self.deduct_easy_numbers(digits)
        self.deduct_six([digit for digit in digits if len(digit) == 6])
        self.deduct_five([digit for digit in digits if len(digit) == 5])

    def deduct_five(self, digits: List[str]):
        for digit in digits:
            if self.check_chars_in_bigger_string(self.numbers[7], digit):
                self.numbers[3] = digit
                break
        for digit in digits:
            if self.check_chars_in_bigger_string(digit, self.numbers[6]) and digit != self.numbers[3]:
                self.numbers[5] = digit
                break
        for digit in digits:
            if digit != self.numbers[3] and digit != self.numbers[5]:
                self.numbers[2] = digit
                break

    def deduct_six(self, digits: List[str]):
        for digit in digits:
            if not self.check_chars_in_bigger_string(self.numbers[1], digit):
                self.numbers[6] = digit
                break
        for digit in digits:
            if self.check_chars_in_bigger_string(self.numbers[4], digit) and digit != self.numbers[6]:
                self.numbers[9] = digit
                break
        for digit in digits:
            if digit != self.numbers[6] and digit != self.numbers[9]:
                self.numbers[0] = digit
                break

    def deduct_easy_numbers(self, digits: List[str]):
        for digit in digits:
            match len(digit):
                case 2:
                    self.numbers[1] = digit
                case 3:
                    self.numbers[7] = digit
                case 4:
                    self.numbers[4] = digit
                case 7:
                    self.numbers[8] = digit

    @staticmethod
    def get_key_from_value(dictionary, value):
        return next((key for key, val in dictionary.items() if val == value), None)

    @staticmethod
    def check_chars_in_bigger_string(small_string, big_string):
        return set(small_string).issubset(set(big_string))


if __name__ == "__main__":
    digital_display = DigitDisplay(INPUT_FILE)
    print(f"The answer for day 8 part 1: {digital_display.get_total_easy_digits()}")
    print(f"The answer for day 8 part 2: {digital_display.get_total_production()}")
