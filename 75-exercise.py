picture = [
    [0,0,0,1,0,0,0],
    [0,0,1,1,1,0,0],
    [0,1,1,1,1,1,0],
    [1,1,1,1,1,1,1],
    [0,0,0,1,0,0,0],
    [0,0,0,1,0,0,0],
]

for i, row in enumerate(picture):
    for j, num in enumerate(row):
        if bool(num):
            picture[i][j] = '*'
        else:
            picture[i][j] = ' '
    print(''.join(row))