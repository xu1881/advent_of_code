# DAY 1 PART 1
inputs = input.split('\n')
print(inputs)
max = 0
current_calories = 0

for calorie in inputs:
    if calorie == '':
        if current_calories > max:
            max = current_calories
        current_calories = 0
    else:
        current_calories += int(calorie)
print(max)

# DAY 1 PART 2
inputs = input.split('\n')
current_calories = 0
all_elves = []

for calorie in inputs:
    if calorie == '':
        all_elves.append(current_calories)
        current_calories = 0
    else:
        current_calories += int(calorie)
print(sum(sorted(all_elves, reverse=True)[:3]))
