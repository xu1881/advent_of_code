stacks_input = """    [S] [C]         [Z]            
[F] [J] [P]         [T]     [N]    
[G] [H] [G] [Q]     [G]     [D]    
[V] [V] [D] [G] [F] [D]     [V]    
[R] [B] [F] [N] [N] [Q] [L] [S]    
[J] [M] [M] [P] [H] [V] [B] [B] [D]
[L] [P] [H] [D] [L] [F] [D] [J] [L]
[D] [T] [V] [M] [J] [N] [F] [M] [G]"""

# Part 1
import re
# put the stacks into lists
stacks_input = stacks_input.split("\n")
stacks = []
for i in range(10):
    stacks.append([])
for stack in stacks_input[::-1]:
    stack = stack.replace("[", "").replace("] ", "").replace("]", "").replace("   ","")
    for i, letter in enumerate(stack):
        if letter != " ":
            stacks[i+1].append(letter)

input = input.split("\n")
for move in input:
    amount, stack_from, stack_to = [int(s) for s in re.findall(r'\b\d+\b', move)]
    from_len = len(stacks[stack_from])
    stacks[stack_to].extend(stacks[stack_from][from_len - amount:][::-1])
    stacks[stack_from] = [] if from_len <= amount else stacks[stack_from][:from_len - amount]
res = ''
for s in stacks[1:]:
    res += s[-1]
print(res)

# Part 2
# Just remove [::-1] from L27 
