from typing import Tuple
from util.main import parse_file_to_lines

test_file = "day5/test.txt"
input_file = "day5/input.txt"
lines: list[str] = parse_file_to_lines(input_file)

def merge_ranges(ranges: list[Tuple[int, int]]):
    n = len(ranges)
    ranges.sort(key=lambda r: r[0])

    result = []
    
    for i in range(n):
        start = ranges[i][0]
        end = ranges[i][1]

        if result and result[-1][1] >= end:
            continue
        
        for j in range(i + 1, n):
            if ranges[j][0] <= end:
                end = max(end, ranges[j][1])
        result.append((start, end))
    return result

def convert_ranges(ranges: list[str]):
    return [tuple([int(n) for n in range.split("-")]) for range in ranges]
        

def part_1():
    blank_line = lines.index("")
    ranges = merge_ranges(convert_ranges(lines[:blank_line]))
    ids = [int(n) for n in lines[blank_line + 1:]]
    fresh = 0

    for id in ids:
        if any([range[0] <= id <= range[1] for range in ranges]):
            # print(id)
            fresh += 1

    print(fresh)

def part_2():
    blank_line = lines.index("")
    ranges = merge_ranges(convert_ranges(lines[:blank_line]))

    fresh_ids = 0

    for range in ranges:
        fresh_ids += range[1] - range[0] + 1

    print(fresh_ids)

if __name__ == "__main__":
    part_2()