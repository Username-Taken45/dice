# this is only a script version to test, not the module
import random 

ToRoll = int(input() )
r1 = 0
r2 = 0
r3 = 0
r4 = 0
r5 = 0
r6 = 0
roll = 0

while ToRoll > 0:

    roll = random.randint(1, 6)
    if roll == 1:
        r1 = r1 +1
    if roll == 2:
        r2 = r2 + 1
    if roll == 3:
        r3 = r3 + 1
    if roll == 4:
        r4 = r4 + 1
    if roll == 5:
        r5 = r5 + 1
    if roll == 6:
        r6 = r6 + 1
    print(r1, r2, r3, r4, r5, r6)
    ToRoll = ToRoll -1

print(r1, r2, r3, r4, r5, r6)
