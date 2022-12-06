# DAY 2 PART 1

# A,X - Rock
# B,Y - Paper
# C,Z - Scissors
game_rule = {"Z": "B", "X": "C", "Y": "A"}
shape_score = {"X": 1, "Y": 2, "Z": 3, "A": 1, "B": 2, "C": 3}
inputs = input.split('\n')
my_score = 0
for opponent,_,me in inputs:
    # draw
    if shape_score.get(opponent) == shape_score.get(me):
        my_score += 3
    # win
    if game_rule.get(me) == opponent:
        my_score += 6
    my_score += shape_score.get(me)
print(my_score)


# DAY 2 PART 2
action_score = {"X": 0, "Y": 3, "Z": 6}
winning = {"A":2, "B":3, "C":1}
losing = {"A":3, "B":1, "C":2}
draw = {"A":1, "B":2, "C":3}

inputs = input.split('\n')
my_score = 0
for opponent,_,action in inputs:
    my_score += action_score[action]
    if action == "X":
        my_score += losing[opponent]
    if action == "Y":
        my_score += draw[opponent]
    if action == "Z":
        my_score += winning[opponent]
print(my_score)
