#!/usr/bin/env python3

import numpy as np

I = np.float32(
    [[209, 30, 247, 61 , 27 , 202, 159, 101, 146, 36 ],
     [36, 7, 58, 250, 106, 83, 6, 47, 114, 120 ],
     [211, 0, 168, 124, 4, 141, 49, 137, 188, 15],
     [115, 219, 48, 72, 10, 29, 213, 244, 193, 234],
     [203, 97, 148, 131, 194, 139, 183, 147, 106, 48],
     [109, 65, 30, 65, 23, 54, 108, 18, 187, 117],
     [238, 197, 227, 118, 99, 179, 158, 208, 62, 81],
     [246, 8, 79, 230, 39, 113, 154, 191, 160, 202]]
)

H = np.float32(
    [[114, 118, 112],
     [203, 229, 4],
     [170, 88, 13]]
)

print(I.shape)
print(H.shape)
