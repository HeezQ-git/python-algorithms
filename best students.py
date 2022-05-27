# Example input:

# 3
# Oliver Moore 2.92
# Sophia Young 3.86
# Liam Allen 1.05
# Isabella Hall 4.81
# Amelia Thomas 3.23
# Oliver Walker 2.86
# James White 4.31
# Elijah Jones 1.06
# Emma Martinez 2.64
# Amelia Young 3.16
# Ava Walker 1.42
# Liam Rodriguez 1.87
# -
# Emma Hill 4.88
# Harper Thompson 5.01
# James Martin 2.95
# Harper Ramirez 5.88
# Isabella Allen 1.27
# Olivia Williams 2.94
# Oliver Lopez 4.11
# Noah Smith 3.67
# James Harris 2.70
# Isabella Roberts 5.97
# -
# Sophia Perez 3.05
# Olivia Smith 2.79
# James Robinson 3.26
# Emma Miller 4.44
# William Nelson 5.74
# Harper Harris 3.43
# Olivia Garcia 4.66
# Henry Moore 1.05
# Isabella Davis 5.81
# Oliver Ramirez 2.07
# Noah Thompson 1.09
# Alexander Baker 2.99
# Olivia Young 3.44
# Harper Nelson 3.15
# Evelyn King 4.67
# Henry White 5.24
# Noah Miller 5.91
# Charlotte Rodriguez 5.52
# Mia Rodriguez 1.26
# James Roberts 3.68
# Mia Hill 5.95
# Oliver Roberts 3.19
# Elijah Miller 1.02
# Alexander Roberts 3.49
# William Smith 2.54
# Olivia Scott 3.99
# -

# Output:
# Isabella Hall
# James White
# -
# Isabella Roberts
# -
# Mia Hill
# Noah Miller
# Isabella Davis
# -

import math

def merge(left, right):
    result = []
    left_idx, right_idx = 0, 0
    while left_idx < len(left) and right_idx < len(right):
        if left[left_idx]["average"] <= right[right_idx]["average"]:
            result.append(left[left_idx])
            left_idx += 1
        else:
            result.append(right[right_idx])
            right_idx += 1

    if left:
        result.extend(left[left_idx:])
    if right:
        result.extend(right[right_idx:])
    return result

def merge_sort(m):
    if len(m) <= 1:
        return m

    middle = len(m) // 2
    left = m[:middle]
    right = m[middle:]

    left = merge_sort(left)
    right = merge_sort(right)
    return list(merge(left, right))

classes = []

classes_amount = int(input())
_class = []
counter = 0

while counter < classes_amount:
    query = input("")
    if query == '-':
        classes.append(_class)
        _class = []
        counter += 1
    else:
        query = query.split(' ')
        _class.append({ "name": query[0], "surname": query[1], "average": query[2] })

print('\n\n')

for class_ in classes:
    class_ = merge_sort(class_)
    class_.reverse()

    top_students_amount = math.ceil((len(class_) * 10) / 100)
    for _ in range(top_students_amount):
        print(f"{class_[_]['name']} {class_[_]['surname']}")
    print('-')
