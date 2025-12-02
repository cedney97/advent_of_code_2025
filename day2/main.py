import re
from typing import Counter
from util.main import parse_file_to_lines

def part_1(file: str):
    lines = parse_file_to_lines(file)
    ranges = lines[0].split(',')
    result = 0
    for r in ranges:
        low, high = r.split("-")
        low, high = int(low), int(high)
        for i in range(low, high + 1):
            str_i = f"{i}"
            if len(str_i) % 2 == 1:
                continue
            if str_i[0:len(str_i)//2] != str_i[len(str_i)//2:]:
                continue
            # print(r, i)
            result += i
    return result

def part_2(file: str):
    lines = parse_file_to_lines(file)
    ranges = lines[0].split(',')
    result = 0
    for r in ranges:
        low, high = r.split("-")
        low, high = int(low), int(high)
        # print("---")
        # print(r)
        for i in range(low, high + 1):
            str_i = f"{i}"
            if not re.match(r"^(.+?)\1+$", str_i):
                continue
            result += i
            # print(i)
    return result

if __name__ == "__main__":
    print(part_2("day2/input.txt"))