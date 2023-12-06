from collections import namedtuple
import functools

Race = namedtuple('Race', ['t', 'd'])
with open('input2.txt', 'r') as file:
    [_,time] = file.readline().split(":")
    time = [int(t) for t in time.strip().split()]
    [_, distance] = file.readline().split(":")
    distance = [int(d) for d in distance.strip().split()]

    races = [Race(t,d) for t,d in zip(time,distance)]

    wins = []
    for r in races:
        count = 0
        for x in range(1, r.t + 1):
            count += 1 if (r.t - x) * x > r.d else 0
        wins.append(count)

    print(f"Result: {functools.reduce(lambda x,y: x*y, wins)}")