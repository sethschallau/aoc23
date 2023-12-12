def main():
    directions = [(0, -1), (1, -1), (1, 0), (1, 1), (0, 1), (-1, 1), (-1, 0), (-1, -1)]
    matrix = []
    matrix.append(['.']*12)
    with open('input/day3.txt', 'r') as file:
        for line in file:
            line = line.strip()
            temp = []
            temp.append('.')
            for x in line:
                temp.append(x)
            temp.append('.')
            matrix.append(temp)
    matrix.append(['.']*12)


    total = 0
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if 48 <= ord(matrix[i][j]) <= 57 or ord(matrix[i][j]) == 46:
                continue

            if matrix[i][j] != '*':
                continue

            been_there = set()
            outside = []
            for dx, dy, in directions:
                temp = []
                if(48 <= ord(matrix[i+dy][j+dx]) <= 57):
                    temp.append(matrix[i+dy][j+dx])
                    left = 1
                    while(48 <= ord(matrix[i+dy][j+dx-left]) <= 57):
                        temp.insert(0,matrix[i+dy][j+dx-left])
                        left += 1
                    right = 1
                    while(48 <= ord(matrix[i+dy][j+dx+right]) <= 57):
                        temp.append(matrix[i+dy][j+dx+right])
                        right += 1
                if temp:
                    value = int(''.join(temp))
                    if value not in been_there:
                        been_there.add(value)
                        outside.append(value)

            if len(outside) == 2:
                total += outside[0] * outside[1]
    print(total)
if __name__ == '__main__':
    main()
