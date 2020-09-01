#!/usr/bin/env python3
M_IN_INCH = .0256
KMPH_IN_MPM = 3.6/60

cadence = 170

system = [20, 40]
# system = [32, 32]

cassete = [11, 28]
# cassete = [11, 50]

wheel = 26
# wheel = 29

wheel_len = wheel * M_IN_INCH * 3.14
transmission = system[0]/cassete[1], system[1]/cassete[0]
one_rotation = [wheel_len * t for t in transmission]
spd = [cadence * e * KMPH_IN_MPM for e in one_rotation]

print(wheel_len, transmission, one_rotation, spd)
