import re

def main():
    total = 0
    mapping = {
    'one': 1, '1': 1,
    'two': 2, '2': 2,
    'three': 3, '3': 3,
    'four': 4, '4': 4,
    'five': 5, '5': 5,
    'six': 6, '6': 6,
    'seven': 7, '7': 7,
    'eight': 8, '8': 8,
    'nine': 9, '9': 9
    }

    with open('input/day1.txt', 'r') as file:
        for line in file:
            left = 0
            right = 0
            pointer = 0
            while(pointer < len(line)):
                for x in mapping:
                    if len(x) <= (len(line) - pointer):
                        if line[pointer:pointer+len(x)] == x:
                            if left == 0:
                                left = right = mapping[x]
                            else:
                                right = mapping[x]
                pointer += 1

            
            total += (left * 10) + right
    print('Final: ' + str(total) + '\n')
if __name__ == '__main__':
    main()
'''
if string is length 4 and I'm on iteration 1 it's 

'''