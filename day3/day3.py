from dataclasses import dataclass
from typing import List, Dict

INPUT_FILE = 'input_day3'


@dataclass
class PowerConsumption:
    input_file: str

    def calculate_power_consumption(self):
        matrix = self.get_byte_list_matrix()
        gamma_digit = ''
        epsilon_digit = ''
        for i in range(0, len(matrix[0])):
            column = [row[i] for row in matrix]
            if sum(column) > (len(matrix) / 2):
                gamma_digit_unit = '1'
                epsilon_digit_unit = '0'
            else:
                gamma_digit_unit = '0'
                epsilon_digit_unit = '1'
            gamma_digit += gamma_digit_unit
            epsilon_digit += epsilon_digit_unit
        return self.binary_to_decimal(gamma_digit) * self.binary_to_decimal(epsilon_digit)

    def calculate_life_support_rating(self):
        matrix = self.get_byte_list_matrix()
        return self.calculate_oxygen_rating(matrix.copy()) * self.calculate_co2_scrubber_rating(matrix.copy())

    def calculate_oxygen_rating(self, matrix):
        for i in range(0, len(matrix[0])):
            column = [row[i] for row in matrix]
            if sum(column) >= (len(matrix) / 2):
                matrix = [row for row in matrix if not row[i] == 1]
            else:
                matrix = [row for row in matrix if not row[i] == 0]
            if len(matrix) == 1:
                break
        return self.binary_to_decimal(''.join([str(digit) for digit in matrix[0]]))

    def calculate_co2_scrubber_rating(self, matrix):
        for i in range(0, len(matrix[0])):
            column = [row[i] for row in matrix]
            if sum(column) >= (len(matrix) / 2):
                matrix = [row for row in matrix if not row[i] == 0]
            else:
                matrix = [row for row in matrix if not row[i] == 1]
            if len(matrix) == 1:
                break
        return self.binary_to_decimal(''.join([str(digit) for digit in matrix[0]]))

    def binary_to_decimal(self, binary):
        decimal = 0
        power = len(binary) - 1

        for digit in binary:
            if digit == '1':
                decimal += 2**power
            power -= 1

        return decimal

    def get_byte_list_matrix(self):
        matrix = []
        with open(self.input_file, 'r', newline='') as file:
            for row in file.readlines():
                byte_list = [int(char) for char in row.strip()]
                matrix.append(byte_list)
        return matrix


power_consumption = PowerConsumption(input_file=INPUT_FILE)

print(power_consumption.calculate_power_consumption())
print(power_consumption.calculate_life_support_rating())
