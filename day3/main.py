from util.main import parse_file_to_lines

test_file = "day3/test.txt"
input_file = "day3/input.txt"
lines: list[str] = parse_file_to_lines(input_file)

def part_1():
    banks = lines[:]

    result = 0
    for bank in banks:
        ints = [int(b) for b in bank]
        max_tens = max(ints[:-1])
        tens_index = ints.index(max_tens)
        max_ones = max(ints[tens_index + 1:])
        joltage = max_tens * 10 + max_ones
        # print(joltage)
        result += joltage

    print(result)

def part_2():
    banks = lines[:]

    result = 0
    for bank in banks:
        ints = [int(b) for b in bank]
        joltage = 0

        current_tens = 11
        last_index = -1
        while current_tens >= 0:
            cut_ints = ints[last_index + 1:-current_tens] if current_tens != 0 else ints[last_index + 1:]
            max_num = max(cut_ints)
            max_index = ints.index(max_num, last_index + 1)
            joltage += max_num * (10 ** current_tens)
            last_index = max_index
            current_tens -= 1
        print(joltage)
        result += joltage

    print(result)

if __name__ == "__main__":
    part_2()