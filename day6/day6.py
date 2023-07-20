from dataclasses import dataclass, field
from collections import Counter


INPUT_FILE = 'input_day6'


@dataclass
class LanternFish:
    input_file: str
    fish_count: Counter = field(default_factory=lambda: Counter({key: 0 for key in range(9)}))

    def let_day_pass(self) -> None:
        fish_on_zero = self.fish_count[0]
        for timer, amount in self.fish_count.items():
            if timer != 0 and amount != 0:
                fish_count_on_timer = self.fish_count[timer]
                self.fish_count[timer] -= fish_count_on_timer
                self.fish_count[timer - 1] += fish_count_on_timer
        self.fish_count[6] += fish_on_zero
        self.fish_count[8] += fish_on_zero
        self.fish_count[0] -= fish_on_zero

    def get_lantern_fish_after_x_days(self, days: int) -> int:
        with open(self.input_file, 'r', newline='') as file:
            internal_timer_list = [int(digit) for digit in file.readline().split(',')]
            for internal_timer in internal_timer_list:
                if internal_timer in self.fish_count:
                    self.fish_count[internal_timer] += 1
            for day in range(days):
                self.let_day_pass()
        return sum(self.fish_count.values())


if __name__ == "__main__":
    lantern_fish_part_1 = LanternFish(INPUT_FILE)
    lantern_fish_part_2 = LanternFish(INPUT_FILE)
    print(f"The answer for day 6 part 1: {lantern_fish_part_1.get_lantern_fish_after_x_days(days=80)}")
    print(f"The answer for day 6 part 2: {lantern_fish_part_2.get_lantern_fish_after_x_days(days=256)}")
