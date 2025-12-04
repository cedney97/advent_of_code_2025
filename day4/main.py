from util.main import parse_file_to_lines, print_grid

test_file = "day4/test.txt"
input_file = "day4/input.txt"
lines: list[str] = parse_file_to_lines(input_file)

deltas = ((0, 1), (1, 0), (0, -1), (-1, 0), (1, 1), (-1, -1), (-1, 1), (1, -1))

def part_1():
    grid = lines
    def is_roll(r: int, c: int):
        if r < 0 or r >= len(grid) or c < 0 or c >= len(grid[r]):
            return False
        return grid[r][c] == "@"
    
    access = [[col for col in row] for row in grid]
    result = 0

    for row in range(len(grid)):
        for col in range(len(grid[row])):
            if is_roll(row, col):
                surrounding = 0
                for dr, dc in deltas:
                    surrounding += 1 if is_roll(row + dr, col + dc) else 0
                if surrounding < 4:
                    access[row][col] = "X"
                    result += 1
    
    print_grid(access)
    print(result)

def part_2():
    grid = [[col for col in row] for row in lines]
    def remove_paper(grid: list[list[str]]):
        def is_roll(r: int, c: int):
            if r < 0 or r >= len(grid) or c < 0 or c >= len(grid[r]):
                return False
            return grid[r][c] == "@"
        
        access = [[col for col in row] for row in grid]
        removed = 0

        for row in range(len(grid)):
            for col in range(len(grid[row])):
                if is_roll(row, col):
                    surrounding = 0
                    for dr, dc in deltas:
                        surrounding += 1 if is_roll(row + dr, col + dc) else 0
                    if surrounding < 4:
                        access[row][col] = "X"
                        removed += 1

        return access, removed
    
    grid, result = remove_paper(grid)
    prev_result = 0

    while result != prev_result:
        grid, removed = remove_paper(grid)
        prev_result = result
        result += removed

    print(result)

if __name__ == "__main__":
    part_2()