# EXERCICE: Your robot 'Nono' needs to go straigth in line, but needs to clear
# its path on the way. Its path is N pads (squares), on each pads sits an
# obstacle. Nono need to take the obstacle in from of him/it, and dispose of it,
# back to its storage unit (all the way back where it started)... and do so for
# each and every obstacles on its path.
# GOAL: Print out what its path (back and forth) looks like.

# Detailed version
field_size = 10
path = []

for n in range(field_size + 1):

    if not n:
        path.append(n)
    for a in range(1, n):
        path.append(a)

    if n < field_size:
        for b in reversed(range(n - 1)):
            path.append(b)

print(path)

# One liner(~ish)
from itertools import chain
l = 10  # field_size
print(list(chain.from_iterable([[0] + [a for a in range(1, s + 1)] +
                                ([r for r in range(s - 1, 0, -1)
                                  ] if s < l - 1 else []) for s in range(1, l)
                                ])))
