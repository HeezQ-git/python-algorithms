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
