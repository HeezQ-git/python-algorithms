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

tab = input()

nums = []
tab = tab[1:-1].split('[')
for num in tab:
    if num == '': continue
    _tab = num[:-1].split(',') if num[-1] != ',' else num[:-2].split(',')
    nums.append([int(x) for x in _tab])

unique = []
for num in nums:
    for x in num:
        if x not in unique:
            unique.append(x)

occurence = [0] * len(unique)

for num in nums:
    for x in num:
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

num = None
for i in range(len(result)):
    if result[i] == '_':
        num = result[i - 1]
        for j in nums:
            if result[i] == '_' and num in j:
                if j[0] == num and j[1] not in result: result[i] = j[1]
                elif j[0] not in result: result[i] = j[0]

print(result)
