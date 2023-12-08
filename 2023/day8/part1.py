
with open('input.txt', 'r') as file:

    directions = list(file.readline().strip('\n'))
    print(directions)

    map = dict()
    for line in file:
        if line == '\n':
            continue

        [node, options] = [s.strip().replace(' ','') for s in line.split('=')] 
        options = tuple(options.strip('()').split(','))
        map[node] = options

    step = 0
    pos = 'AAA'
    while True:
        if pos == 'ZZZ':
            break

        options = map[pos]
        action = directions[step % len(directions)]
        pos = options[0] if action == 'L' else options[1] 
        step += 1
    
    print(f"Steps: {step}")