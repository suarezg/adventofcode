with open('input.txt', 'r') as file:

    directions = list(file.readline().strip('\n'))
    
    map = dict()
    starts = []
    for line in file:
        if line == '\n':
            continue

        [node, options] = [s.strip().replace(' ','') for s in line.split('=')] 
        if node[-1] == 'A':
            starts.append(node)

        options = tuple(options.strip('()').split(','))
        map[node] = options

    steps = []
    for s in starts:
        step = 0
        pos = s
        while True:
            if pos[-1] == 'Z':
                break

            options = map[pos]
            action = directions[step % len(directions)]
            pos = options[0] if action == 'L' else options[1] 
            step += 1
                
        print(f'{s} reached end at step: {step}')
        steps.append(step)

    print(f"Steps: {steps}")
