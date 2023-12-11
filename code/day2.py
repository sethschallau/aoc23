import re

def main():
    mapping = {
        'red' : 12,
        'green' : 13,
        'blue' : 14
    }
    bads = set()
    allofthem = set()
    with open('input/day2.txt', 'r') as file:
        for line in file:
            id = int(re.search(r'\d+', line).group())
            allofthem.add(id)
            bags = line.split(':')[1].strip()
            seperated = bags.split(';')
            for x in seperated:
                hands = x.strip().split(',')
                for y in hands:
                    y = y.strip().split(' ')
                    if mapping[y[1]] < int(y[0]):
                        if(id not in bads):
                            bads.add(id)
    print(sum(allofthem - bads))

if __name__ == '__main__':
    main()
