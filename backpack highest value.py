values = input().split(', ')
weight = input().split(', ')
bp_max_weight = int(input())
items = []

for index, value in enumerate(values): items.append({ "value": float(value), "weight": float(weight[index]), "worth": (float(weight[index]) / float(value)) })

items = sorted(items, key=lambda k: (k['value'], k['worth']), reverse=True)

bp_worth = 0
bp_weight = 0

for item in items:
    if (bp_weight >= bp_max_weight) or (bp_weight + item["weight"] > bp_max_weight): break
    bp_weight += item["weight"]
    bp_worth += item["value"]

print(int(bp_worth))
