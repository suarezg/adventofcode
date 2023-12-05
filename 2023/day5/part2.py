from dataclasses import dataclass
import functools 

@dataclass
class Seed:
    pos: int
    has_changed: bool


with open('input.txt') as file:

    line = file.readline()
    [_, seeds] = line.split(":")
    seeds = seeds.strip().split()
    seeds = [Seed(int(s), False) for s in seeds]
    print(seeds)

    for line in file:
        if line == '\n':
            print("found new line, skipping")
            continue

        if line.find('map') != -1:
            for s in seeds:
                s.has_changed = False
            continue

        dest, src, length = [int(n) for n in line.split()]
        print(f"dest: {dest}, start: {src}, length: {length}")
        for s in seeds:
            if not s.has_changed and src <= s.pos < src + length:
                offset = s.pos - src
                s.pos = dest + offset
                s.has_changed = True

    print(f"Final locations: {seeds}") 
    print(f"Min: {functools.reduce(lambda a, b: a if a.pos < b.pos else b, seeds)}")
    