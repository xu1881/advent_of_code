# DAY 4 PART 1
inputs = input.split('\n')
count = 0
for i in inputs:
    two_elves = i.split(',')
    a, b = two_elves[0].split('-')
    c, d = two_elves[1].split('-')
    a, b, c, d = int(a), int(b), int(c), int(d)
    if (b >= d and a <= c) or(d >= b and c <= a):
        count += 1
print(count)

# DAY 4 PART 2
inputs = input.split('\n')
count = 0
for i in inputs:
    two_elves = i.split(',')
    a, b = two_elves[0].split('-')
    c, d = two_elves[1].split('-')
    a, b, c, d = int(a), int(b), int(c), int(d)
    if (c<=a<=d) or (c<=b<=d) or (a<=c<=b) or(a<=d<=b):
        count += 1
print(count)
