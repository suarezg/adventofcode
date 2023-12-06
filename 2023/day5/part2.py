from dataclasses import dataclass
import functools 

@dataclass
class Seed:
    start: int
    end: int
    has_changed: bool


with open('input.txt') as file:

    line = file.readline()
    [_, seeds] = line.split(":")
    seeds = seeds.strip().split()
    seeds = [Seed(int(start), int(start) + int(length) - 1, False) for start, length in zip(seeds[0::2], seeds[1::2])]
    
    interval_count = len(seeds)
    original_count = interval_count
    interval_additions = 0
    for line in file:
        if line == '\n':
            continue

        if line.find('map') != -1:
            for s in seeds:
                s.has_changed = False
            continue

        dest, src, length = [int(n) for n in line.split()]
        
        new_seeds = []
        while len(seeds) > 0:
            s = seeds.pop(0)
            if s.has_changed:
                new_seeds.append(s)
                continue

            src_end = src + length - 1

            # seed interval is left or right of source interval, no overlap
            if s.end < src or s.start > src_end:
                print(f"No overlap")
                new_seeds.append(s)
                continue

            # seed interval is is enclosed by src interval
            if s.start >= src and s.end <= src_end:
                print(f"enclosed")
                new_start = dest + s.start - src
                new_end = new_start + s.end - s.start
                new_seeds.append(Seed(new_start, new_end, True))
                continue

            if s.start < src and s.end > src_end:
                print(f"mid cut")
                interval_additions += 2
                new_seeds.append(Seed(dest + src - s.start, dest + src + (src_end - src) , True)) 
                new_seeds.append(Seed(s.start, src - 1, False)) # left interval
                new_seeds.append(Seed(src_end + 1, s.end, False)) # right interval 
                continue
                

            if s.start < src:
                print(f"left cut")
                interval_additions += 1
                new_seeds.append(Seed(dest, dest + s.end - src, True)) # right interval
                new_seeds.append(Seed(s.start, src - 1, False)) # left interval
                continue

           
            print(f"right cut")
            interval_additions += 1
            new_seeds.append(Seed(dest + s.start - src, dest + s.start - src + (src_end - s.start), True)) # left interval
            new_seeds.append(Seed(src_end + 1, s.end, False)) # right interval
        
        seeds = new_seeds
        
    # print(f"\n\noriginal_count: {original_count}, additions: {interval_additions}, num of intervals: {len(seeds)}")
    # print(f"Final intervals: {seeds}") 
    print(f"Min: {functools.reduce(lambda a, b: a if a.start < b.start else b, seeds)}")
    