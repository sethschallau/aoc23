import re

def main():
    mapping = {
    'red' : 0,
    'green' : 1,
    'blue' : 2
    }
    total = 0
    with open('input/day2.txt', 'r') as file:
        max = []
        for line in file:
            max = [0,0,0]
            id = int(re.search(r'\d+', line).group())
            bags = line.split(':')[1].strip()
            seperated = bags.split(';')
            for x in seperated:
                hands = x.strip().split(',')
                for y in hands:
                    y = y.strip().split(' ')
                    if max[mapping[y[1]]] < int(y[0]):
                        max[mapping[y[1]]] = int(y[0])

            start = 1
            for x in max:
                start *= x

            total += start
    print(total)
if __name__ == '__main__':
    main()
