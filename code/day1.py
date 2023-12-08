import re

def main():
    total = 0
    with open('input/day1.txt', 'r') as file:
        for line in file:
            numbers = re.sub(r'\D', '', line)

            if(len(numbers) == 1):
                numbers += numbers[0]
                
            total += (int(numbers[0]) * 10) + int(numbers[-1])
    print('Final: ' + str(total) + '\n')
if __name__ == '__main__':
    main()
