from dataclasses import dataclass
from typing import List, Optional
import copy

INPUT_FILE = 'input_day12'


class Graph:
    def __init__(self):
        self.graph = {}

    def add_vertex(self, vertex):
        if vertex not in self.graph:
            self.graph[vertex] = []

    def add_edge(self, src, dest):
        self.add_vertex(src)
        self.add_vertex(dest)
        self.graph[src].append(dest)
        self.graph[dest].append(src)


@dataclass
class PassagePath:
    input_file: str

    def __post_init__(self):
        self.create_passage_graph()

    def create_passage_graph(self) -> None:
        self.path_graph = Graph()
        with open(self.input_file, 'r', newline='') as file:
            for row in file.readlines():
                parsed_row = row.strip().split('-')
                source = parsed_row[0]
                destination = parsed_row[1]
                self.path_graph.add_vertex(source)
                self.path_graph.add_vertex(destination)
                self.path_graph.add_edge(source, destination)

    def get_all_paths(self) -> int:
        self.visited_small_caves = set()
        self.all_paths = set()
        start = 'start'
        end = 'end'
        self.dfs(start, end, [start])
        return len(self.all_paths)

    def get_all_paths_part_2(self) -> int:
        self.visited_small_caves = set()
        self.all_paths = set()
        start = 'start'
        end = 'end'
        self.special_dfs(start, end, [((start, ), False)])
        return len(self.all_paths)

    def special_dfs(self, current, end, path):
        path, double_visited = path.pop()
        if current == 'end':
            self.all_paths.add(''.join(path[:]))
            return
        for neighbor in self.path_graph.graph[current]:
            if neighbor == 'start':
                continue
            elif neighbor.isupper() or neighbor not in path:
                new_path = [((*path, neighbor), double_visited)]
                self.special_dfs(neighbor, end, new_path)
            elif not double_visited:
                new_path = [((*path, neighbor), True)]
                self.special_dfs(neighbor, end, new_path)

    def dfs(self, current, end, path):
        if current.islower():
            self.visited_small_caves.add(current)
        if current == end:
            self.all_paths.add(''.join(path[:]))
        for neighbor in self.path_graph.graph[current]:
            if neighbor not in self.visited_small_caves:
                path.append(neighbor)
                self.dfs(neighbor, end, path)
                path.pop()
        if current.islower():
            self.visited_small_caves.remove(current)


if __name__ == "__main__":
    passage_path = PassagePath(INPUT_FILE)
    passage_path_2 = PassagePath(INPUT_FILE)
    print(f"The answer for day 12 part 1: {passage_path.get_all_paths()}")
    print(f"The answer for day 12 part 2: {passage_path_2.get_all_paths_part_2()}")
