from matrix import Matrix, zeroes, identity

I2 = Matrix([
        [1, 0],
        [0, 1]
        ])
I2_neg = Matrix([
        [-1, 0],
        [0, -1]
        ])

zero = Matrix([
        [0,0],
        [0,0]
        ])

m1 = Matrix([
        [1,2,3],
        [4,5,6]
        ])

m2 = Matrix([
        [7,-2],
        [-3,-5],
        [4,1]
        ])
    
m3 = Matrix([
        [8]
        ])
    
m3_inv = Matrix([
        [0.125]
        ])

m1_x_m2 = Matrix([
        [ 13,  -9],
        [ 37, -27]])

m2_x_m1 = Matrix([
        [ -1,   4,   9],
        [-23, -31, -39],
        [  8,  13,  18]])

m1_m2_inv = Matrix([
        [1.5, -0.5],
        [2.0555556, -0.722222222]
        ])

top_ones = Matrix([
        [1,1],
        [0,0],
        ])

left_ones = Matrix([
        [1,0],
        [1,0]
        ])

import test

