from dataclasses import dataclass
from typing import List, Optional, Tuple

INPUT_FILE = 'input_day10'


@dataclass
class SyntaxScoring:
    input_file: str
    brackets_map = {')': '(', '}': '{', ']': '[', '>': '<'}
    points_map = {')': 3, ']': 57, '}': 1197, '>': 25137}
    auto_complete_points_map = {')': 1, ']': 2, '}': 3, '>': 4}

    def get_syntax_score(self) -> Tuple[int, int]:
        syntax_score = 0
        auto_complete_scores = []
        with open(self.input_file, 'r', newline='') as file:
            for row in file:
                brackets = row.strip()
                illegal_bracket = self.find_first_illegal_bracket(brackets)
                if illegal_bracket is not None:
                    syntax_score += self.points_map.get(illegal_bracket, 0)

                closing_brackets = self.find_missing_closing_brackets(brackets)
                if closing_brackets is not None:
                    auto_complete_score = sum(
                        self.auto_complete_points_map.get(bracket, 0) * 5 ** i
                        for i, bracket in enumerate(reversed(closing_brackets))
                    )
                    auto_complete_scores.append(auto_complete_score)

        return syntax_score, sorted(auto_complete_scores)[len(auto_complete_scores) // 2]

    def find_missing_closing_brackets(self, brackets: str) -> Optional[List[str]]:
        stack = []
        closing_brackets = []
        for char in brackets:
            if char in self.brackets_map.values():
                stack.append(char)
            elif char in self.brackets_map.keys():
                if not stack:
                    return None
                last_opening_bracket = stack.pop()
                if self.brackets_map[char] != last_opening_bracket:
                    return None
        closing_brackets.extend(self.get_key_from_value(self.brackets_map, char) for char in reversed(stack))
        return closing_brackets

    def find_first_illegal_bracket(self, brackets: str) -> Optional[str]:
        stack = []
        for char in brackets:
            if char in self.brackets_map.values():
                stack.append(char)
            elif char in self.brackets_map.keys():
                if not stack:
                    return char
                last_opening_bracket = stack.pop()
                if self.brackets_map[char] != last_opening_bracket:
                    return char
        return None

    @staticmethod
    def get_key_from_value(dictionary, value):
        return next((key for key, val in dictionary.items() if val == value), None)


if __name__ == "__main__":
    syntax_scoring = SyntaxScoring(INPUT_FILE)
    syntax_score, middle_score = syntax_scoring.get_syntax_score()
    print(f"The answer for day 10 part 1: {syntax_score}")
    print(f"The answer for day 10 part 2: {middle_score}")