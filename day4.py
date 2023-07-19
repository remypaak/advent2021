from dataclasses import dataclass
from typing import List, Dict
import re

INPUT_FILE = 'input_day4'


@dataclass
class BingoCard:
    matrix: List[List[str]]

    def has_bingo(self, number_draw_sequence: List) -> bool:
        for row_index in range(0, len(self.matrix)):
            if set(self.matrix[row_index]).issubset(number_draw_sequence):
                return True
        for column_index in range(0, len(self.matrix[0])):
            column = [row[column_index] for row in self.matrix]
            if set(column).issubset(number_draw_sequence):
                return True
        return False

    def sum_of_unused_numbers_for_bingo(self, number_draw_sequence):
        raw_numbers = [number for row in self.matrix for number in row]
        return sum((int(number) for number in set(raw_numbers)-set(number_draw_sequence)))



@dataclass
class Bingo:
    input_file: str
    number_draw_sequence: List[int] | None = None
    bingo_cards: List[BingoCard] | None = None

    def get_number_draw_sequence(self):
        with open(self.input_file, 'r', newline='') as file:
            self.number_draw_sequence = file.readline().split(',')


    def create_bingo_cards(self):
        self.bingo_cards = []
        with open(self.input_file, 'r', newline='') as file:
            file.readline()
            list_of_bingo_cards = [re.findall(r'\d+', row) for row in file.readlines() if row.strip() != '']
            for i in range(0, len(list_of_bingo_cards), 5):
                self.bingo_cards.append(BingoCard(list_of_bingo_cards[i:i+5]))

    def get_bingo_score(self):
        self.get_number_draw_sequence()
        self.create_bingo_cards()
        for number_index in range(5, len(self.number_draw_sequence)):
            number_sequence = self.number_draw_sequence[:number_index]
            for bingo_card in self.bingo_cards:
                if bingo_card.has_bingo(number_sequence):
                    return bingo_card.sum_of_unused_numbers_for_bingo(number_sequence) * int(self.number_draw_sequence[number_index - 1])




bingo = Bingo(INPUT_FILE)

print(bingo.get_bingo_score())
