from util.main import parse_file_to_lines

lines = parse_file_to_lines("day1/test.txt")
zeros = 0
dial = 50

for line in lines:
    direction = line[0]
    dist = int(line[1:])

    start = dial

    if direction == "R":
        t0 = (100 - start) % 100
    else:
        t0 = start % 100

    if t0 == 0:
        t0 = 100

    if dist >= t0:
        hits = 1 + (dist - t0) // 100
        zeros += hits

    if direction == "R":
        dial = (dial + dist) % 100
    else:
        dial = (dial - dist) % 100

print(zeros)