from collections import deque
def main():
    processed = []
    index = 0
    total = 0
    with open('input/day4.txt', 'r') as file:
        for line in file:
            line = line.split(":")[1].strip()
            lines = line.split('|')
            winners = lines[0].strip().replace('  ', ' ')
            yours = lines[1].strip().replace('  ', ' ')
            winners = set(winners.split(' '))
            yours = set(yours.split(' '))
            intersect = len(winners & yours)
            processed.append((index, intersect))
            index += 1

    q = deque()
    for i, val in processed:
            total += 1
            q.appendleft((i,val))

    while q:
        curr = q.pop()
        if curr[1] != 0:
            for card in processed[curr[0]+1:curr[0]+curr[1]+1]:
                total += 1
                q.appendleft(card)
    print(total)
if __name__ == '__main__':
    main()
