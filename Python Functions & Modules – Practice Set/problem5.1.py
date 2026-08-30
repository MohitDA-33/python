# 5. Modules and Pip – Using External Libraries

'''
1 - Import the math module and use it to:

Find the square root of 144
Calculate sin(90°) (hint: use math.radians())
'''

import math
print(math.sqrt(144))   # .sqrt is a function in python used to find the squareroot of a number.
print(math.sin(math.radians(90)))# .sin expects the angle in radians and not degree, so you calculate radians first and then you calculate sin.
