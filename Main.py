from itertools import permutations

#dot_positons:
positions = ['up_left', 'up_mid', 'up_right', 'mid_left', 'mid_mid', 'mid_right', 'bottom_left', 'bottom_mid', 'bottom_right']

#default available adjacent connections for each dot:
connection_dict = {
    "up_left": ['up_mid', 'mid_left', 'mid_mid', 'mid_right', 'bottom_mid'],
    "up_mid": ['up_left', 'up_right', 'mid_left', 'mid_mid', 'mid_right', 'bottom_left', 'bottom_right'],
    "up_right": ['up_mid', 'mid_left', 'mid_mid', 'mid_right', 'bottom_mid'],
    "mid_left": ['up_left', 'up_mid', 'up_right', 'mid_mid', 'bottom_left', 'bottom_mid', 'bottom_right'],
    "mid_mid": ['up_left', 'up_mid', 'up_right', 'mid_left', 'mid_right', 'bottom_left', 'bottom_mid', 'bottom_right'],
    "mid_right": ['up_left', 'up_mid', 'up_right', 'mid_mid', 'bottom_left', 'bottom_mid', 'bottom_right'],
    "bottom_left": ['up_mid', 'mid_left', 'mid_mid', 'mid_right', 'bottom_mid',],
    "bottom_mid": ['up_left', 'up_right', 'mid_left', 'mid_mid', 'mid_right', 'bottom_left', 'bottom_right'],
    "bottom_right": ['up_mid','mid_left', 'mid_mid', 'mid_right', 'bottom_mid'],
}


arrow_dict = {
'up': '\u2191',
'left': '\u2190',
'right': '\u2192',
'down:': '\u2193',
'up_left': '\u2B09',
'up_right': '\u2B08',
'down_left:': '\u2B0B',
'down_right': '\u2B0A',
}

# counts total permutations. needs to be a non-primitive type
# so it can be accessed inside function
total = [0,1]


def find_all(target, traversed, permutation, length):
    if length == 1:
        return
    possibilities = [i for i in connection_dict[target] if i not in traversed]

    while len(possibilities) != 0:
        # print(target, end=' : '); print([p for p in permutation], sep=' -> ')
        total[0] += 1; traversed.append(target); permutation.append(target)
        permreverse = permutation; permreverse.reverse()    #only for printing purposes
        find_all(possibilities.pop(0), traversed, permutation, length-1)
        traversed.remove(target); permutation.remove(target)
    if len(possibilities) == 0:
        extra_perms = list(permutations([i for i in connection_dict if i not in traversed]))
        total[1] = len(extra_perms)


for c in connection_dict:
    for l in [2,3,4,5,6,7,8,9]:
        find_all(c, [], [], l)

print((total[1] - total[0]) + total[1])