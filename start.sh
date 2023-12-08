#!/bin/bash

# Check if exactly one argument is provided
if [ "$#" -ne 1 ]; then
    echo "Usage: $0 <number>"
    exit 1
fi

x=$1


# Create a text file in the input directory
touch "input/day${x}.txt"

# Create a Python file in the code directory with a structure to read the input file
echo "def main():
    with open('../input/day${x}.txt', 'r') as file:
        data = file.read()
        # Process the data as needed

if __name__ == '__main__':
    main()" > "code/day${x}.py"
