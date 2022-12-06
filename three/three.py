# DAY 3 PART 1
inputs = input.split('\n')
priorities = 0
for racksuck in inputs:
    mid = int(len(racksuck)/2)
    for letter in racksuck[:mid]:
        if letter in racksuck[mid:]:
            priority = (ord(letter) - 96) if letter.islower() else (ord(letter) - 38)
            priorities += priority
            break
print(priorities)

# DAY 3 PART 2
inputs = input.split('\n')
priorities = i = 0
while i < len(inputs):
    for letter in inputs[i]:
        if letter in inputs[i+1] and letter in inputs[i+2]:
            priority = (ord(letter) - 96) if letter.islower() else (ord(letter) - 38)
            priorities += priority
            i += 3
            break
print(priorities)
