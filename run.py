# The GOPIGo Robot here are stats:
# 1 unit moves the robot ~ 330mm
# Left & Right takes degrees

#!/usr/bin/python

from gopigo import *

## Helper functions

def cm_to_unit(cm):
    return cm / 33

def rotate(right):
    turn = move_left
    if right:
        turn = move_right
    turn(45)
    move_fwd(1)
    turn(90)
    move_fwd(1)
    turn(45)

##  Robot moving

move_fwd(cm_to_unit(25.4))

move_left(90)

for _ in range(5):
    move_fwd(cm_to_unit(232.5/5))

rotate(right=True)

for _ in range(5):
    move_fwd(cm_to_unit(288.9 / 5))

rotate(right=False)

for _ in range(5):
    move_fwd(cm_to_unit(275 / 5))
