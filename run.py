# The GOPIGo Robot here are stats:
# 1 unit moves the robot ~ 330mm
# Left & Right takes degrees

#!/usr/bin/env python

from gopigo import *

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

def main():
    move_fwd(cm_to_unit(25.4))

    move_left(90)

    move_fwd(cm_to_unit(232.5))

    rotate(right=True)

    move_fwd(cm_to_unit(288.9))

    rotate(right=False)

    move_fwd(cm_to_unit(275))

if __name__ == "__main__":
    main()
