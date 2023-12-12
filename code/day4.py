def main():
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
            if intersect != 0:
                total += 2 ** (intersect-1)
    print(total)


if __name__ == '__main__':
    main()
