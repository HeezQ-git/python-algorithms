# An algorithm that takes an array from the user
# in the form of pairs of numbers to be adjacent to each other.
# The program returns an array that consists of
# adjacent numbers based on the list given by the user.

# Examples:

# Input: [[5,1],[2,3],[4,3],[1,4]]
# Output: [5, 1, 4, 3, 2]

# Input: [[4,-2],[1,4],[-3,1]]
# Output: [-2, 4, 1, -3]

# Input: [[6,5],[6,3],[9,5],[3,0],[0,1]]
# Output: [9,5,6,3,0,1]

# Input: [[5,6],[2,6],[0,1],[9,0],[3,9],[5,3]]
# Output: [2,6,5,3,9,0,1]

blocks = input()[1:-1].split('[')

numbers = []
for number in blocks:
    if number == '': continue
    _blocks = number[:-1].split(',') if number[-1] != ',' else number[:-2].split(',')
    numbers.append([int(x) for x in _blocks])

unique = []
for number in numbers:
    for x in number:
        if x not in unique:
            unique.append(x)

occurence = [0] * len(unique)

for number in numbers:
    for x in number:
        occurence[unique.index(x)] += 1

result = ['_'] * len(unique)

for i in range(len(occurence)):
    if occurence[i] == 1:
        result[0] = unique[i]
        break

for i in range(len(occurence) - 1, -1, -1):
    if occurence[i] == 1:
        result[-1] = unique[i]
        break

number = None
for i in range(len(result)):
    if result[i] == '_':
        number = result[i - 1]

        for block in numbers:
            if number not in block: continue

            if (block[0] == number) and (block[1] not in result): result[i] = block[1]
            elif block[0] not in result: result[i] = block[0]

print(result)
